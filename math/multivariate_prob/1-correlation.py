#!/usr/bin/env python3
"""Correlation Matrix"""

import numpy as np


def correlation(C):
    """
    Calculates a correlation matrix.

    Args:
        C: numpy.ndarray of shape (d, d)
           containing a covariance matrix.

    Returns:
        Correlation matrix.
    """

    # Check if C is a numpy array
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")

    # Check if C is a square matrix
    if C.ndim != 2 or C.shape[0] != C.shape[1]:
        raise ValueError("C must be a 2D square matrix")

    # Standard deviations
    std = np.sqrt(np.diag(C))

    # Outer product of standard deviations
    std_matrix = np.outer(std, std)

    # Correlation matrix
    corr = C / std_matrix

    return corr
