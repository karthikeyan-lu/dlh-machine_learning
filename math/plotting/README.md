# Plotting - AI Academy (DLH)

![Python](https://img.shields.io/badge/Python-3.9-blue)
![NumPy](https://img.shields.io/badge/NumPy-1.25.2-orange)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.8.3-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

This project contains data visualization exercises using Matplotlib and NumPy. It focuses on plotting line graphs, scatter plots, histograms, stacked bar charts, subplots, color gradients, and PCA projections.

---

## Objective

To build a strong foundation in Python visualization by learning:

- Plotting data with Matplotlib
- Creating line graphs and scatter plots
- Using logarithmic scales
- Customizing titles, labels, axes, limits, and legends
- Building histograms and stacked bar charts
- Combining multiple visualizations into one figure
- Mapping color gradients to values
- Visualizing PCA-reduced data in 3D

---

## Topics Covered

### Core Plot Types

- Line graphs
- Scatter plots
- Histograms
- Stacked bar charts

### Plot Customization

- Figure sizing
- Axis labels and titles
- Axis limits and tick marks
- Legends
- Logarithmic scales
- Color maps and color bars

### Multi-Plot and Advanced Views

- Subplots
- Combined dashboards
- 3D plotting
- PCA visualization

---

## Requirements

- Ubuntu 20.04 LTS
- Python 3.9
- NumPy 1.25.2
- Matplotlib 3.8.3
- Pillow 10.3.0
- `pycodestyle` 2.11.1
- All Python files should be executable
- All Python files should begin with `#!/usr/bin/env python3`
- Modules and functions should be documented

---

## Installation

```bash
pip install --user matplotlib==3.8.3
pip install --user Pillow==10.3.0
```

---

## Files

| File | Description |
| --- | --- |
| `0-line.py` | Plots a cubic function as a red line graph |
| `1-scatter.py` | Plots men's height and weight as a scatter plot |
| `2-change_scale.py` | Plots Carbon-14 exponential decay on a log scale |
| `3-two.py` | Compares Carbon-14 and Radium-226 decay curves |
| `4-frequency.py` | Plots a histogram of student grades |
| `5-all_in_one.py` | Combines previous plots into one multi-plot figure |
| `6-bars.py` | Creates a stacked bar chart of fruit quantities |
| `100-gradient.py` | Creates a scatter plot with an elevation color gradient |
| `101-pca.py` | Performs PCA and visualizes Iris data in 3D |
| `pca.npz` | Dataset used for the PCA visualization |

---

## Usage

Run a plotting task:

```bash
python3 6-bars.py
```

Import and call a plotting function:

```python
bars = __import__('6-bars').bars

bars()
```

---

## Author

Karthikeyan Marimuthu - AI Academy, Digital Learning Hub Luxembourg
