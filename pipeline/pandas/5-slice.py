#!/usr/bin/env python3
"""Slice a pandas DataFrame."""


def slice(df):
    """
    Extract the High, Low, Close, and Volume_(BTC) columns
    and select every 60th row.

    Args:
        df: pandas DataFrame

    Returns:
        Sliced pandas DataFrame.
    """
    return df[["High", "Low", "Close", "Volume_(BTC)"]].iloc[::60]
