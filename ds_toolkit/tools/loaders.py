import pandas as pd
from pandas.io.parsers import TextFileReader

from typing import Optional


def load_dataframe(file_path: str, **kwargs) -> Optional[pd.DataFrame]:
    df: pd.DataFrame = pd.DataFrame()

    if file_path.endswith(".csv"):
        result = pd.read_csv(file_path, **kwargs)
        # Handle chunked reading
        if isinstance(result, TextFileReader):
            df = pd.concat(result, ignore_index=True)
        else:
            df = result

    if df.empty:
        print(f"File at {file_path} could not be loaded as a dataframe!")

    else:
        print(df.info())

    return df
