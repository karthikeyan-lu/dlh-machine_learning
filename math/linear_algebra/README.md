# Linear Algebra - AI Academy (DLH)

![Python](https://img.shields.io/badge/Python-3.9-blue)
![NumPy](https://img.shields.io/badge/NumPy-1.25.2-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Level](https://img.shields.io/badge/Level-Beginner%20to%20Intermediate-yellow)

This project contains Python and NumPy exercises for foundational linear algebra. It covers arrays, vectors, matrices, slicing, transposition, matrix addition, concatenation, element-wise operations, and matrix multiplication.

---

## Objective

To build practical linear algebra skills by learning:

- List and NumPy array slicing
- Matrix shape detection
- Matrix transposition
- Element-wise array and matrix operations
- Matrix concatenation across axes
- Matrix multiplication
- Recursive operations on nested matrices
- NumPy-based matrix manipulation

---

## Topics Covered

### Python Lists and Matrices

- Array slicing
- Matrix slicing
- Matrix shape calculation
- 2D matrix transposition
- Element-wise array addition
- Element-wise 2D matrix addition
- Array and matrix concatenation
- Pure Python matrix multiplication

### NumPy Arrays

- NumPy slicing
- NumPy shape inspection
- NumPy transposition
- Element-wise arithmetic
- NumPy concatenation
- NumPy matrix multiplication

### Advanced Matrix Handling

- Multi-axis slicing
- Recursive matrix addition
- Recursive matrix concatenation
- Shape validation across nested lists

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
| `0-slice_me_up.py` | Slices a Python list into selected ranges |
| `1-trim_me_down.py` | Extracts middle columns from a 2D matrix |
| `2-size_me_please.py` | Returns the shape of a matrix |
| `3-flip_me_over.py` | Transposes a 2D matrix |
| `4-line_up.py` | Adds two arrays element-wise |
| `5-across_the_planes.py` | Adds two 2D matrices element-wise |
| `6-howdy_partner.py` | Concatenates two arrays |
| `7-gettin_cozy.py` | Concatenates two 2D matrices by axis |
| `8-ridin_bareback.py` | Multiplies two matrices |
| `9-let_the_butcher_slice_it.py` | Slices a NumPy matrix by rows, columns, and submatrix |
| `10-ill_use_my_scale.py` | Returns the shape of a NumPy array |
| `11-the_western_exchange.py` | Transposes a NumPy array |
| `12-bracin_the_elements.py` | Performs NumPy element-wise arithmetic |
| `13-cats_got_your_tongue.py` | Concatenates NumPy arrays by axis |
| `14-saddle_up.py` | Multiplies NumPy matrices |
| `100-slice_like_a_ninja.py` | Slices NumPy arrays along specified axes |
| `101-the_whole_barn.py` | Adds matrices recursively |
| `102-squashed_like_sardines.py` | Concatenates matrices recursively along an axis |

---

## Usage

Run a script directly:

```bash
python3 0-slice_me_up.py
```

Import and test a function:

```python
matrix_shape = __import__('2-size_me_please').matrix_shape

matrix = [[1, 2], [3, 4]]
print(matrix_shape(matrix))
```

Output:

```text
[2, 2]
```

---

## Author

Karthikeyan Marimuthu - AI Academy, Digital Learning Hub Luxembourg
