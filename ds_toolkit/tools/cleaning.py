import pandas as pd


def remove_outliers_iqr(df: pd.DataFrame, column: str):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    filtered_df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    return filtered_df


def remove_outliers_zscore(df: pd.DataFrame, column: str, threshold: int = 3):
    mean = df[column].mean()
    std = df[column].std()
    filtered_df = df[(df[column] - mean).abs() <= threshold * std]
    return filtered_df


def remove_outliers_percentile(
    df: pd.DataFrame, column: str, lower_percentile: int = 5, upper_percentile: int = 95
):
    lower_bound = df[column].quantile(lower_percentile / 100)
    upper_bound = df[column].quantile(upper_percentile / 100)
    filtered_df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    return filtered_df
