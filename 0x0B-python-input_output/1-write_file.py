#!/usr/bin/python3
"""The ``1-write_file`` module

The module contains one function ``write_file``
"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the
        number of characters written
    """
    with open(filename, mode='w', encoding='utf-8') as a_file:
        nWrite = a_file.write(text)
    return nWrite
