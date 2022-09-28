#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """only_diff_elements - returns a set of all elements
        present in only one set

    Args:
        set_1: first set
        set_2: second set

    Returns:
        The set of all elements present in only one set
    """
    return set_1 ^ set_2
