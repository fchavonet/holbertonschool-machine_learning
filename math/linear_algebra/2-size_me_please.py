#!/usr/bin/env python3

"""
Module to calculate the shape of a matrix (or nested list).
"""


def matrix_shape(matrix):
    """
    Calculates the shape of a matrix (nested list).

    Args:
        matrix (list): a nested list whose shape is to be determined.

    Returns:
        list: a list of integers representing the size of each dimension.
    """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
