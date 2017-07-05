#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""This is the setup file of the stream-to-logger package."""


from distutils.core import setup


__author__ = "Patrick Hohenecker"
__copyright__ = \
        """
        Copyright (c) 2017 Patrick Hohenecker

        Permission is hereby granted, free of charge, to any person obtaining a copy
        of this software and associated documentation files (the "Software"), to deal
        in the Software without restriction, including without limitation the rights
        to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
        copies of the Software, and to permit persons to whom the Software is
        furnished to do so, subject to the following conditions:

        The above copyright notice and this permission notice shall be included in all
        copies or substantial portions of the Software.

        THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
        IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
        FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
        AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
        LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
        OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
        SOFTWARE.
        """
__license__ = "MIT License"
__version__ = "2017.1"
__date__ = "Jul 05, 2017"
__maintainer__ = "Patrick Hohenecker"
__email__ = "mail@paho.at"
__status__ = "Production"


# read the long description from the read me file
long_description = open("README.md").read()

setup(
    author="Patrick Hohenecker",
    author_email="mail@paho.at",
    classifiers=[
            "Programming Language :: Python :: 3"
    ],
    install_requires=[],
    long_description=long_description,
    name="stream-to-logger",
    version="2017.1",
    package_dir={"": "src/main/python"},
    packages=["streamtologger"]
)
