# Multivariate Probability - AI Academy (DLH)

![Python](https://img.shields.io/badge/Python-3.9-blue)
![NumPy](https://img.shields.io/badge/NumPy-Multivariate%20Math-orange)
![Statistics](https://img.shields.io/badge/Statistics-Covariance%20%26%20Correlation-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

This project implements multivariate probability and statistics utilities in Python. It focuses on mean vectors, covariance matrices, correlation matrices, multivariate normal distributions, and probability density function (PDF) evaluation.

---

## Objective

To build a practical foundation in multivariate probability by learning:

- Mean vector calculation
- Covariance matrix calculation
- Correlation matrix calculation
- Multivariate normal distribution modeling
- Probability density evaluation for multivariate data
- Matrix-based statistical computation with NumPy
- Input validation for multidimensional data

---

## Topics Covered

### Multivariate Statistics

- Mean vectors
- Covariance matrices
- Correlation matrices
- Standard deviations from covariance
- Centered data matrices

### Multivariate Normal Distribution

- Distribution parameters
- Mean vector estimation
- Covariance matrix estimation
- Multivariate Gaussian PDF

### Matrix Operations

- Matrix transposition
- Matrix multiplication
- Determinants
- Matrix inverses
- Vectorized NumPy calculations

---

## Requirements

- Ubuntu 20.04 LTS
- Python 3.9
- NumPy
- All Python files should be executable
- All Python files should begin with `#!/usr/bin/env python3`
- Modules, classes, and functions should be documented
- `pycodestyle` compliant

---

## Files

| File | Description |
| --- | --- |
| `0-mean_cov.py` | Calculates the mean vector and covariance matrix of a data set |
| `1-correlation.py` | Converts a covariance matrix into a correlation matrix |
| `multinormal.py` | Defines a `MultiNormal` class for multivariate normal distributions |

---

## Features

### Mean and Covariance

- Validates that the input is a 2D NumPy array
- Ensures the data set contains multiple data points
- Calculates the mean vector across features
- Calculates the sample covariance matrix

### Correlation Matrix

- Validates that the input is a NumPy array
- Ensures the covariance matrix is square
- Extracts standard deviations from the covariance diagonal
- Normalizes covariance values into correlations

### MultiNormal Class

- Stores the mean vector of a multivariate normal distribution
- Stores the covariance matrix of the distribution
- Validates multidimensional input data
- Calculates the PDF at a given column vector

---

## Usage

Run a Python interpreter:

```bash
python3
```

Mean and covariance example:

```python
import numpy as np

mean_cov = __import__('0-mean_cov').mean_cov

X = np.array([[1, 2], [3, 4], [5, 6]])
mean, cov = mean_cov(X)

print(mean)
print(cov)
```

Multivariate normal PDF example:

```python
import numpy as np
from multinormal import MultiNormal

data = np.array([[1, 2, 3], [4, 5, 6]])
mn = MultiNormal(data)
x = np.array([[2], [5]])

print(mn.pdf(x))
```

---

## Author

Karthikeyan Marimuthu - AI Academy, Digital Learning Hub Luxembourg
