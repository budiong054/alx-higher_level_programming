#!/usr/bin/python3
"""This modules contains a Square class
"""


class Square:
    """Square defines a private instance attribute `size`.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
            size (:obj:`int`): The size of the square.
            position (:obj:`tuple`): The coordinate of the square.
        """
        if type(size) != int:
            print("size must be an integer", end="")
            raise TypeError
        else:
            self.__size = size
        if size < 0:
            print("size must be >= 0", end="")
            raise ValueError

        if type(position) != tuple or len(position) != 2 or\
                position[0] < 0 or position[1] < 0 or\
                type(position[0]) is not int or type(position[1]) is not int:
            print("position must be a tuple of 2 positive integers", end="")
            raise TypeError
        else:
            self.__position = position

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

    @property
    def position(self):
        """Retrives the position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the postion of the square attribute

        Args:
            value (:obj:`tuple`): The position coordinate of the square
        """
        if type(value) != tuple or len(value) != 2 or\
                value[0] < 0 or value[1] < 0 or type(value[0]) is not int or\
                type(value[1]) is not int:
            print("position must be a tuple of 2 positive integers", end="")
            raise TypeError
        else:
            self.__position = position

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
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(f'{self.__position[0] * " "}{self.__size * "#"}')
