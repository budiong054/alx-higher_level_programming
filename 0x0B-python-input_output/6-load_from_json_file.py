#!/usr/bin/python3
"""The ``6-load_from_json_file`` module

The module contains one function ``load_from_json_file``
"""
import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file
    """
    with open(filename, mode='r', encoding='utf-8') as a_file:
        py_string_object = a_file.read()
    return json.loads(py_string_object)
