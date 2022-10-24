#!/usr/bin/python3
"""The ``8-rectangle`` module

The module contains one class ``Rectangle``
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class inherits from `BaseGeometry`
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
