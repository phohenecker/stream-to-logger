#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A simple example of how to redirect stdout."""


import logging
import sys

import streamtologger


__author__ = "Patrick Hohenecker"
__copyright__ = \
        """
        Copyright (c) 2017, Patrick Hohenecker
        All rights reserved.

        Redistribution and use in source and binary forms, with or without
        modification, are permitted provided that the following conditions are met:
            * Redistributions of source code must retain the above copyright
              notice, this list of conditions and the following disclaimer.
            * Redistributions in binary form must reproduce the above copyright
              notice, this list of conditions and the following disclaimer in the
              documentation and/or other materials provided with the distribution.
            * Neither the name of the <organization> nor the
              names of its contributors may be used to endorse or promote products
              derived from this software without specific prior written permission.

        THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
        ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
        WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
        DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
        DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
        (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
        LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
        ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
        (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
        SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
        """
__license__ = "BSD License 2.0"
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
