import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

from pon import VERSION

setuptools.setup(
    name="ponponon",
    version=VERSION,
    author="ponponon",
    author_email="1729303158@qq.com",
    maintainer='ponponon',
    maintainer_email='1729303158@qq.com',
    license='MIT License',
    platforms=["all"],
    description="An advanced message queue framework, derived from nameko",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ponponon/pon",
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries'
    ]
)
