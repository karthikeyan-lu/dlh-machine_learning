# Advanced Linear Algebra

This project covers advanced matrix operations and concepts in linear algebra using pure Python and NumPy.

## Learning Objectives

At the end of this project, you should be able to explain:

* What the determinant of a matrix is
* What a minor matrix is
* What a cofactor matrix is
* What an adjugate matrix is
* How to calculate the inverse of a matrix
* What matrix definiteness means
* How eigenvalues relate to definiteness
* How to perform recursive matrix operations in Python

---

# Requirements

## General

* Allowed editors: `vi`, `vim`, `emacs`
* All files interpreted/compiled on Ubuntu 20.04 LTS using:

  * Python `3.9`
  * NumPy `1.25.2`
* All files should end with a new line
* The first line of all files should be:

```python
#!/usr/bin/env python3
```

* Code should follow `pycodestyle` style (`version 2.11.1`)
* All files must be executable
* All modules and functions must be documented

---

# Files

| File                | Description                                |
| ------------------- | ------------------------------------------ |
| `0-determinant.py`  | Calculates the determinant of a matrix     |
| `1-minor.py`        | Calculates the minor matrix                |
| `2-cofactor.py`     | Calculates the cofactor matrix             |
| `3-adjugate.py`     | Calculates the adjugate matrix             |
| `4-inverse.py`      | Calculates the inverse of a matrix         |
| `5-definiteness.py` | Determines matrix definiteness using NumPy |

---

# Concepts

## Determinant

The determinant is a scalar value calculated from a square matrix.

For a `2x2` matrix:

[
\begin{vmatrix}
a & b \
c & d
\end{vmatrix}
= ad - bc
]

A matrix is invertible only if its determinant is non-zero.

---

## Minor Matrix

The minor of an element is the determinant of the submatrix formed by removing its row and column.

The minor matrix contains all minors of a matrix.

---

## Cofactor Matrix

The cofactor matrix applies alternating signs to the minor matrix.

Sign pattern:

```text
+ - + -
- + - +
+ - + -
```

Formula:

[
C_{ij} = (-1)^{i+j} M_{ij}
]

---

## Adjugate Matrix

The adjugate matrix is the transpose of the cofactor matrix.

[
adj(A) = C^T
]

---

## Inverse Matrix

The inverse of a matrix is calculated using:

[
A^{-1} = \frac{1}{det(A)} \times adj(A)
]

A matrix is singular if its determinant is `0`, meaning it has no inverse.

---

## Matrix Definiteness

Definiteness describes the behavior of quadratic forms and depends on eigenvalues.

### Categories

| Condition on Eigenvalues | Definiteness           |
| ------------------------ | ---------------------- |
| All eigenvalues > 0      | Positive definite      |
| All eigenvalues >= 0     | Positive semi-definite |
| All eigenvalues < 0      | Negative definite      |
| All eigenvalues <= 0     | Negative semi-definite |
| Mixed signs              | Indefinite             |

---

# Usage

## Determinant

```python
determinant = __import__('0-determinant').determinant

matrix = [[1, 2], [3, 4]]

print(determinant(matrix))
```

Output:

```text
-2
```

---

## Inverse

```python
inverse = __import__('4-inverse').inverse

matrix = [[1, 2], [3, 4]]

print(inverse(matrix))
```

Output:

```text
[[-2.0, 1.0], [1.5, -0.5]]
```

---

# Example

Matrix:

```text
[[5, 7, 9],
 [3, 1, 8],
 [6, 2, 4]]
```

## Cofactor Matrix

```text
[[-12, 36, 0],
 [-10, -34, 32],
 [47, -13, -16]]
```

## Adjugate Matrix

```text
[[-12, -10, 47],
 [36, -34, -13],
 [0, 32, -16]]
```

---

# Author

Karthikeyan Marimuthu
