# Calculus - AI Academy (DLH)

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Level](https://img.shields.io/badge/Level-Beginner%20to%20Intermediate-yellow)

This project contains calculus exercises covering summation, products, derivatives, partial derivatives, indefinite integrals, definite integrals, double integrals, and polynomial calculus using pure Python.

---

## Objective

To build practical calculus knowledge by learning:

- Sigma notation
- Product notation
- Series expansion
- Derivative rules
- Product rule
- Chain rule
- Partial derivatives
- Indefinite integrals
- Definite integrals
- Double integrals
- Polynomial differentiation and integration

---

## Topics Covered

### Summation and Products

- Sigma notation
- Summation expansion
- Pi notation
- Product expansion
- Series operations

### Derivatives

- Basic derivative rules
- Polynomial derivatives
- Product rule
- Chain rule
- Partial derivatives
- Higher-order partial derivatives

### Integrals

- Indefinite integrals
- Exponential integrals
- Definite integrals
- Symmetric definite integrals
- Constant definite integrals
- Double integrals
- Polynomial integration

---

## Requirements

- Ubuntu 20.04 LTS
- Python 3.9
- `pycodestyle` 2.11.1
- All Python files should be executable
- All Python files should begin with `#!/usr/bin/env python3`
- Modules and functions should be documented
- Unless otherwise noted, modules should not be imported

---

## Files

| File | Description |
| --- | --- |
| `0-sigma_is_for_sum` | Represents sigma summation notation |
| `1-seegma` | Expands summation notation |
| `2-pi_is_for_product` | Represents product notation |
| `3-pee` | Expands product notation |
| `4-hello_derivatives` | Covers basic derivative rules |
| `5-log_on_fire` | Covers product rule derivatives |
| `6-voltaire` | Covers chain rule derivatives |
| `7-partial_truths` | Covers partial derivatives |
| `8-all-together` | Covers higher-order partial derivatives |
| `9-sum_total.py` | Calculates the summation of `i^2` |
| `10-matisse.py` | Calculates the derivative of a polynomial |
| `11-integral` | Covers indefinite integrals |
| `12-integral` | Covers exponential integrals |
| `13-definite` | Covers definite integrals |
| `14-definite` | Covers symmetric definite integrals |
| `15-definite` | Covers constant definite integrals |
| `16-double` | Covers double integrals |
| `17-integrate.py` | Calculates the integral of a polynomial |

---

## Key Concepts Used

- Summation notation
- Product notation
- Polynomial functions
- Derivative rules
- Integral rules
- Function validation
- List-based polynomial representation
- Pure Python arithmetic

---

## Usage

Calculate a summation of squares:

```python
summation_i_squared = __import__('9-sum_total').summation_i_squared

print(summation_i_squared(5))
```

Output:

```text
55
```

Calculate a polynomial derivative:

```python
poly_derivative = __import__('10-matisse').poly_derivative

poly = [5, 3, 0, 1]
print(poly_derivative(poly))
```

Output:

```text
[3, 0, 3]
```

Calculate a polynomial integral:

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

## Author

Karthikeyan Marimuthu - AI Academy, Digital Learning Hub Luxembourg
