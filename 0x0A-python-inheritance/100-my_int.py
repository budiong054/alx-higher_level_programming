#!/usr/bin/python3
"""The ``100-my_int`` module

The module contains one class ``MyInt``
"""


class MyInt(int):
    """Inherits from `int` class
    """
    def __eq__(self, value):
        if MyInt(int.__ne__(self, value)):
            return True
        else:
            return False

    def __ne__(self, value):
        if MyInt(int.__eq__(self, value)):
            return True
        else:
            return False
