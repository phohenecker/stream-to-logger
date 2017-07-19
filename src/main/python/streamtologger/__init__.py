# -*- coding: utf-8 -*-

"""The root of the provided python package, which contains a single module."""


import logging
import sys
import typing

from streamtologger.logger_adapter import LoggerAdapter


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


def redirect(target: typing.Union[logging.Logger, str]="out.log", print_to_screen: bool=True) -> None:
    """Redirects stdout/stderr to the specified target.

    Args:
        target (optional): If ``target`` is a `logging.Logger`, then stdout and stderr are simply redirected to it.
            Otherwise, ``target`` is expected to specify the path of a file that all output should be written to (in
            addition to the usual printing to the screen if ``print_to_screen`` is ``True``). In this case, an
            appropriate ``logging.Logger`` is created and configured automatically, and stdout as well as stderr are
            redirected to it.
        print_to_screen (bool, optional): Indicates whether stdout and stderr should be printed to the console in
            addition to writing them to a file. This arg is ``True`` by default, and is ignored if ``target`` is an
            instance of `logging.Logger`.
    """
    # if the provided target is a logger, then redirect stdout/stderr to it
    if isinstance(target, logging.Logger):
        # redirect stdout/stderr to the logger
        sys.stdout = LoggerAdapter(target)
        sys.stderr = LoggerAdapter(target, log_level=logging.ERROR)
    # otherwise, create a new logger that logs to the console as well as to a file, and redirect stdout/stderr to it
    else:
        # create the logger that is used to print+store output
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.INFO)

        # setup logging to console
        if print_to_screen:
            console_handler = logging.StreamHandler(stream=sys.stdout)
            console_handler.terminator = ""
            root_logger.addHandler(console_handler)

        # setup logging to file
        file_handler = logging.FileHandler(target)
        file_handler.terminator = ""
        root_logger.addHandler(file_handler)

        # redirect stdout/stderr to the logger
        sys.stdout = LoggerAdapter(root_logger)
        sys.stderr = LoggerAdapter(root_logger, log_level=logging.ERROR)
