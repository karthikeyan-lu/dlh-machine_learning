#!/usr/bin/env python3
"""Convert selected DataFrame columns to a NumPy array."""


def array(df):
    """
    Select the last 10 rows of the High and Close columns
    and convert them to a NumPy array.

    Args:
        df: pandas DataFrame

    Returns:
        numpy.ndarray
    """
    return df[["High", "Close"]].tail(10).to_numpy()
