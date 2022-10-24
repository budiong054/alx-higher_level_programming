#!/usr/bin/python3
"""The ``10-square`` module

The module contains one class ``Square``
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle class
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def area(self):
        """Returns the area of the square
        """
        return self.__size * self.__size
