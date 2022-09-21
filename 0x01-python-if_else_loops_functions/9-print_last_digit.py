#!/usr/bin/python3
def print_last_digit(number):
    last_digit = number % 10
    if (number < 0) and (last_digit != 0):
        last_digit -= 10
    return last_digit
