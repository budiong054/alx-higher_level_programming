#!/usr/bin/python3

def remove_char_at(str, n):
    count = 0
    new_str = ""
    for char in str:
        if count == n:
            count += 1
            continue
        new_str += char
        count += 1
    return new_str
