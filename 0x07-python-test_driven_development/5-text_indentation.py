#!/usr/bin/python3
"""The ``5-text_indentation`` module

This module contains one function ``text_indentation()``
"""


def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        for i in range(len(text)):
            if text[i] in [' ', '\t'] and text[i - 1] in ['.', '?', ':']:
                continue
            elif text[i] == '\t':
                continue
            elif text[i] in ['.', '?', ':']:
                print("{}".format(text[i]))
                print()
            else:
                print("{}".format(text[i]), end="")
