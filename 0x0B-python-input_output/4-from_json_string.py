#!/usr/bin/python3
"""The ``4-from_json_string`` module

The module contains one function ``from_json_string``
"""
import json


def from_json_string(my_str):
    """Returns an object (Python data structure) represented
        by a JSON string
    """
    return json.loads(my_str)
