# Probability - AI Academy (DLH)

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Math](https://img.shields.io/badge/Mathematics-Probability-orange)
![Statistics](https://img.shields.io/badge/Statistics-Distributions-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

This project implements several probability distributions from scratch using Python. It focuses on statistical modeling, probability mass functions (PMF), probability density functions (PDF), cumulative distribution functions (CDF), parameter estimation, and distribution analysis.

---

## Objective

To build a strong foundation in probability and statistics by learning:

- Probability distributions
- Distribution parameter estimation
- Probability Mass Functions (PMF)
- Probability Density Functions (PDF)
- Cumulative Distribution Functions (CDF)
- Mean, variance, and standard deviation
- Z-scores and normalization
- Statistical modeling using Python

---

## Topics Covered

### Discrete Distributions

- Poisson Distribution
- Binomial Distribution

### Continuous Distributions

- Exponential Distribution
- Normal Distribution

### Statistical Concepts

- Mean
- Variance
- Standard Deviation
- Z-Score
- Method of Moments

### Probability Functions

- PMF (Probability Mass Function)
- PDF (Probability Density Function)
- CDF (Cumulative Distribution Function)

---

## Requirements

- Ubuntu 20.04 LTS
- Python 3.9
- No external libraries
- No module imports
- All Python files should be executable
- All Python files should begin with `#!/usr/bin/env python3`
- Modules and functions should be documented
- `pycodestyle` compliant

---

## Files

| File | Description |
| --- | --- |
| `poisson.py` | Implementation of the Poisson distribution |
| `exponential.py` | Implementation of the Exponential distribution |
| `normal.py` | Implementation of the Normal (Gaussian) distribution |
| `binomial.py` | Implementation of the Binomial distribution |

---

## Features

### Poisson Distribution

- Estimate λ from data
- PMF calculation
- CDF calculation

### Exponential Distribution

- Estimate λ from data
- PDF calculation
- CDF calculation

### Normal Distribution

- Estimate mean and standard deviation from data
- Z-score calculation
- X-value calculation
- PDF calculation
- CDF calculation

### Binomial Distribution

- Estimate n and p using the Method of Moments
- PMF calculation
- CDF calculation

---

## Usage

Run a Python interpreter:

```bash
python3
```

Example:

```python
from normal import Normal

n = Normal(mean=70, stddev=10)

print(n.z_score(90))
print(n.pdf(90))
print(n.cdf(90))
```

---

## Author

Karthikeyan Marimuthu - AI Academy, Digital Learning Hub Luxembourg