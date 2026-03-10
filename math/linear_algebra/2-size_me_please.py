#!/usr/bin/env python3

"""
Module that defines matrix_shape function.
"""


def matrix_shape(matrix):
    """
    Calculates the shape of a matrix.
    """

    shape = []

    while isinstance(matrix, list):
        shape.append(len(matrix))

        if len(matrix) == 0:
            break

        matrix = matrix[0]

    return shape
