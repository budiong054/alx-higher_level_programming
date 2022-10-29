#!/usr/bin/python3
"""The ``square`` module

This module contains one class ``Square`` that inherits
from ``Rectangle``
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The Square class inherit from the Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initializing the Square class
        
        Args:
            size(:obj:`int`): size of the square
            x(:obj:`int`): x - coordinate
            y(:obj;`int`): y - coordinate
            id(:obj:`int`): class id
        """ 
        Rectangle.__init__(self, size, size, x, y, id)

    def __str__(self):
        """Returns the string format
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Retrieve the size of the square
        """
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def update(self, *args, **kwargs):
        """Update an argument to each attribute
        """
        for index, arg in enumerate(args):
            if index == 0:
                self.id = arg
            elif index == 1:
                self.size = arg
            elif index == 2:
                self.x = arg
            elif index == 3:
                self.y = arg
            else:
                break

        if len(args) == 0:
            args_tuple = ("id", "size", "x", "y")
            for key, value in kwargs.items():
                if key in args_tuple:
                    if key == "id":
                        self.id = value
                    elif key == "size":
                        self.size = value
                    elif key == "x":
                        self.x = value
                    else:
                        self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a `Square`
        """
        attr_dict = dict()
        attr_dict['x'] = self.x
        attr_dict['y'] = self.y
        attr_dict['id'] = self.id
        attr_dict['size'] = self.size
        return attr_dict
