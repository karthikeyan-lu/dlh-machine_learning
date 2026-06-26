#!/usr/bin/env python3
"""Mean and Covariance"""

import numpy as np


def mean_cov(X):
    """
    Calculates the mean and covariance of a data set.

    Args:
        X: numpy.ndarray of shape (n, d)

    Returns:
        mean: numpy.ndarray of shape (1, d)
        cov: numpy.ndarray of shape (d, d)
    """

    # Check if X is a 2D numpy array
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        raise TypeError("X must be a 2D numpy.ndarray")

    n = X.shape[0]

    # Must contain at least two data points
    if n < 2:
        raise ValueError("X must contain multiple data points")

    # Calculate mean
    mean = np.mean(X, axis=0, keepdims=True)

    # Center the data
    X_centered = X - mean

    # Calculate covariance
    cov = (X_centered.T @ X_centered) / (n - 1)

    return mean, cov
