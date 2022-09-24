#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """divisible_by_2: finds all multiples of 2 in a list

    Args:
        my_list: a list

    Returns:
        The new list with True or False
    """
    new_list = []
    for num in my_list:
        if num % 2:
            new_list.append(False)
        else:
            new_list.append(True)
    return new_list
