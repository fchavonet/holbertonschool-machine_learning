#!/usr/bin/env python3

"""
Module for concatenating arrays using NumPy.
"""

import numpy as np


def np_cat(mat1, mat2, axis=0):
    """
    Concatenates two NumPy arrays along a specified axis.

    Parameters:
        mat1 (numpy.ndarray): the first array to concatenate.
        mat2 (numpy.ndarray): the second array to concatenate.
        axis (int): the axis along which to concatenate the matrices.

    Returns:
        numpy.ndarray: The concatenated array.
    """
    return np.concatenate((mat1, mat2), axis)
