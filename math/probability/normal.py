#!/usr/bin/env python3
"""Module that defines a Normal distribution class."""


class Normal:
    """Represents a normal distribution."""

    e = 2.7182818285
    pi = 3.1415926536

    def __init__(self, data=None, mean=0., stddev=1.):
        """Initialize a Normal distribution."""

        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")

            self.mean = float(mean)
            self.stddev = float(stddev)

        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")

            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            self.mean = float(sum(data) / len(data))

            variance = 0
            for x in data:
                variance += (x - self.mean) ** 2

            variance /= len(data)
            self.stddev = variance ** 0.5

    def z_score(self, x):
        """Calculate the z-score of a given x-value.

        Args:
            x: The x-value to normalize.

        Returns:
            The z-score of x.
        """

        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Calculate the x-value of a given z-score.

        Args:
            z: The z-score to convert.

        Returns:
            The x-value that corresponds to z.
        """

        return self.mean + (z * self.stddev)

    def pdf(self, x):
        """Calculate the PDF value for a given x-value.

        Args:
            x: The x-value.

        Returns:
            The PDF value at x.
        """

        exponent = -((x - self.mean) ** 2) / (2 * (self.stddev ** 2))

        return (1 / (self.stddev * ((2 * self.pi) ** 0.5))) * (
            self.e ** exponent
        )

    def cdf(self, x):
        """Calculate the CDF value for a given x-value.

        Args:
            x: The x-value.

        Returns:
            The CDF value at x.
        """

        z = (x - self.mean) / (self.stddev * (2 ** 0.5))

        erf = (2 / (self.pi ** 0.5)) * (
            z
            - ((z ** 3) / 3)
            + ((z ** 5) / 10)
            - ((z ** 7) / 42)
            + ((z ** 9) / 216)
        )

        return 0.5 * (1 + erf)
