#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """My Print_list_integer function prints all integers of a list

    Args:
        my_list: a list

    Returns:
        The return value is None
    """
    for integer in my_list:
        print("{:d}".format(integer))
