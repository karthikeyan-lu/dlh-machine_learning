#!/usr/bin/env python3
"""The Whole Barn"""


def add_matrices(mat1, mat2):
    """
    Adds two matrices recursively.

    Args:
        mat1: first matrix
        mat2: second matrix

    Returns:
        A new matrix containing the sum,
        or None if shapes are different.
    """

    # Check if shapes match
    if type(mat1) != type(mat2):
        return None

    # Base case: numbers
    if isinstance(mat1, (int, float)):
        return mat1 + mat2

    # Check same length
    if len(mat1) != len(mat2):
        return None

    result = []

    for i in range(len(mat1)):
        added = add_matrices(mat1[i], mat2[i])

        if added is None:
            return None

        result.append(added)

    return result
