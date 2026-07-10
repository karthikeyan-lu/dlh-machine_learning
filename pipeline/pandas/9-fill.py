#!/usr/bin/env python3
"""Clean and fill missing values in a pandas DataFrame."""


def fill(df):
    """
    Clean the DataFrame by filling missing values.

    Args:
        df: pandas DataFrame

    Returns:
        Modified pandas DataFrame.
    """
    # Remove the Weighted_Price column
    df = df.drop(columns=["Weighted_Price"])

    # Fill missing Close values with the previous valid value
    df["Close"] = df["Close"].ffill()

    # Fill missing Open, High, and Low values with Close
    for col in ["Open", "High", "Low"]:
        df[col] = df[col].fillna(df["Close"])

    # Fill missing volume values with 0
    df["Volume_(BTC)"] = df["Volume_(BTC)"].fillna(0)
    df["Volume_(Currency)"] = df["Volume_(Currency)"].fillna(0)

    return df
