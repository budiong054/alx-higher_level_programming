#!/usr/bin/python3
import math
"""This modules contains a MagicClass
"""


class MagicClass:
    """magicClass calculates the area and the circumference of a circle"""
    def __init__(self, radius):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculate the area of the circle"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Calculate the circumference of the circle"""
        return (2 * math.pi * self.__radius)