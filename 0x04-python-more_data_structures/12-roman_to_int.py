#!/usr/bin/python3
def check_roman(char):
    """check_roman - checks the char an returns the integer
        equivalent
    """
    if char == 'I':
        return 1
    elif char == 'V':
        return 5
    elif char == 'X':
        return 10
    elif char == 'L':
        return 50
    elif char == 'C':
        return 100
    elif char == 'D':
        return 500
    elif char == 'M':
        return 1000
    else:
        return


def check_double_roman(char):
    """checks if the char passed is I, X or C

    Returns:
        it returns 1 if it's 'I', 2 if it's 'X',
        3 if it's 'C' and 0 otherwise
    """
    if char == 'I':
        return 1
    elif char == 'X':
        return 2
    elif char == 'C':
        return 3
    else:
        return 0


def check_next_roman(char, flag):
    """checks the next char if it is (V or X) or
        (L or C) or (D or M)

    Returns:
        -2 if it's (V or X), -20 if it is (L or C),
        -200 if it's (D or M) otherwise 0
    """
    if (char == 'X' or char == 'V') and flag == 1:
        return -2
    elif (char == 'L' or char == 'C') and flag == 2:
        return -20
    elif (char == 'D' or char == 'M') and flag == 3:
        return -200
    else:
        return 0


def roman_to_int(roman_string):
    """roman_to_int - converts a Roman numeral to an integer

    Args:
        roman_string: Roman numeral

    Returns:
        The arabic equivalent
    """
    if type(roman_string) != str:
        return 0
    flag = 0
    arabic_num = 0
    for char in roman_string:
        if check_roman(char) is None:
            return 0
        if check_double_roman(char) != 0 and flag == 0:
            arabic_num += check_roman(char)
            flag = check_double_roman(char)
            continue
        arabic_num += check_roman(char) + check_next_roman(char, flag)
        flag = 0

    return arabic_num
