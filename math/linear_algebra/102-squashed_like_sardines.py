#!/usr/bin/env python3
"""Squashed Like Sardines"""


def matrix_shape(matrix):
    """Returns the shape of a matrix."""
    shape = []

    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]

    return shape


def cat_matrices(mat1, mat2, axis=0):
    """Concatenates two matrices along a specific axis."""
    shape1 = matrix_shape(mat1)
    shape2 = matrix_shape(mat2)

    if len(shape1) != len(shape2):
        return None

    for i in range(len(shape1)):
        if i != axis and shape1[i] != shape2[i]:
            return None

    if axis == 0:
        return mat1 + mat2

    result = []

    for i in range(len(mat1)):
        result.append(cat_matrices(mat1[i], mat2[i], axis - 1))

    return result
