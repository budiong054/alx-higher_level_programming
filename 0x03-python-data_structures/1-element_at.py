#!/usr/bin/python3
def element_at(my_list, idx):
    """My Element_at function retrieves an element
    from a list

    Args:
        my_list: a list
        idx: index of element in a list

    Returns:
        The element at a particular index or None if its fails
    """
    if idx < 0:
        return None
    if idx > len(my_list) - 1:
        return None
    return my_list[idx]
