#!/usr/bin/python3
"""This is ``7-base_geometry`` module

This module contains one class `BaseGeometry`
"""


class BaseGeometry:
    """BaesGeometry class
    """
    def area(self):
        """Raise an Exception with the message `area() is not
            implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a value

        Args:
            name(:str:): The name associated with value
            value(:obj:`int`): The value to be validated
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
