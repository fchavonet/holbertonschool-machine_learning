#!/usr/bin/env python3

"""
Module that performs matrix multiplication.
"""


def mat_mul(mat1, mat2):
    """
    Multiplies two matrices.
    """

    # Number of columns in mat1 must equal number of rows in mat2.
    if len(mat1[0]) != len(mat2):
        return None

    # Result matrix initialization.
    result = []

    # Iterate over rows of mat1.
    for i in range(len(mat1)):
        new_row = []

        # Iterate over columns of mat2.
        for j in range(len(mat2[0])):
            sum_product = 0

            # Compute dot product.
            for k in range(len(mat1[0])):
                sum_product += mat1[i][k] * mat2[k][j]

            new_row.append(sum_product)

        result.append(new_row)

    return result
