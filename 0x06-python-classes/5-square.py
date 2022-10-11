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

    def my_print(self):
        """Prints in stdout the square with the character `#`
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print(self.__size * "#")
