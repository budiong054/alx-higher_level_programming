#!/usr/bin/python3
"""The ``0-read_file`` module

The module contains one function ``read_file``
"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, mode='r', encoding='utf-8') as a_file:
        print(a_file.read(), end="")
