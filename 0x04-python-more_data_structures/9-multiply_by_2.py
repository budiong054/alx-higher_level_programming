#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """multiply_by_2 - returns a new dictionary with all
        values multiplied by 2

    Args:
        a_dictionary: The dictionary

    Returns:
        a new dictionary
    """
    new_dict = {}
    values = list(map(lambda x: x * 2, a_dictionary.values()))
    i = 0
    for key in a_dictionary.keys():
        new_dict[key] = values[i]
        i += 1
    return new_dict
