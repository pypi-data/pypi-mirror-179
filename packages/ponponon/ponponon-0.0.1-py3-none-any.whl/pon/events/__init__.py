import os
import sys
from typing import Tuple, ClassVar, Type, Dict, List
import yaml
from pathlib import Path
from loguru import logger
from kombu import Exchange, Queue
from kombu import Connection, Consumer, Queue
from kombu.transport.pyamqp import Channel
from kombu.utils.compat import nested
from typing import Callable
from collections import namedtuple
from pon.events.message import MessageConsumer
from pon.standalone.events import get_event_exchange


class QueueLine:
    queue: Queue
    service_cls: Type
    method: Callable

    def __init__(self, queue: Queue, service_cls: Type, method: Callable) -> None:
        self.queue = queue
        self.service_cls = service_cls
        self.method = method


class EventletEventRunner:
    amqp_uri: str
    queues: List[QueueLine]

    def __init__(self) -> None:
        self.put_patch()

    def put_patch(self) -> None:
        import eventlet
        eventlet.monkey_patch()  # noqa (code before rest of imports)

    def load_service_cls_list(self, services: Tuple[str]) -> List[type]:
        BASE_DIR: Path = Path(os.getcwd())
        sys.path.append(BASE_DIR)

        service_cls_list: List[type] = []

        for service in services:

            logger.debug(service)

            items: List[str] = service.split(':')
            if len(items) == 1:
                module_name, service_class_name = items[0], None
            elif len(items) == 2:
                module_name, service_class_name = items
            else:
                raise Exception(f'错误的 service 格式: {service}')

            __import__(module_name)

            module = sys.modules[module_name]

            service_cls = getattr(module, service_class_name)

            service_cls_list.append(service_cls)

        return service_cls_list

    def load_config(self, config_filepath: Path):
        with open(config_filepath, 'r', encoding='utf-8') as f:
            config: Dict[str, Dict] = yaml.safe_load(f)
        self.amqp_uri = config['AMQP_URI']

        logger.debug(self.amqp_uri)

    def declare_exchange(self, exchange: Exchange):
        with Connection(self.amqp_uri) as conn:
            with conn.channel() as channel:
                exchange.declare(channel=channel)

    def declare_queue(self, queue: Queue):
        with Connection(self.amqp_uri) as conn:
            with conn.channel() as channel:
                queue.declare(channel=channel)

    def run(self, services: Tuple[str], config_filepath: Path):
        self.load_config(config_filepath)

        self.queues: List[QueueLine] = []

        service_cls_list: List[type] = self.load_service_cls_list(services)

        from pon.events.entrance import PON_METHOD_ATTR_NAME

        logger.debug(service_cls_list)

        # 1. 去 rabbitmq 创建消息队列

        for service_cls in service_cls_list:
            for item in dir(service_cls):
                cls_property: Callable = getattr(service_cls, item)
                if hasattr(cls_property, PON_METHOD_ATTR_NAME):
                    consumer_method = cls_property

                    pon_consumer_func_config = getattr(
                        consumer_method, PON_METHOD_ATTR_NAME)
                    # 获取修饰器附加的参数
                    source_service: str = pon_consumer_func_config['source_service']
                    event_name: str = pon_consumer_func_config['event_name']

                    exchange_name = get_event_exchange(
                        source_service).name
                    routing_key: str = event_name

                    exchange = Exchange(exchange_name, type='topic')

                    self.declare_exchange(exchange)

                    queue_name = f'evt-{exchange_name}-{routing_key}--{service_cls.name}.{consumer_method.__name__}'

                    queue = Queue(queue_name, exchange,
                                  routing_key, durable=True, queue_arguments={'x-max-priority': 10})
                    self.declare_queue(queue)
                    self.queues.append(QueueLine(
                        queue, service_cls, consumer_method))
                    logger.debug(f'queue: {queue_name}')

        # 2. 开始监听和消费
        with Connection(self.amqp_uri) as conn:
            consumers: List[Consumer] = []
            for queueline in self.queues:

                channel: Channel = conn.channel()
                consumer = Consumer(
                    channel,
                    queues=[queueline.queue],
                    prefetch_count=1,
                    on_message=MessageConsumer(
                        queue=queueline.queue,
                        service_cls=queueline.service_cls,
                        consumer_method=queueline.method
                    ).handle_message
                )
                consumers.append(consumer)

            logger.debug(consumers)

            with nested(*consumers):
                while True:
                    try:
                        conn.drain_events()
                    except Exception as error:
                        logger.exception(error)
