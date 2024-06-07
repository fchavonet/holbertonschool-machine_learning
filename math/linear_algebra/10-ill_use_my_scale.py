#!/usr/bin/env python3

import numpy as np

"""
Module to calculate the shape of a numpy.ndarray
"""


def np_shape(matrix):
    """
    Calculate the shape of a numpy.ndarray.

    Parameters:
        matrix (numpy.ndarray): the input matrix.

    Returns:
        tuple: a tuple of integers representing the shape of the matrix.
    """
    return matrix.shape
