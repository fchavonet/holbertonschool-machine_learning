#!/usr/bin/env python3

"""
Module that concatenates two 2D matrices.
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a given axis.
    """

    # Check if axis is valid.
    if axis not in [0, 1]:
        return None

    # Axis 0 → vertical concatenation (add rows).
    if axis == 0:
        # Check if number of columns match
        if len(mat1[0]) != len(mat2[0]):
            return None

        # Return a new matrix (copy of rows)
        return [row[:] for row in mat1] + [row[:] for row in mat2]

    # Axis 1 → horizontal concatenation (add columns).
    if axis == 1:
        # Check if number of rows match.
        if len(mat1) != len(mat2):
            return None

        # Merge rows one by one.
        new_matrix = []

        for i in range(len(mat1)):
            new_matrix.append(mat1[i][:] + mat2[i][:])

        return new_matrix
