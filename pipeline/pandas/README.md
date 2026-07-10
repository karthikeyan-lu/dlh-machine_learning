# Pandas - AI Academy (DLH)

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-orange)
![Data Processing](https://img.shields.io/badge/Data-Cleaning%20%26%20Transformation-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

This project introduces the fundamentals of **Pandas**, one of Python's most widely used libraries for data analysis and manipulation. The exercises cover creating DataFrames, importing CSV files, cleaning missing data, indexing, sorting, slicing, concatenation, statistical analysis, hierarchical indexing, and data visualization using real Bitcoin market datasets.

---

## Objective

To develop practical skills in data manipulation using Pandas by learning:

- Creating DataFrames from NumPy arrays and dictionaries
- Loading CSV datasets into DataFrames
- Selecting, filtering, and slicing data
- Cleaning and filling missing values
- Renaming and indexing DataFrames
- Sorting and concatenating DataFrames
- Working with hierarchical indexes (MultiIndex)
- Computing descriptive statistics
- Resampling time-series data
- Visualizing financial datasets with Matplotlib

---

## Topics Covered

### DataFrame Fundamentals

- Creating DataFrames from NumPy arrays
- Creating DataFrames from dictionaries
- Reading CSV files
- Converting DataFrames to NumPy arrays

### Data Manipulation

- Renaming columns
- Selecting rows and columns
- Slicing DataFrames
- Sorting values
- Transposing DataFrames
- Setting indexes
- Concatenating DataFrames
- Hierarchical indexing (MultiIndex)

### Data Cleaning

- Removing columns
- Removing missing values
- Forward filling missing values
- Handling incomplete financial datasets

### Statistical Analysis

- Descriptive statistics
- Summary statistics
- Dataset exploration

### Time-Series Analysis

- Timestamp conversion
- Datetime indexing
- Daily resampling
- Aggregation functions

### Data Visualization

- Financial data visualization
- Daily Bitcoin price aggregation
- Matplotlib plotting

---

## Requirements

- Ubuntu 20.04 LTS
- Python 3.9
- Pandas
- NumPy
- Matplotlib
- All Python files should be executable
- All Python files should begin with:

```python
#!/usr/bin/env python3
```

- Modules, classes, and functions should be documented
- `pycodestyle` compliant

---

## Files

| File | Description |
|------|-------------|
| `0-from_numpy.py` | Creates a DataFrame from a NumPy array |
| `1-from_dictionary.py` | Creates a DataFrame from a Python dictionary |
| `2-from_file.py` | Loads a CSV file into a DataFrame |
| `3-rename.py` | Renames the `Timestamp` column to `Datetime`, converts Unix timestamps to datetime values, and selects the `Datetime` and `Close` columns |
| `4-array.py` | Converts the last 10 rows of the `High` and `Close` columns into a NumPy array |
| `5-slice.py` | Extracts the `High`, `Low`, `Close`, and `Volume_(BTC)` columns and selects every 60th row |
| `6-flip_switch.py` | Reverses the DataFrame into reverse chronological order and transposes it |
| `7-high.py` | Sorts the DataFrame by the `High` column in descending order |
| `8-prune.py` | Removes rows containing missing values in the `Close` column |
| `9-fill.py` | Cleans the dataset by filling missing values and removing the `Weighted_Price` column |
| `10-index.py` | Sets the `Timestamp` column as the DataFrame index |
| `11-concat.py` | Concatenates Coinbase and Bitstamp datasets using a hierarchical index |
| `12-hierarchy.py` | Rearranges the MultiIndex to place `Timestamp` first and sorts the data chronologically |
| `13-analyze.py` | Computes descriptive statistics for all numerical columns |
| `14-visualize.py` | Cleans, aggregates, and visualizes Bitcoin market data from 2017 onward |

---

## Features

### Data Import

- Create DataFrames from NumPy arrays
- Create DataFrames from Python dictionaries
- Load CSV datasets into Pandas
- Convert DataFrames into NumPy arrays

### Data Transformation

- Rename columns
- Convert Unix timestamps into datetime values
- Select specific rows and columns
- Slice DataFrames efficiently
- Reverse and transpose DataFrames

### Data Cleaning

- Remove unnecessary columns
- Remove missing observations
- Forward-fill missing closing prices
- Replace missing Open, High, and Low values using Close prices
- Replace missing trading volumes with zero

### Data Organization

- Set DataFrame indexes
- Sort by column values
- Concatenate multiple datasets
- Create hierarchical indexes (MultiIndex)
- Preserve chronological ordering

### Statistical Analysis

- Generate descriptive statistics
- Explore financial market datasets
- Summarize numerical features

### Time-Series Processing

- Convert Unix timestamps to datetime
- Resample minute-level data into daily intervals
- Aggregate daily data using:

  - **High:** Maximum
  - **Low:** Minimum
  - **Open:** Mean
  - **Close:** Mean
  - **Volume (BTC):** Sum
  - **Volume (Currency):** Sum

### Visualization

- Plot aggregated Bitcoin market data
- Visualize market trends from 2017 onward
- Generate publication-quality time-series charts using Matplotlib

---

## Usage

Run any exercise individually.

Example:

```bash
python3 3-main.py
```

Load a CSV dataset:

```python
from_file = __import__('2-from_file').from_file

df = from_file(
    "coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv",
    ","
)

print(df.head())
```

Generate descriptive statistics:

```python
analyze = __import__('13-analyze').analyze

stats = analyze(df)

print(stats)
```

Visualize daily Bitcoin market data:

```bash
python3 14-visualize.py
```

This generates:

- Daily aggregated Bitcoin market statistics
- A visualization saved as `14visualizepandas.png`

---

## Learning Outcomes

After completing this project, you will be able to:

- Work confidently with Pandas DataFrames
- Import and manipulate CSV datasets
- Clean incomplete real-world datasets
- Handle financial time-series data
- Perform descriptive statistical analysis
- Build hierarchical indexes (MultiIndex)
- Aggregate data using resampling
- Create professional visualizations using Pandas and Matplotlib

---

## Author

**Karthikeyan Marimuthu**  
AI Academy, Digital Learning Hub Luxembourg