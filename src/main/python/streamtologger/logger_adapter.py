# -*- coding: utf-8 -*-


import logging


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


class LoggerAdapter(object):
    """This is an object that pretends to be a stream, but redirects writes to a ``Logger``.

    Attributes:
        log_level (int): The logging level that is used when invoking the :attr:`logger`.
        logger (logging.Logger): The logger object that is used to produce output. To support correct logging of any
            kind of output, the provided logger should use an empty terminator, i.e., ``logger.terminator = ""``.
            Furthermore, formatting is not supported.

    Note:
        This class is based on the code provided on
        `https://www.electricmonk.nl/log/2011/08/14/redirect-stdout-and-stderr-to-a-logger-in-python/`_
    """

    def __init__(self, logger: logging.Logger, log_level: int=logging.INFO):
        """Creates a new instance of ``LoggerAdapter`` that uses the provided logger and logging level.

        Args:
            logger (logging.Logger): Specifies the attribute :attr:`logger`.
            log_level (int, optional): Specifies the attribute :attr:`log_level`, which is set to `logging.INFO` by
                default.
        """
        self.logger = logger
        self.log_level = log_level

    def write(self, buffer) -> None:
        # split buffer into lines
        lines = buffer.splitlines()

        # determine whether to add a final "\n"
        # this is important, e.g., if we redirect stdout to a logger, and print(..., end="") is invoked
        final_new_line = len(lines) == 1 and len(buffer) > 0 and buffer[-1] == "\n"

        # forward provided buffer to the logger
        for index, line in enumerate(lines, start=1):
            # log current line
            self.logger.log(self.log_level, line)

            # add newline (if necessary)
            last_line = index == len(lines)
            if (not last_line) or (last_line and final_new_line):
                self.logger.log(self.log_level, "\n")

    def flush(self) -> None:
        """This method does not implement any functionality, but is only present in order to prevent errors."""
        pass
