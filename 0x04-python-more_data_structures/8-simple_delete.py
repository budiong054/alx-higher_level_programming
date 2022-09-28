#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """simple_delete - deletes a keys in a dictionary

    Args:
        a_dictionary: The dictionary
        key: The key to be deleted

    Returns:
        The updated dictionary
    """
    if key in a_dictionary.keys():
        del a_dictionary[key]
    return a_dictionary
