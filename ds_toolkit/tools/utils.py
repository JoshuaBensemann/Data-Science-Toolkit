from itertools import chain, combinations
import pandas as pd
import numpy as np


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def ts_train_test_split(
    df: pd.DataFrame,
    id_col: str,
    split_col: str,
    train_pct: float = 0.8,
    random_seed: int = 1986,
):
    ids_and_dates = df.groupby(id_col).agg({split_col: "first"})
    split_date = ids_and_dates.quantile(train_pct).item()

    train_df = df.loc[df[split_col] < split_date].copy()
    remainder = df.loc[df[split_col] >= split_date].copy()

    remaining_ids = remainder[id_col].unique()
    rng = np.random.default_rng(seed=random_seed)
    val_ids = rng.choice(
        remaining_ids, size=int(remaining_ids.shape[0] / 2), replace=False
    )
    val_df = remainder.loc[remainder[split_col].isin(val_ids)].copy()
    test_df = remainder.loc[~remainder[split_col].isin(val_ids)].copy()

    return train_df, val_df, test_df
