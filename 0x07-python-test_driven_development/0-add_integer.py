#!/usr/bin/python3
"""
This is the "0-add_integer" module.

The 0-add_integer module supplies one function, add_integer().
For example,

>>> add_integer(10, 20)
30
"""


def add_integer(a, b=98):
    """Return the sum of the two integers

    Args:
        a(:obj:`int`): The first integer
        b(:obj:`int`): The second integer
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    else:
        a, b = int(a), int(b)

    return a + b
