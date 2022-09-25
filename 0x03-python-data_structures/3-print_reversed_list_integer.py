#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """print_reversed_list_integer - prints all integers of a list
        , in reverse order

    Args:
        my_list: a list

    Returns:
        None
    """
    """#list_len = len(my_list)
    #for i in range(1, list_len + 1):
    #    print("{:d}".format(my_list[list_len - i]))
    """
    my_list.reverse()
    for num in my_list:
        print("{:d}".format(num))
