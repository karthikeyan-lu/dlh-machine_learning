#!/usr/bin/env python3
"""Module for calculating determinant of a matrix"""


def determinant(matrix):
    """Calculates the determinant of a matrix"""

    # Validate matrix type
    if (not isinstance(matrix, list) or
            len(matrix) == 0 or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    # Special case for 0x0 matrix
    if matrix == [[]]:
        return 1

    # Validate square matrix
    n = len(matrix)

    if not all(len(row) == n for row in matrix):
        raise ValueError("matrix must be a square matrix")

    # Base case: 1x1 matrix
    if n == 1:
        return matrix[0][0]

    # Base case: 2x2 matrix
    if n == 2:
        return matrix[0][0] * matrix[1][1] - \
               matrix[0][1] * matrix[1][0]

    # Recursive case
    det = 0

    for col in range(n):
        # Build minor matrix
        minor = []

        for row in range(1, n):
            minor_row = (
                matrix[row][:col] +
                matrix[row][col + 1:]
            )
            minor.append(minor_row)

        # Cofactor expansion
        cofactor = ((-1) ** col) * matrix[0][col]
        det += cofactor * determinant(minor)

    return det
