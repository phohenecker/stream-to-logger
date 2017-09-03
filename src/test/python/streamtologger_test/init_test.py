#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import sys
import typing
import unittest

import streamtologger


__author__ = "Patrick Hohenecker"
__copyright__ = (
        "Copyright (c) 2017 Patrick Hohenecker"
        "\n\n"
        "Permission is hereby granted, free of charge, to any person obtaining a copy "
        "of this software and associated documentation files (the \"Software\"), to deal "
        "in the Software without restriction, including without limitation the rights "
        "to use, copy, modify, merge, publish, distribute, sublicense, and/or sell "
        "copies of the Software, and to permit persons to whom the Software is "
        "furnished to do so, subject to the following conditions:"
        "\n\n"
        "The above copyright notice and this permission notice shall be included in all "
        "copies or substantial portions of the Software."
        "\n\n"
        "THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR "
        "IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, "
        "FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE "
        "AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER "
        "LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, "
        "OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE "
        "SOFTWARE."
)
__license__ = "MIT License"
__version__ = "2017.1"
__date__ = "Aug 31, 2017"
__maintainer__ = "Patrick Hohenecker"
__email__ = "mail@paho.at"
__status__ = "Development"


class InitTest(unittest.TestCase):

    @staticmethod
    def _read_file(path: str) -> typing.List[str]:
        """Reads the file at the provided path and returns a list of its lines.

        Args:
            path (str): The path of the file to read.

        Returns:
            list[str]: A list of the lines in the file at ``path``.
        """
        with open(path) as f:
            return [line.strip() for line in f]

    def test_redirect(self) -> None:
        # this is the path of the log file that is used in this test
        log_file = "test-out.log"

        # delete the log file if exists already
        if os.path.isfile(log_file):
            os.remove(log_file)

        # write some text to the log file, which is supposed to be overwritten by the logger
        with open(log_file, "w") as f:
            f.write("Veni, vidi, vici!\n")
            f.write("Alea iacta est!")

        streamtologger.redirect(target=log_file, append=False, print_to_screen=False)
        print("line 1")
        print("line 2.1", end="")
        print(", line 2.2")

        self.assertEqual(["line 1", "line 2.1, line 2.2"], self._read_file(log_file))

        # delete created log file again
        os.remove(log_file)
