import pandas as pd


def load_dataframe(file_path: str, **kwargs) -> pd.DataFrame:
    df: pd.DataFrame | None = None

    if file_path.endswith(".csv"):
        df = pd.read_csv(file_path, **kwargs)

    if df is not None:
        print(f"Loaded dataframe has {df.shape[0]} rows and {df.shape[1]} features.")
    else:
        print("File at {file_path} could not be loaded as a dataframe!")

    return df
