#!/usr/bin/env python3
"""Squashed Like Sardines"""


def cat_matrices(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis.

    Args:
        mat1: first matrix
        mat2: second matrix
        axis: axis along which to concatenate

    Returns:
        A new concatenated matrix, or None if not possible.
    """

    if axis == 0:
        return mat1 + mat2

    if len(mat1) != len(mat2):
        return None

    result = []

    for i in range(len(mat1)):
        cat = cat_matrices(mat1[i], mat2[i], axis - 1)

        if cat is None:
            return None

        result.append(cat)

    return result
