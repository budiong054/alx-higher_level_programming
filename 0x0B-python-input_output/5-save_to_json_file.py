#!/usr/bin/python3
"""The ``5-save_to_json_file`` module

The module contains one function ``save_to_json_file``
"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file, using a JSON representation
    """
    with open(filename, mode='w', encoding='utf-8') as a_file:
        a_file.write(json.dumps(my_obj))
