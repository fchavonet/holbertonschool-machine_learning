#!/usr/bin/env python3

"""
Module for adding two matrices of any dimension.
"""


def add_matrices(mat1, mat2):
    """
    Add two matrices of any dimension.

    Args:
        mat1: the first matrix, a list of lists of numbers.
        mat2: the second matrix, a list of lists of numbers.

    Returns:
        A new matrix representing the element-wise sum of mat1 and mat2,
        or None if the matrices do not have the same shape.
    """
    # Check if both matrices are lists (for recursive structure).
    if isinstance(mat1, list) and isinstance(mat2, list):
        # If lengths are different, return None
        if len(mat1) != len(mat2):
            return None

        # Recursively call add_matrices on each element.
        result = []
        for sub_mat1, sub_mat2 in zip(mat1, mat2):
            added = add_matrices(sub_mat1, sub_mat2)
            if added is None:
                return None
            result.append(added)
        return result
    else:
        # If elements are not lists, just add them.
        return mat1 + mat2
