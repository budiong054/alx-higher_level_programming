#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """print_sorted_dictionary - prints a dictionary by ordered keys

    Args:
        a_dictionary: dictionary

    Returns:
        None
    """
    for key, value in sorted(a_dictionary.items()):
        print("{}: {}".format(key, value))
