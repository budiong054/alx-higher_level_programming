#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """print_reversed_list_integer - prints all integers of a list
        , in reverse order

    Args:
        my_list: a list

    Returns:
        None
    """
    if my_list is None:
        return
    list_len = len(my_list)
    for i in range(1, list_len + 1):
        print("{:d}".format(my_list[list_len - i]))
