#!/usr/bin/env python3
"""Module that defines a Binomial distribution."""


class Binomial:
    """Represents a binomial distribution."""

    def __init__(self, data=None, n=1, p=0.5):
        """Initialize a Binomial distribution.

        Args:
            data: List of data to estimate the distribution.
            n: Number of Bernoulli trials.
            p: Probability of success.
        """

        if data is None:

            if n <= 0:
                raise ValueError(
                    "n must be a positive value"
                )

            if p <= 0 or p >= 1:
                raise ValueError(
                    "p must be greater than 0 and less than 1"
                )

            self.n = int(n)
            self.p = float(p)

        else:

            if not isinstance(data, list):
                raise TypeError(
                    "data must be a list"
                )

            if len(data) < 2:
                raise ValueError(
                    "data must contain multiple values"
                )

            mean = sum(data) / len(data)

            variance = sum(
                (x - mean) ** 2
                for x in data
            ) / len(data)

            p = 1 - (variance / mean)

            n = round(mean / p)

            p = mean / n

            self.n = int(n)
            self.p = float(p)

    def pmf(self, k):
        """Calculate the probability mass function.

        Args:
            k: Number of successes.

        Returns:
            The PMF value for k successes.
        """

        k = int(k)

        if k < 0 or k > self.n:
            return 0

        n_fact = 1
        for i in range(1, self.n + 1):
            n_fact *= i

        k_fact = 1
        for i in range(1, k + 1):
            k_fact *= i

        nk_fact = 1
        for i in range(1, self.n - k + 1):
            nk_fact *= i

        combination = n_fact / (k_fact * nk_fact)

        return (
            combination
            * (self.p ** k)
            * ((1 - self.p) ** (self.n - k))
        )

    def cdf(self, k):
        """Calculate the cumulative distribution function.

        Args:
            k: Number of successes.

        Returns:
            The probability of obtaining at most
            k successes.
        """

        k = int(k)

        if k < 0:
            return 0

        if k > self.n:
            k = self.n

        cdf = 0

        for i in range(k + 1):
            cdf += self.pmf(i)

        return cdf
