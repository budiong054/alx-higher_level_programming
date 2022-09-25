#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """add_tuple: adds two tuples together

    Args:
        tuple_a: first tuple
        tuple_b: second tuple

    Returns:
        The result of the addition as a tuple
    """

    tuple_list = []
    i = 0
    while i < 2:
        if i > len(tuple_a) - 1:
            a = 0
        else:
            a = tuple_a[i]

        if i > len(tuple_b) - 1:
            b = 0
        else:
            b = tuple_b[i]
        tuple_list.append(a + b)
        i += 1

    return tuple(tuple_list)
