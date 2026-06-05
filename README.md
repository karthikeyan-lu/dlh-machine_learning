# Machine Learning Foundations - AI Academy (DLH)

![Python](https://img.shields.io/badge/Python-3.9-blue)
![NumPy](https://img.shields.io/badge/NumPy-1.25.2-orange)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.8.3-green)
![SQL](https://img.shields.io/badge/SQL-MySQL-blue)
![MongoDB](https://img.shields.io/badge/MongoDB-Shell%20%26%20PyMongo-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Level](https://img.shields.io/badge/Level-Beginner%20to%20Advanced-red)

This repository contains my mathematics, visualization, and data pipeline exercises for the **AI Academy course at DLH**. It demonstrates hands-on practice across calculus, linear algebra, plotting, SQL, MongoDB, and PyMongo.

---

## Objective

To build the foundations needed for machine learning by learning:

- Calculus notation and polynomial calculus
- Linear algebra operations with Python lists and NumPy
- Advanced matrix operations and definiteness
- Data visualization with Matplotlib
- SQL database querying and optimization
- MongoDB shell operations
- PyMongo-based document workflows
- Basic data pipeline and log analytics patterns

---

## Topics Covered

### Math

- Summation and product notation
- Derivatives and partial derivatives
- Indefinite, definite, and double integrals
- Matrix shapes and slicing
- Matrix addition, concatenation, and multiplication
- Determinants, minors, cofactors, adjugates, and inverses
- Eigenvalue-based matrix definiteness

### Visualization

- Line graphs
- Scatter plots
- Histograms
- Stacked bar charts
- Subplots
- Logarithmic scales
- Color gradients and color bars
- 3D PCA visualization

### Data Pipeline and Databases

- MySQL database and table creation
- SQL filtering, sorting, aggregation, and joins
- SQL constraints, indexes, views, triggers, functions, and procedures
- MongoDB shell CRUD operations
- PyMongo collection operations
- MongoDB aggregation
- Nginx log statistics

---

## Project Modules

| Folder | Description |
| --- | --- |
| `math/calculus` | Calculus notation, derivatives, integrals, and polynomial calculus |
| `math/linear_algebra` | Python and NumPy matrix operations for foundational linear algebra |
| `math/advanced_linear_algebra` | Determinants, minors, cofactors, adjugates, inverses, and definiteness |
| `math/plotting` | Matplotlib and NumPy visualizations, including PCA plotting |
| `pipeline/databases` | MySQL, MongoDB shell, and PyMongo database exercises |

---

## Key Concepts Used

- Python functions
- Pure Python lists and nested lists
- NumPy arrays
- Matplotlib figures and axes
- Matrix validation
- Recursive matrix algorithms
- SQL queries
- MySQL joins and aggregation
- MySQL indexes, views, triggers, procedures, and functions
- MongoDB documents and collections
- PyMongo
- Aggregation pipelines

---

## Project Structure

```text
dlh-machine_learning/
|
├── math/
│   ├── calculus/
│   ├── linear_algebra/
│   ├── advanced_linear_algebra/
│   └── plotting/
│
├── pipeline/
│   └── databases/
│
├── requirements.txt
├── aiacademy.yml
└── README.md
```

---

## Requirements

- Ubuntu 20.04 LTS
- Python 3.9
- NumPy 1.25.2
- Matplotlib 3.8.3
- Pillow 10.3.0
- MySQL
- MongoDB
- PyMongo
- `pycodestyle` 2.11.1

---

## Usage

Run a Python task:

```bash
python3 math/linear_algebra/0-slice_me_up.py
```

Run a plotting task:

```bash
python3 math/plotting/6-bars.py
```

Run a MySQL script:

```bash
mysql -uroot -p < pipeline/databases/0-create_database_if_missing.sql
```

Run a PyMongo script:

```bash
python3 pipeline/databases/34-log_stats.py
```

---

## Module READMEs

- `math/calculus/README.md`
- `math/linear_algebra/README.md`
- `math/advanced_linear_algebra/README.md`
- `math/plotting/README.md`
- `pipeline/databases/README.md`

---

## Author

Karthikeyan Marimuthu - AI Academy, Digital Learning Hub Luxembourg
