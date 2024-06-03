#!/usr/bin/env python3

"""
Module to add two arrays element-wise.
"""


def add_arrays(arr1, arr2):
    """
    Adds two arrays element-wise.

    Parameters:
        arr1 (list of int/float): the first array to add.
        arr2 (list of int/float): the second array to add.

    Returns:
        list: a new array with the element-wise sum of the input arrays.
        None: if the input arrays are not the same shape.
    """
    if len(arr1) != len(arr2):
        return None

    new_list = []

    for i in range(len(arr1)):
        new_list.append(arr1[i] + arr2[i])

    return new_list
