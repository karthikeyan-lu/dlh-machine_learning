#!/usr/bin/env python3
"""Module for calculating the minor matrix"""


def determinant(matrix):
    """Calculates determinant of a matrix"""

    if matrix == [[]]:
        return 1

    n = len(matrix)

    # 1x1 matrix
    if n == 1:
        return matrix[0][0]

    # 2x2 matrix
    if n == 2:
        return (
            matrix[0][0] * matrix[1][1] -
            matrix[0][1] * matrix[1][0]
        )

    det = 0

    for col in range(n):
        submatrix = []

        for row in range(1, n):
            new_row = (
                matrix[row][:col] +
                matrix[row][col + 1:]
            )
            submatrix.append(new_row)

        det += (
            ((-1) ** col) *
            matrix[0][col] *
            determinant(submatrix)
        )

    return det


def minor(matrix):
    """Calculates the minor matrix of a matrix"""

    # Validate matrix type
    if (not isinstance(matrix, list) or
            len(matrix) == 0 or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)

    # Validate square matrix
    if n == 0 or not all(len(row) == n for row in matrix):
        raise ValueError(
            "matrix must be a non-empty square matrix"
        )

    # Special case for 1x1 matrix
    if n == 1:
        return [[1]]

    minor_matrix = []

    for i in range(n):
        row = []

        for j in range(n):

            # Build submatrix without row i and column j
            submatrix = []

            for r in range(n):
                if r != i:
                    new_row = []

                    for c in range(n):
                        if c != j:
                            new_row.append(matrix[r][c])

                    submatrix.append(new_row)

            # Determinant of submatrix
            row.append(determinant(submatrix))

        minor_matrix.append(row)

    return minor_matrix
