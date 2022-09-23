#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """replace_in_list - replaces an element of a list at a specific position

    Args:
        my_list: a list
        idx: index of the element to be replaced
        element: new element

    Returns:
        The new list or the original list if its fails
    """
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    my_list[idx] = element
    return my_list
