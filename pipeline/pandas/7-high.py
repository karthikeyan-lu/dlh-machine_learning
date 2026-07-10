#!/usr/bin/env python3
"""Sort a pandas DataFrame by the High column."""


def high(df):
    """
    Sort the DataFrame by the High price in descending order.

    Args:
        df: pandas DataFrame

    Returns:
        Sorted pandas DataFrame.
    """
    return df.sort_values(by="High", ascending=False)
