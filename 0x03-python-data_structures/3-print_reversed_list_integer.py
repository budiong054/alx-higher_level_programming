#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """print_reversed_list_integer - prints all integers of a list
        , in reverse order

    Args:
        my_list: a list

    Returns:
        None
    """
    my_list.reverse()
    for integer in my_list:
        print("{:d}".format(integer))
