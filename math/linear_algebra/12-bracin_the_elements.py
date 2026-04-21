#!/usr/bin/env python3

"""
Module that performs element-wise operations.
"""


def np_elementwise(mat1, mat2):
    """
    Returns element-wise addition, subtraction, multiplication, and division.
    """

    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
