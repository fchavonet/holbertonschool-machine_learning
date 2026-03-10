#!/usr/bin/env python3

"""
Module that defines matrix_transpose function.
"""


def matrix_transpose(matrix):
    """
    Returns the transpose of a 2D matrix.
    """

    transpose = []

    for i in range(len(matrix[0])):
        new_row = []

        for j in range(len(matrix)):
            new_row.append(matrix[j][i])

        transpose.append(new_row)

    return transpose
