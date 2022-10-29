#!/usr/bin/python3
"""The ``base`` module

The module ontains one class ``Base``
"""
import json


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

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of `list_objs` to a
            file

        Args:
            list_objs(:obj:`list`): list of instances who inherits of `Base`
        """
        if list_objs is None:
            list_dict = []
        else:
            list_dict = []
            for instance in list_objs:
                list_dict.append(instance.to_dictionary())
        with open(f'{cls.__name__}.json', mode='w', encoding='utf-8')\
                as a_file:
            a_file.write(cls.to_json_string(list_dict))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attribute already set
        """
        if cls.__name__ == 'Rectangle':
            r = cls(1, 1)
            r.update(**dictionary)
            return r
        else:
            s = cls(1)
            s.update(**dictionary)
            return s

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances
        """
        try:
            a_file = open(f'{cls.__name__}.json', mode='r', encoding='utf-8')
        except FileNotFoundError:
            return list()
        else:
            json_string = a_file.read()
            a_file.close()
            list_dict = cls.from_json_string(json_string)
            list_instance = list()
            for i in list_dict:
                list_instance.append(cls.create(**i))
            return list_instance

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of
            `list_dictionaries`

        Args:
            list_dictionaries(:obj:`list`): list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation
            `json_string`

        Args:
            json_string(:obj:`str`): is a string representing a list
                of dictionaries
        """
        if json_string is None or len(json_string) == 0:
            return list()
        return json.loads(json_string)
