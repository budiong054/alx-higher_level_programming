#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """new_in_list: replaces an element in a list at a specific position
        without modifying the original list

    Args:
        my_list: a list
        idx: index of element to replace
        element: element to be replace

    Returns:
        The new list on success otherwise return the original list
    """
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
