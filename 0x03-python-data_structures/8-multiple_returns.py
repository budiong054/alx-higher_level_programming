#!/usr/bin/python3
def multiple_returns(sentence):
    """multiple_returns: returns a tuple with the length of a
        string and its first character

    Args:
        sentence: The string

    Returns:
        The length of a string and its first character or None if the
        sentence is empty
    """
    if len(sentence) == 0:
        new_tuple = (len(sentence), None)
        return new_tuple
    new_tuple = (len(sentence), sentence[0])
    return new_tuple
