#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

deps (requires up2date version):
    *) pip install --upgrade pip wheel setuptools twine
publish to pypi w/o having to convert Readme.md to RST:
    1) #> python setup.py sdist bdist_wheel
    2) #> twine upload dist/*   #<specify bdist_wheel version to upload>; #optional --repository <testpypi> or  --repository-url <testpypi-url>

'''
import os
from setuptools import setup, find_packages

version = "0.0.3"
name = "solidityParserPlus"

setup(
    name=name,
    version=version,
    packages=find_packages(),
    author="t0hka",
    author_email="s4ndalph0n.t0hka@gmail.com",
    description=(
        "A Solidity parser for Python built on top of a robust ANTLR4 grammar"),
    license="MIT",
    keywords=["solidity","parser","antlr"],
    url="https://github.com/VelitasDao/python-solidity-parser",
    long_description_content_type='text/markdown',
    install_requires=["antlr4-python3-runtime==4.9.3"],
)
