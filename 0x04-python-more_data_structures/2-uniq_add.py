#!/usr/bin/python3
def uniq_add(my_list=[]):
    """uniq_add - adds all unique integers in a list

    Args:
        my_list: list

    Returns:
        The result of the addition
    """
    result = 0
    if my_list is None:
        return result
    for num in set(my_list):
        result += num
    return result
