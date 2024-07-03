#!/usr/bin/env python3

"""
Module for concatenating two matrices along a specific axis.
"""


def cat_matrices(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis.

    Args:
        mat1: the first matrix, a list of lists of ints/floats.
        mat2: the second matrix, a list of lists of ints/floats.
        axis: the axis along which the matrices should be concatenated.

    Returns:
        A new matrix that is the result of concatenating mat1 and mat2 along
        the specified axis,vor None if the matrices cannot be concatenated.
    """
    # Handle 1-dimensional cases.
    if isinstance(mat1[0], (int, float)) and isinstance(mat2[0], (int, float)):
        return mat1 + mat2

    if axis == 0:
        # Concatenate along axis 0 (rows).
        if all(len(row) == len(mat1[0]) for row in mat2):
            return mat1 + mat2
        else:
            return None
    elif axis == 1:
        # Concatenate along axis 1 (columns).
        if len(mat1) == len(mat2):
            return [row1 + row2 for row1, row2 in zip(mat1, mat2)]
        else:
            return None
    else:
        # Recursively concatenate along higher dimensions.
        if isinstance(mat1, list) and isinstance(mat2, list):
            if len(mat1) != len(mat2):
                return None
            concatenated = []
            for sub1, sub2 in zip(mat1, mat2):
                result = cat_matrices(sub1, sub2, axis - 1)
                if result is None:
                    return None
                concatenated.append(result)
            return concatenated
        else:
            return None
