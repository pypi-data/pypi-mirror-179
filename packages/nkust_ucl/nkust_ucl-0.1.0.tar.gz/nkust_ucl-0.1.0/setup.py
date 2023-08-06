# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="nkust_ucl",
    #author_email="asdewq45445@gmail.com",
    version="0.1.0",
    #url="https://github.com/XinBow99",
    description="A pip package",
    license="MIT",
    author="a9931543",
    packages=["nkust_ucl"],
    install_requires=[],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
    ]
)
