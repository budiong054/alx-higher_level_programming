#!/usr/bin/python3
def best_score(a_dictionary):
    """best_score - returns a key with the biggest integer value

    Args:
        a_dictionary: The dictionary

    Returns:
        The key with the biggest integer
    """
    max_score = 0
    max_key = ""
    if a_dictionary is None or not len(a_dictionary):
        return
    for key in a_dictionary:
        if a_dictionary.get(key) > max_score:
            max_score = a_dictionary.get(key)
            max_key = key
    return max_key
