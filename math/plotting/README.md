````md
# Calculus

This project covers fundamental calculus concepts including summation, products, derivatives, partial derivatives, and integrals using pure Python.

## Learning Objectives

At the end of this project, you should be able to explain:

* Summation and Product notation
* What a series is
* Common series
* What a derivative is
* What the product rule is
* What the chain rule is
* Common derivative rules
* What a partial derivative is
* What an indefinite integral is
* What a definite integral is
* What a double integral is

---

# Requirements

## General

* Allowed editors: `vi`, `vim`, `emacs`
* All files interpreted/compiled on Ubuntu 20.04 LTS using:

  * Python `3.9`

* All files should end with a new line
* The first line of all files should be:

```python
#!/usr/bin/env python3
````

* Code should follow `pycodestyle` style (`version 2.11.1`)
* All files must be executable
* All modules and functions must be documented
* Unless otherwise noted, you are not allowed to import any module

---

# Files

| File                  | Description                      |
| --------------------- | -------------------------------- |
| `0-sigma_is_for_sum`  | Sigma summation notation         |
| `1-seegma`            | Summation expansion              |
| `2-pi_is_for_product` | Product notation                 |
| `3-pee`               | Product evaluation               |
| `4-hello_derivatives` | Basic derivatives                |
| `5-log_on_fire`       | Product rule derivatives         |
| `6-voltaire`          | Chain rule derivatives           |
| `7-partial_truths`    | Partial derivatives              |
| `8-all-together`      | Higher order partial derivatives |
| `9-sum_total.py`      | Summation of squares             |
| `10-matisse.py`       | Polynomial derivatives           |
| `11-integral`         | Indefinite integrals             |
| `12-integral`         | Exponential integrals            |
| `13-definite`         | Definite integrals               |
| `14-definite`         | Symmetric definite integrals     |
| `15-definite`         | Constant definite integrals      |
| `16-double`           | Double integrals                 |
| `17-integrate.py`     | Polynomial integration           |

---

# Concepts

## Summation

Sigma notation is used to represent repeated addition.

Example:

[
\sum_{i=1}^{5} i = 1 + 2 + 3 + 4 + 5
]

---

## Product

Pi notation is used to represent repeated multiplication.

Example:

[
\prod_{i=1}^{4} i = 1 \times 2 \times 3 \times 4
]

---

## Derivatives

The derivative measures the rate of change of a function.

### Power Rule

[
\frac{d}{dx}(x^n) = nx^{n-1}
]

Example:

[
\frac{d}{dx}(x^3) = 3x^2
]

---

## Integrals

Integration is the reverse process of differentiation.

### Power Rule

[
\int x^n , dx = \frac{x^{n+1}}{n+1} + C
]

Example:

[
\int x^3 , dx = \frac{x^4}{4} + C
]

---

## Partial Derivatives

Partial derivatives differentiate multivariable functions with respect to one variable while treating the others as constants.

Example:

[
\frac{\partial}{\partial y}(e^{xy}) = xe^{xy}
]

---

# Usage

## Summation of Squares

```python
summation_i_squared = __import__('9-sum_total').summation_i_squared

print(summation_i_squared(5))
```

Output:

```text
55
```

---

## Polynomial Derivative

```python
poly_derivative = __import__('10-matisse').poly_derivative

poly = [5, 3, 0, 1]

print(poly_derivative(poly))
```

Output:

```text
[3, 0, 3]
```

---

## Polynomial Integral

```python
poly_integral = __import__('17-integrate').poly_integral

poly = [5, 3, 0, 1]

print(poly_integral(poly))
```

Output:

```text
[0, 5, 1.5, 0, 0.25]
```

---

# Author

Karthikeyan Marimuthu

```
```
