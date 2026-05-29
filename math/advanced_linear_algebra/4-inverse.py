#!/usr/bin/env python3
"""Module for calculating the inverse of a matrix"""


def determinant(matrix):
    """Calculates the determinant of a matrix"""
    if matrix == [[]]:
        return 1

    n = len(matrix)

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return matrix[0][0] * matrix[1][1] - \
               matrix[0][1] * matrix[1][0]

    det = 0

    for col in range(n):
        submatrix = [
            row[:col] + row[col + 1:]
            for row in matrix[1:]
        ]
        det += ((-1) ** col) * matrix[0][col] * determinant(submatrix)

    return det


def minor(matrix):
    """Calculates the minor matrix of a matrix"""
    n = len(matrix)

    if n == 1:
        return [[1]]

    return [
        [
            determinant([
                matrix[r][:j] + matrix[r][j + 1:]
                for r in range(n)
                if r != i
            ])
            for j in range(n)
        ]
        for i in range(n)
    ]


def cofactor(matrix):
    """Calculates the cofactor matrix of a matrix"""
    n = len(matrix)
    minor_matrix = minor(matrix)

    return [
        [
            minor_matrix[i][j] * ((-1) ** (i + j))
            for j in range(n)
        ]
        for i in range(n)
    ]


def adjugate(matrix):
    """Calculates the adjugate matrix of a matrix"""
    n = len(matrix)
    cof_matrix = cofactor(matrix)

    return [
        [
            cof_matrix[j][i]
            for j in range(n)
        ]
        for i in range(n)
    ]


def inverse(matrix):
    """Calculates the inverse of a matrix"""
    if (not isinstance(matrix, list) or
            len(matrix) == 0 or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)

    if not all(len(row) == n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    det = determinant(matrix)

    if det == 0:
        return None

    adj_matrix = adjugate(matrix)

    return [
        [
            adj_matrix[i][j] / det
            for j in range(n)
        ]
        for i in range(n)
    ]
