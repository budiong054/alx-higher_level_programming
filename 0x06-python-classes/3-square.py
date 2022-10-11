#!/usr/bin/python3
"""This modules contains a Square class
"""


class Square:
    """Square defines a private instance attribute `size`.
    """
    def __init__(self, size=0):
        """
        Args:
            size (:obj:`int`): The size of the square.
        """
        if type(size) != int:
            print("size must be an integer", end="")
            raise TypeError
        else:
            self.__size = size
        if size < 0:
            print("size must be >= 0", end="")
            raise ValueError

    def area(self):
        """Returns the area of the square."""
        return self.__size * self.__size
