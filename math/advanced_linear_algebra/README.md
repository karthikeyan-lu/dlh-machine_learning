# Advanced Linear Algebra - AI Academy (DLH)

![Python](https://img.shields.io/badge/Python-3.9-blue)
![NumPy](https://img.shields.io/badge/NumPy-1.25.2-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Level](https://img.shields.io/badge/Level-Intermediate%20to%20Advanced-red)

This project contains advanced matrix operation exercises implemented with pure Python and NumPy. It covers determinants, minors, cofactors, adjugates, inverses, and matrix definiteness.

---

## Objective

To deepen linear algebra knowledge by learning:

- Recursive determinant calculation
- Minor matrix construction
- Cofactor matrix construction
- Adjugate matrix calculation
- Matrix inversion
- Singular matrix detection
- Symmetric matrix validation
- Eigenvalue-based definiteness classification

---

## Topics Covered

### Matrix Operations

- Determinants
- Minors
- Cofactors
- Adjugates
- Inverses
- Recursive submatrix handling

### Matrix Properties

- Square matrix validation
- Singular and invertible matrices
- Symmetric matrices
- Eigenvalues
- Positive definite matrices
- Negative definite matrices
- Semi-definite matrices
- Indefinite matrices

---

## Requirements

- Ubuntu 20.04 LTS
- Python 3.9
- NumPy 1.25.2
- `pycodestyle` 2.11.1
- All Python files should be executable
- All Python files should begin with `#!/usr/bin/env python3`
- Modules and functions should be documented

---

## Files

| File | Description |
| --- | --- |
| `0-determinant.py` | Calculates the determinant of a square matrix |
| `1-minor.py` | Calculates the minor matrix |
| `2-cofactor.py` | Calculates the cofactor matrix |
| `3-adjugate.py` | Calculates the adjugate matrix |
| `4-inverse.py` | Calculates the inverse of a matrix or returns `None` if singular |
| `5-definiteness.py` | Determines matrix definiteness using NumPy eigenvalues |

---

## Key Concepts Used

- Recursive functions
- List comprehensions
- Matrix validation
- Cofactor expansion
- Matrix transposition
- Determinants and inverses
- NumPy arrays
- NumPy eigenvalue functions

---

## Usage

Calculate a determinant:

```python
determinant = __import__('0-determinant').determinant

matrix = [[1, 2], [3, 4]]
print(determinant(matrix))
```

Output:

```text
-2
```

Calculate an inverse:

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

## Author

Karthikeyan Marimuthu - AI Academy, Digital Learning Hub Luxembourg
