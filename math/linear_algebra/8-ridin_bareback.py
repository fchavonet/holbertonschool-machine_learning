#!/usr/bin/env python3

"""
Module to perform matrix multiplication.
"""


def mat_mul(mat1, mat2):
    """
    Performs matrix multiplication.

    Parameters:
        mat1 (list of list of int/float): the first matrix.
        mat2 (list of list of int/float): the second matrix.

    Returns:
        list: a new matrix with the product of the input matrices.
        None: if the matrices cannot be multiplied.
    """
    if len(mat1[0]) != len(mat2):
        return None

    result = []

    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            element = 0
            for k in range(len(mat2)):
                element += mat1[i][k] * mat2[k][j]
            row.append(element)
        result.append(row)

    return result
