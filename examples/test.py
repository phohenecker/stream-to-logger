#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A simple example of how to redirect stdout."""


import logging
import sys

import streamtologger


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


# create the logger that is used in this example
root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)

# setup logging to console
console_handler = logging.StreamHandler(stream=sys.stdout)
console_handler.terminator = ""
root_logger.addHandler(console_handler)

# setup logging to file
file_handler = logging.FileHandler("stdout.log")
file_handler.terminator = ""
root_logger.addHandler(file_handler)

# redirect stdout/stderr to the logger
sys.stdout = streamtologger.LoggerAdapter(root_logger)
sys.stderr = streamtologger.LoggerAdapter(root_logger, log_level=logging.ERROR)

# a few prints
print("line 1")
print("line 2.1", end="")
print(" line 2.2")
print("line 3")

# have a look at the file stdout.log!!!
