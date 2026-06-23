#!/usr/bin/env python3
"""Posterior probability"""

import numpy as np


def posterior(x, n, P, Pr):
    """Calculate the posterior probability.

    Args:
        x: Number of patients with severe side effects.
        n: Total number of patients observed.
        P: Hypothetical probabilities.
        Pr: Prior beliefs about P.

    Returns:
        The posterior probability for each value in P.
    """

    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    if not isinstance(x, int) or x < 0:
        raise ValueError(
            "x must be an integer that is greater than or equal to 0"
        )

    if x > n:
        raise ValueError("x cannot be greater than n")

    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")

    if not isinstance(Pr, np.ndarray) or Pr.shape != P.shape:
        raise TypeError(
            "Pr must be a numpy.ndarray with the same shape as P"
        )

    if np.any(P < 0) or np.any(P > 1):
        raise ValueError("All values in P must be in the range [0, 1]")

    if np.any(Pr < 0) or np.any(Pr > 1):
        raise ValueError("All values in Pr must be in the range [0, 1]")

    if not np.isclose(np.sum(Pr), 1):
        raise ValueError("Pr must sum to 1")

    k = min(x, n - x)

    numerator = np.prod(np.arange(n - k + 1, n + 1, dtype=float))
    denominator = np.prod(np.arange(1, k + 1, dtype=float))
    combination = numerator / denominator

    likelihood = combination * (P ** x) * ((1 - P) ** (n - x))

    intersection = likelihood * Pr

    marginal = np.sum(intersection)

    return intersection / marginal
