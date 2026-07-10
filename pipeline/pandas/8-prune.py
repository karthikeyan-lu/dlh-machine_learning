#!/usr/bin/env python3
"""Remove rows with NaN values in the Close column."""


def prune(df):
    """
    Remove rows where the Close column contains NaN.

    Args:
        df: pandas DataFrame

    Returns:
        Modified pandas DataFrame.
    """
    return df.dropna(subset=["Close"])
