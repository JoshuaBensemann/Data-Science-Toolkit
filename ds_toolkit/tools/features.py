import numpy as np
import pandas as pd


def create_time_series(
    df,
    value_col: str,
    time_col: str,
    min_days: int = 0,
    max_days: int = 365,
    max_days_offset: int = 30,
):
    time_series = np.full(max_days + max_days_offset, fill_value=np.nan)
    for _, row in df.iterrows():
        if row[time_col] < max_days + max_days_offset:
            time_series[row[time_col]] = row[value_col]

    time_series = pd.Series(
        time_series[min_days : max_days + 1], index=range(min_days, max_days + 1)
    )
    return time_series.interpolate(method="linear")[min_days : max_days + 1]
