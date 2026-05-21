#!/usr/bin/env python3
"""The Whole Barn"""


def add_matrices(mat1, mat2):
    """Adds two matrices recursively."""
    if type(mat1) is not type(mat2):
        return None

    if isinstance(mat1, (int, float)):
        return mat1 + mat2

    if len(mat1) != len(mat2):
        return None

    result = []

    for i in range(len(mat1)):
        added = add_matrices(mat1[i], mat2[i])

        if added is None:
            return None

        result.append(added)

    return result
