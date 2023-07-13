import numpy as np
from typing import List
from pandas import DataFrame

def create_features(df: DataFrame, df_pre_computed: DataFrame):
    """
    Create additional features based on the given DataFrame and pre-computed features.

    Args:
        df (DataFrame): The input DataFrame containing the data.
        df_pre_computed (DataFrame): The DataFrame with pre-computed features.

    Returns:
        DataFrame: The DataFrame with additional created features.

    """
    # Create list with feature columns
    feature_columns: List[str] = []
    feature_columns += list(df.columns)
    
    # Merge pre-computed features into the new DataFrame
    df = df.join(df_pre_computed)
    
    # Perform additional feature transformations
    df["AmountLog"] = np.log(df["Amount"])
    df["AmountDiff"] = df["Amount"] - df["AmountLogMean"]
    feature_columns += ["AmountLog", "AmountDiff"]
    df["V1214"] = df["V12"] * df["V14"]
    df["V1217"] = df["V12"] * df["V17"]
    df["V1417"] = df["V14"] * df["V17"]
    feature_columns += ["V1214", "V1217", "V1417"]
    
    return df[feature_columns]