#!/usr/bin/env python3
"""Set the Timestamp column as the DataFrame index."""


def index(df):
    """
    Set the Timestamp column as the index.

    Args:
        df: pandas DataFrame

    Returns:
        Modified pandas DataFrame.
    """
    return df.set_index("Timestamp")
