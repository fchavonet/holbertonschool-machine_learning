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

    for row in range(len(mat1)):
        new_row = []
        for col in range(len(mat1[row])):
            new_row.append(mat1[row][col] + mat2[row][col])
        new_mat.append(new_row)

    return new_mat
