import os
from pathlib import Path
from typing import Tuple, Union, Optional
import click
from loguru import logger
import eventlet
import time


def run_forever():
    while True:
        time.sleep(8888)


@click.group()
def pon_cli():
    pass


@pon_cli.command()
@click.argument('services', nargs=-1, required=True)
@click.option('--config', help='config file path')
def run(services: Tuple[str], config: Optional[str] = None):
    """ 启动 pon 服务 """
    config_filepath: Path = Path(os.getcwd())/config
    from pon.events import EventletEventRunner
    from pon.web import EventletAPIRunner

    eventlet.spawn_n(EventletEventRunner().run, services, config_filepath)
    eventlet.spawn_n(EventletAPIRunner().run, services, config_filepath)

    gt = eventlet.spawn(run_forever)
    gt.wait()


@pon_cli.command()
@click.option('--config', help='config file path')
def shell(file_path: str = None):
    """ shell 交互环境 """
    pass


cli = click.CommandCollection(sources=[pon_cli])

if __name__ == '__main__':
    cli()
