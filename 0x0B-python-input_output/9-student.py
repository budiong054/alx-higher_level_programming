#!/usr/bin/python3
"""The ``9-student`` module

This module contains a ``Student`` class
"""


class Student:
    """This is a students class
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionaru representation of a
            `Student` instance
        """
        return self.__dict__
