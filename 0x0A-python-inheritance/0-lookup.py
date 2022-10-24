#!/usr/bin/python3
"""This is a ``lookup`` module
"""


def lookup(obj):
    """Returns the list of available attributes and
        methods of an object

    Arg:
        obj: Object
    """
    return dir(obj)
