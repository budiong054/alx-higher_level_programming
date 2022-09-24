#!/usr/bin/python3
def max_integer(my_list=[]):
    """max_integer: finds the biggest integer of a list

    Args:
        my_list: a list

    Returns:
        The biggest integer of a list
    """
    if len(my_list) == 0:
        return None

    max_num = my_list[0]
    for i in range(len(my_list)):
        if max_num < my_list[i]:
            max_num = my_list[i]

    return max_num
