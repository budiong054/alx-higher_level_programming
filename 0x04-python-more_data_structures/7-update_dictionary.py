#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """update_dictionary - replaces or adds key/value in a dictionary

    Args:
        a_dictionary: The dictionary
        key: The key
        value: The value

    Returns:
        The updated dictionary
    """
    a_dictionary[key] = value
    return a_dictionary
