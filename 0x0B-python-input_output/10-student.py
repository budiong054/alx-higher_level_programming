#!/usr/bin/python3
"""The ``10-student`` module

This module contains a ``Student`` class
"""


class Student:
    """This is a students class
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionaru representation of a
            `Student` instance
        """
        if attrs is not None:
            new_dict = dict()
            for key in attrs:
                if self.__dict__.get(key) is not None:
                    new_dict[key] = self.__dict__.get(key)
            return new_dict
        else:
            return self.__dict__
