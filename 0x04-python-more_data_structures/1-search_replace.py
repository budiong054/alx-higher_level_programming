#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """search_replace - replaces all occurences of an element
        by another in a new list

       Args:
            my_list: the initial list
            search: the element to replace in the list
            replace: the new element

        Returns:
            The new list
    """
    if my_list is None:
        return
    new_list = []
    for i in my_list:
        if i == search:
            i = replace
        new_list.append(i)
    return new_list
