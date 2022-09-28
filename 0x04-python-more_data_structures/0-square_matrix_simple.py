#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """square_matrix_simple - computes the square value of
        all integers of a matrix

    Args:
        matrix: The matrix

    Returns:
        A new matrix
    """
    new_matrix = []
    for num in matrix:
        c = list(map(lambda x: x * x, num))
        new_matrix.append(c)
    return new_matrix
