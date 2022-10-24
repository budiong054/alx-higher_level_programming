#!/usr/bin/python3
"""This is ``1-my_list`` module

This module contains a class ``MyList`` that inherits from ``list``
"""


class MyList(list):
    """MyList class inherits from the list class
    """
    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)
        """
        new_list = self.copy()
        new_list.sort()
        print(new_list)
