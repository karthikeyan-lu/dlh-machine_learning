#!/usr/bin/env python3
"""Load data from a file into a pandas DataFrame."""

import pandas as pd


def from_file(filename, delimiter):
    """
    Load a file into a pandas DataFrame.

    Args:
        filename: Path to the file.
        delimiter: Column separator.

    Returns:
        A pandas DataFrame.
    """
    return pd.read_csv(filename, sep=delimiter)
