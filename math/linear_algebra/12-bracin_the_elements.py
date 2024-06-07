#!/usr/bin/env python3

"""
Module to perform element-wise operations on matrices using NumPy.
"""


def np_elementwise(mat1, mat2):
    """
    Element-wise operations on two matrices using NumPy.

    Parameters:
        mat1 (numpy.ndarray): first matrix.
        mat2 (numpy.ndarray or scalar): second matrix or scalar.

    Returns:
        tuple: a tuple containing the element-wise result of the operation.
    """
    addition = mat1 + mat2
    subtraction = mat1 - mat2
    multiplication = mat1 * mat2
    division = mat1 / mat2

    return addition, subtraction, multiplication, division
