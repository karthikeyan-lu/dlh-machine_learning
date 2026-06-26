# Bayesian Probability - AI Academy (DLH)

![Python](https://img.shields.io/badge/Python-3.9-blue)
![NumPy](https://img.shields.io/badge/NumPy-Bayesian%20Arrays-orange)
![SciPy](https://img.shields.io/badge/SciPy-Beta%20Posterior-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

This project implements Bayesian probability calculations in Python. It focuses on likelihood, intersection, marginal probability, posterior probability, and continuous posterior intervals for binomial observations.

---

## Objective

To build a practical foundation in Bayesian probability by learning:

- Binomial likelihood calculations
- Prior probability distributions
- Intersection of likelihood and prior
- Marginal probability of observed data
- Posterior probability updates
- Continuous posterior probability over an interval
- Input validation for probabilistic models

---

## Topics Covered

### Bayesian Inference

- Prior probability
- Likelihood
- Intersection
- Marginal probability
- Posterior probability

### Binomial Modeling

- Number of successes
- Number of trials
- Candidate probability values
- Uniform prior assumptions

### Continuous Posterior Probability

- Beta distribution parameters
- Posterior probability over a range
- Regularized incomplete beta function

---

## Requirements

- Ubuntu 20.04 LTS
- Python 3.9
- NumPy
- SciPy
- All Python files should be executable
- All Python files should begin with `#!/usr/bin/env python3`
- Modules and functions should be documented
- `pycodestyle` compliant

---

## Files

| File | Description |
| --- | --- |
| `0-likelihood.py` | Calculates the likelihood of observing `x` successes in `n` trials for each probability in `P` |
| `1-intersection.py` | Calculates the intersection of likelihood and prior probability |
| `2-marginal.py` | Calculates the marginal probability of the observed data |
| `3-posterior.py` | Calculates posterior probabilities for each candidate probability |
| `100-continuous.py` | Calculates the posterior probability that `p` falls within a continuous interval |

---

## Features

### Likelihood

- Validates the number of trials and successes
- Validates candidate probability values
- Computes binomial likelihood for a 1D NumPy array of probabilities

### Intersection

- Validates prior probabilities
- Ensures prior probabilities match the candidate probability shape
- Multiplies likelihood by the prior distribution

### Marginal Probability

- Computes the total probability of observing the data
- Sums the intersection across all candidate probability values

### Posterior Probability

- Applies Bayes' theorem
- Normalizes the intersection by the marginal probability
- Returns updated probabilities for each hypothesis in `P`

### Continuous Posterior

- Uses the beta posterior distribution
- Calculates the probability that `p` lies between `p1` and `p2`
- Uses SciPy's regularized incomplete beta function

---

## Usage

Run a Python interpreter:

```bash
python3
```

Example:

```python
import numpy as np

posterior = __import__('3-posterior').posterior

P = np.linspace(0, 1, 11)
Pr = np.ones(11) / 11

print(posterior(26, 130, P, Pr))
```

Continuous posterior example:

```python
posterior = __import__('100-continuous').posterior

print(posterior(26, 130, 0.17, 0.23))
```

---

## Author

Karthikeyan Marimuthu - AI Academy, Digital Learning Hub Luxembourg
