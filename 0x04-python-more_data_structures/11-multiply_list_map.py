#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """multiply_list_map - returns a list with all values
       multiplied by a number

    Args:
        my_list: A list
        number: number to be multiplied with

    Returns:
        The new_list
    """
    new_list = list(map(lambda x: x * number, my_list))
    return new_list
