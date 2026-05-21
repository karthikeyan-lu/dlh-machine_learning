#!/usr/bin/env python3
"""Slice Like A Ninja"""


def np_slice(matrix, axes={}):
    """
    Slices a numpy.ndarray along specific axes.

    Args:
        matrix: numpy.ndarray to slice
        axes: dictionary where:
              key = axis index
              value = tuple representing slice arguments

    Returns:
        A new sliced numpy.ndarray
    """

    slices = []

    for i in range(matrix.ndim):
        if i in axes:
            slices.append(slice(*axes[i]))
        else:
            slices.append(slice(None))

    return matrix[tuple(slices)]
