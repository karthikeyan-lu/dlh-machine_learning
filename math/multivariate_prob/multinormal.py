#!/usr/bin/env python3
"""Multivariate Normal Distribution"""

import numpy as np


class MultiNormal:
    """Represents a Multivariate Normal distribution."""

    def __init__(self, data):
        """
        Class constructor.

        Args:
            data: numpy.ndarray of shape (d, n)

        Sets:
            mean: (d, 1) mean vector
            cov: (d, d) covariance matrix
        """

        # Check if data is a numpy array
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        d, n = data.shape

        # Must contain at least two data points
        if n < 2:
            raise ValueError("data must contain multiple data points")

        # Mean vector
        self.mean = np.mean(data, axis=1, keepdims=True)

        # Center the data
        centered = data - self.mean

        # Covariance matrix
        self.cov = (centered @ centered.T) / (n - 1)
