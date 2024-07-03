#!/usr/bin/env python3

"""
Module for slicing a numpy array along specified axes.
"""

import numpy as np


def np_slice(matrix, axes={}):
    """
    Slices a numpy array along specified axes.

    Parameters:
        matrix (numpy.ndarray): the matrix to be sliced.
        axes (dict): dict with axis as key and slice tuple as value.

    Returns:
        numpy.ndarray: a new sliced numpy array.
    """
    # Create a slice object for each dimension of the matrix
    slices = [slice(None)] * matrix.ndim

    # Update the slice object for each axis specified in the axes dictionary
    for axis, slice_tuple in axes.items():
        slices[axis] = slice(*slice_tuple)

    # Use tuple of slice objects to slice the matrix
    return matrix[tuple(slices)]
