#!/usr/bin/python3
"""This modules contains a Square class
"""


class Square:
    """Square defines a private instance attribute `size`.
    """
    def __init__(self, size):
        """
        Args:
            size (:obj:`int`): The size of the square.
        """
        self.__size = size
