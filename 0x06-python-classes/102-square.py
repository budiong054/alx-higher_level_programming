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
        self.size = size

    def __str__(self):
        return str(self.__size * self.__size)

    def __lt__(self, other):
        return self.size < other.size

    def __le__(self, other):
        return self.size <= other.size

    def __ge__(self, other):
        return self.size >= other.size

    def __gt__(self, other):
        return self.size > other.size

    def __eq__(self, other):
        return self.size == other.size

    def __ne__(self, other):
        return self.size != other.size

    @property
    def size(self):
        """Retrieves the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square

        Args:
            value (:obj:`int`): The size of the square to be set
        """
        if type(value) != int:
            print("size must be an integer", end="")
            raise TypeError
        else:
            self.__size = value
        if value < 0:
            print("size must be >= 0", end="")
            raise ValueError

    def area(self):
        """Returns the area of the square.
        """
        return self.__size * self.__size
