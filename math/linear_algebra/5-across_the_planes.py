#!/usr/bin/env python3

"""
Module that defines add_matrices2D function.
"""


def add_matrices2D(mat1, mat2):
    """
    Adds two 2D matrices element-wise.
    """

    if len(mat1) != len(mat2):
        return None

    new_matrix = []

    for i in range(len(mat1)):
        if len(mat1[i]) != len(mat2[i]):
            return None

        new_row = []

        for j in range(len(mat1[i])):
            new_row.append(mat1[i][j] + mat2[i][j])

        new_matrix.append(new_row)

    return new_matrix
