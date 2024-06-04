#!/usr/bin/env python3

"""
Module to concatenate two 2D matrices along a specific axis.
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenates two 2D matrices along a specified axis.

    Parameters:
        mat1 (list of lists of int/float): the first matrix.
        mat2 (list of lists of int/float): the second matrix.
        axis (int): the axis along which to concatenate the matrices.

    Returns:
        list of lists: a new matrix resulting from concatenating mat1 and mat2.
        None: if the matrices cannot be concatenated along the specified axis.
    """
    # Check if the concatenation is along the rows (axis 0).
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        return mat1 + mat2
    # Check if the concatenation is along the columns (axis 1).
    elif axis == 1:
        if len(mat1) != len(mat2):
            return None
        return [row1 + row2 for row1, row2 in zip(mat1, mat2)]
    # Return None for an invalid axis.
    else:
        return None
