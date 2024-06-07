#!/usr/bin/env python3

"""
Module to transpose a matrix using NumPy.
"""


def np_transpose(matrix):
    """
    Transposes the given matrix using NumPy.

    Parameters:
        matrix (numpy.ndarray): the matrix to transpose.

    Returns:
        numpy.ndarray: the transposed matrix.
    """
    return matrix.transpose()
