#!/usr/bin/env python3

"""
Module to transpose a 2D matrix.
"""


def matrix_transpose(matrix):
    """
    Transpose a 2D matrix.

    Args:
        matrix (list of list): the input matrix.

    Returns:
        list of list: the transposed matrix.
    """
    # Get the number of rows and columns in the matrix.
    rows = len(matrix)
    cols = len(matrix[0])

    # Initialize an empty matrix to store the transposed matrix.
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    # Iterate through the original matrix and populate the transposed matrix.
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed
