#!/usr/bin/python3
"""The ``base`` module

The module ontains one class ``Base``
"""


class Base:
    """This base class manages the ``id`` attribute
        in all future subclasses

    Args:
        __nb_objects(:obj:`int`): number of object
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize all instance attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
