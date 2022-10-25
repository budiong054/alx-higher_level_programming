#!/usr/bin/python3
"""The ``2-append_write`` module

The module contains one function ``append_write``
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8) and returns
        the number of characters added
    """
    with open(filename, mode='a', encoding='utf-8') as a_file:
        nAppend = a_file.write(text)    # number of character written
    return nAppend
