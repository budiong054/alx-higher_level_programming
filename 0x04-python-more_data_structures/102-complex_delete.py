#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """complex_delete - deletes keys with a specific
        value in a dictionary

    Args:
        a_dictionary: The dictionary
        value: The values to which the keys will
            be deleted

    Returns:
        The updated dictionary
    """
    del_list = []
    for key, val in a_dictionary.items():
        if val == value:
            del_list.append(key)

    for key in del_list:
        del a_dictionary[key]
    return a_dictionary
