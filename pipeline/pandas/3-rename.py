#!/usr/bin/env python3
"""Rename and format DataFrame columns."""

import pandas as pd


def rename(df):
    """
    Rename the Timestamp column to Datetime, convert it to datetime,
    and keep only the Datetime and Close columns.

    Args:
        df: pandas DataFrame

    Returns:
        Modified pandas DataFrame
    """
    df = df.rename(columns={"Timestamp": "Datetime"})
    df["Datetime"] = pd.to_datetime(df["Datetime"], unit="s")
    return df[["Datetime", "Close"]]
