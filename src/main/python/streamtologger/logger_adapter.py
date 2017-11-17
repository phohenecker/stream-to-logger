# -*- coding: utf-8 -*-


import datetime
import logging


__author__ = "Patrick Hohenecker"
__copyright__ = (
        "Copyright (c) 2017 Patrick Hohenecker\n"
        "\n"
        "Permission is hereby granted, free of charge, to any person obtaining a copy\n"
        "of this software and associated documentation files (the \"Software\"), to deal\n"
        "in the Software without restriction, including without limitation the rights\n"
        "to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n"
        "copies of the Software, and to permit persons to whom the Software is\n"
        "furnished to do so, subject to the following conditions:\n"
        "\n"
        "The above copyright notice and this permission notice shall be included in all\n"
        "copies or substantial portions of the Software.\n"
        "\n"
        "THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n"
        "IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n"
        "FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n"
        "AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n"
        "LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n"
        "OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\n"
        "SOFTWARE."
)
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
        header_format (str): This is an optional format string that specifies a line header that is prepended to each
            line. ``start_format`` is supposed to specify a format for new-style formatting with `String.Formatter`
            (which is used whenever ``"some string".format(...)`` is invoked), and may use the named elements ``level``,
            for the logging level (as string), and ``timestamp``, for a current timestamp. A valid ``start_format``
            could look like this:

                start_format = "[{timestamp:%Y-%m-%d %H:%M:%S} - {level:8}] "
    """

    def __init__(
            self,
            logger: logging.Logger,
            log_level: int=logging.INFO,
            header_format: str=None
    ):
        """Creates a new instance of ``LoggerAdapter`` that uses the provided logger and logging level.

        Args:
            logger (logging.Logger): Specifies the attribute :attr:`logger`.
            log_level (int, optional): Specifies the attribute :attr:`log_level`, which is set to `logging.INFO` by
                default.
            header_format (str, optional): Specifies the attribute :attr:`header_format`.
        """
        self._new_line = True  # indicates whether the next write starts a new line
        self.logger = logger
        self.log_level = log_level
        self.header_format = header_format

    def write(self, buffer) -> None:
        # split buffer into lines
        lines = buffer.splitlines()

        # determine whether to add a final "\n"
        # this is important, e.g., if we redirect stdout to a logger, and print(..., end="") is invoked
        final_new_line = len(buffer) > 0 and buffer[-1] == "\n"

        # forward provided buffer to the logger
        for index, line in enumerate(lines, start=1):

            # print line header (if specified)
            if self.header_format is not None and (index > 1 or self._new_line):
                self.logger.log(
                        self.log_level,
                        self.header_format.format(
                                level=logging.getLevelName(self.log_level),
                                timestamp=datetime.datetime.now()
                        )
                )

            # log current line
            self.logger.log(self.log_level, line)

            # add newline (if necessary)
            last_line = index == len(lines)
            if (not last_line) or (last_line and final_new_line):
                self.logger.log(self.log_level, "\n")

        # store whether the next write starts a new line
        self._new_line = final_new_line

    def flush(self) -> None:
        """This method does not implement any functionality, but is only present in order to prevent errors."""
        pass
