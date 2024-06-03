#!/usr/bin/env python3

"""
Module to add two 2D matrices element-wise.
"""


def add_matrices2D(mat1, mat2):
    """
    Adds two 2D matrices element-wise.

    Parameters:
        mat1 (list of list of int/float): the first matrix to add.
        mat2 (list of list of int/float): the second matrix to add.

    Returns:
        list of list: a new matrix with the element-wise sum.
        None: if the matrices are not the same shape.
    """
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None

    new_mat = []

    # Iterate over corresponding rows of mat1 and mat2 using zip
    for row1, row2 in zip(mat1, mat2):
        new_row = []
        # Iterate over corresponding elements of row1 and row2 using zip
        for x, y in zip(row1, row2):
            new_row.append(x + y)
        new_mat.append(new_row)

    return new_mat
