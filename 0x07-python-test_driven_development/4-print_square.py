#!/usr/bin/python3
"""
This is ``4-print_square`` module.

The 4-print_square module supplies one function, print_square().
"""

def print_square(size):
    """Prints a square with the character `#`

    Args:
        size(:obj:`int`): The size length of the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            print(size * "#")
