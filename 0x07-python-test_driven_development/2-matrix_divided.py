#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.

The 2-matrix_divided module supplies one function, matrix_divided()
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix

    Args:
        matrix(:obj:`list`): The list of integers or floats
        div(:obj:`int` or `float`): The integer or float divisor
    """
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
