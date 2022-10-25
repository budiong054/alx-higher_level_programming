#!/usr/bin/python3
"""The ``3-to_json_string`` module

The module contains one function ``to_json_string``
"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)
    """
    return json.dumps(my_obj)
