#!/usr/bin/env python3
"""Concatenate two pandas DataFrames."""

import pandas as pd
index = __import__('10-index').index


def concat(df1, df2):
    """
    Concatenate Bitstamp and Coinbase data.

    Args:
        df1: Coinbase DataFrame.
        df2: Bitstamp DataFrame.

    Returns:
        Concatenated pandas DataFrame.
    """
    # Set Timestamp as the index
    df1 = index(df1)
    df2 = index(df2)

    # Keep Bitstamp rows up to and including timestamp 1417411920
    df2 = df2.loc[:1417411920]

    # Concatenate with hierarchical keys
    return pd.concat([df2, df1], keys=["bitstamp", "coinbase"])
