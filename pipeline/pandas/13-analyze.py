#!/usr/bin/env python3
"""Compute descriptive statistics for a DataFrame."""


def analyze(df):
    """
    Compute descriptive statistics for all columns except Timestamp.

    Args:
        df: pandas DataFrame

    Returns:
        pandas DataFrame containing descriptive statistics.
    """
    return df.drop(columns=["Timestamp"]).describe()
