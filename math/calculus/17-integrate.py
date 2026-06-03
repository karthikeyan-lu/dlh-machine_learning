#!/usr/bin/env python3
"""Module for polynomial integration"""


def poly_integral(poly, C=0):
    """Calculates the integral of a polynomial"""

    if not isinstance(poly, list) or len(poly) == 0:
        return None

    if not isinstance(C, int):
        return None

    for item in poly:
        if not isinstance(item, (int, float)):
            return None

    integral = [C]

    for power in range(len(poly)):
        value = poly[power] / (power + 1)

        if value == int(value):
            value = int(value)

        integral.append(value)

    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()

    return integral
