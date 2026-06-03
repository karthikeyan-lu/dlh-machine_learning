#!/usr/bin/env python3
"""Module for polynomial derivatives"""


def poly_derivative(poly):
    """Calculates the derivative of a polynomial"""

    if not isinstance(poly, list) or len(poly) == 0:
        return None

    for item in poly:
        if not isinstance(item, (int, float)):
            return None

    if len(poly) == 1:
        return [0]

    derivative = []

    for power in range(1, len(poly)):
        derivative.append(poly[power] * power)

    return derivative
