#!/usr/bin/python3
"""The ``rectangle`` module

The module contains one class ``Rectangle``
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class inherits from ``Base`` class and
        contains all the methods for rectangles
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize all the instances attribute

        Args:
            width(:obj:`int`): The width of the rectangle
            height(:obj:`int`): The height of the rectangle
            x(:obj:`int`): The x - coordinate
            y(:obj:`int`): The y - coordinate
        """
        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """Return the string format overriding the default `__str__`
            method
        """
        return f"[Rectangle] ({self.id:d}) {self.x:d}/{self.y:d}"\
                f" - {self.width:d}/{self.height:d}"

    @property
    def width(self):
        """Retrieve the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Retrieve the x-coordinate of the rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x-coordinate of the rectangle
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Retrieve the y-coordinate of the rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y-coordinate of the rectangle
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Return the area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """Prints in stdout the `Rectangle` instance with
            the character `#`
        """
        for i in range(self.y):
            print()
        for row in range(self.height):
            print("{}{}".format(self.x * " ", self.width * '#'))

    def update(self, *args, **kwargs):
        """Update an argument to each attribute
        """
        for index, arg in enumerate(args):
            if index == 0:
                self.id = arg
            elif index == 1:
                self.width = arg
            elif index == 2:
                self.height = arg
            elif index == 3:
                self.x = arg
            elif index == 4:
                self.y = arg
            else:
                break

        if len(args) == 0:
            args_tuple = ("id", "width", "height", "x", "y")
            for key, value in kwargs.items():
                if key in args_tuple:
                    if key == "id":
                        self.id = value
                    elif key == "width":
                        self.width = value
                    elif key == "height":
                        self.height = value
                    elif key == "x":
                        self.x = value
                    else:
                        self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a `Rectangle`
        """
        attr_dict = dict()
        attr_dict['x'] = self.x
        attr_dict['y'] = self.y
        attr_dict['id'] = self.id
        attr_dict['height'] = self.height
        attr_dict['width'] = self.width
        return attr_dict
