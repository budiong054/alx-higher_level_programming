#!/usr/bin/python3
"""This is ``3-is_kind_of_class`` module

This module contains ``is_kind_of_class`` function
"""


def is_kind_of_class(obj, a_class):
    """Returns `True` if the object is an instance of, or if the object
        is an instance of a class that inherited from, the specified class;
        other wise `False`
    """
    return isinstance(obj, a_class)
