from setuptools import setup


def readme():
    with open("README.rst") as f:
        return f.read()


setup(
    name="evsauto",
    version="0.1",
    description="Everett's personal collection of wrappers/drivers for python-based automation projects.",
    long_description=readme(),
    classifiers=[
        "License: MIT License",
        "Topic: Webdrivers | Excel Files | File Infra.",
    ],
    url="https://github.com/everettadw/evsauto",
    author="Everett Daniels-Wright",
    author_email="business@everettdw.com",
    license="MIT",
    packages=["evsauto"],
    install_requires=[
        "selenium",
        "webdriver-manager",
        "openpyxl",
        "tomlkit",
    ],
    zip_safe=False,
)
