#!/usr/bin/python3
def no_c(my_string):
    """no_c: removes all characters c and C from string

    Args:
        my_string: the string

    Returns:
        The new string
    """
    for char in my_string:
        if char == 'c' or char == 'C':
            del char
    return my_string
