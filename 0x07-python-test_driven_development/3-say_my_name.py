#!/usr/bin/python3
"""
This is the "3-say_my_name" module.

The 3-say_my_name module supplies one function, say_my_name().
"""


def say_my_name(first_name, last_name=""):
    """This function prints ``My name is <first name> <last name>

    Args:
        first_name(:string:): Input first name
        last_name(:string:): Input last name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")
