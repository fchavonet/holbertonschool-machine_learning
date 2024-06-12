#!/usr/bin/env python3

"""
Module for performing matrix multiplication using NumPy.
"""

import numpy as np


def np_matmul(mat1, mat2):
    """
    Performs matrix multiplication on two numpy.ndarrays.

    Args:
        mat1 (numpy.ndarray): the first matrix.
        mat2 (numpy.ndarray): the second matrix.

    Returns:
        numpy.ndarray: the result of the matrix multiplication.
    """
    return np.matmul(mat1, mat2)
