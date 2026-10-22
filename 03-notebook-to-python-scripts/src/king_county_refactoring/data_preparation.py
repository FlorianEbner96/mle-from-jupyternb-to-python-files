"""Starter functions for the King County notebook-to-script refactoring lesson.

This file is the exercise version used alongside:
- `03-notebook-to-python-scripts/03-from-jupyter-notebook-to-python-scripts-example.ipynb`
- `03-notebook-to-python-scripts/king-county-data-preparation.ipynb`

Each function should:
- accept a pandas DataFrame,
- work on a copy,
- apply one focused transformation,
- and return the transformed DataFrame.
"""

from pathlib import Path

import numpy as np
import pandas as pd


def bath_bed_ratio_outlier(df):
    # Exercise goal: Remove outlier rows based on `bathrooms / bedrooms` ratio.
    # @TODO:
    # 1. Work on a DataFrame copy.
    # 2. Build a helper column named `bath_bed_ratio`.
    # 3. Mark rows where the ratio is >= 2 or <= 0.10.
    # 4. Keep only the rows that are inside the valid range.
    # 5. Drop the helper column before returning so the output schema matches the input schema.
    # Reference solution: `03-notebook-to-python-scripts/src/king_county_refactoring/data_preparation_solution.py`.

    # 1. Work on a DataFrame copy.
    df = df.copy()
    # 2. Build a helper column named `bath_bed_ratio`.
    df["bath_bed_ratio"] = df["bathrooms"] / df["bedrooms"]
    # 3. Mark rows where the ratio is >= 2 or <= 0.10.
    invalid_ratio = (df["bath_bed_ratio"] >= 2) | (
        df["bath_bed_ratio"] <= 0.10)
    # 4. Keep only the rows that are inside the valid range.
    df = df.loc[~invalid_ratio].copy()
    # 5. Drop the helper column before returning so the output schema matches the input schema.
    df.drop(columns=["bath_bed_ratio"], inplace=True)
    return df


def sqft_basement(df):
    # Exercise goal: Recompute `sqft_basement` from reliable source columns.
    # @TODO:
    # 1. Work on a DataFrame copy.
    df = df.copy()
    # 2. Recompute `sqft_basement` as `sqft_living - sqft_above`.
    df["sqft_basement"] = df["sqft_living"] - df["sqft_above"]
    # 3. Return the cleaned DataFrame.
    return df


def calculate_last_change(df):
    # Exercise goal: Create `last_known_change` from `yr_renovated` and `yr_built`.
    # @TODO:
    # 1. Work on a DataFrame copy.
    df = df.copy()

    last_known_change = []

    for idx, yr_re in df["yr_renovated"].items():
        # Missing values or 0 mean "no known renovation",
        # so we fall back to the original build year.
        if str(yr_re) == "nan" or yr_re == 0.0:
            last_known_change.append(df["yr_built"][idx])
        else:
            # Otherwise, keep the renovation year as the last known change.
            last_known_change.append(int(yr_re))

    ["last_known_change"] = last_known_change

    df.drop("yr_renovated", axis=1, inplace=True)
    df.drop("yr_built", axis=1, inplace=True)

    return df


def fill_missings_view_wf(df):
    # Exercise goal: Fill missing values in `view` and `waterfront` with 0.
    # @TODO:
    # 1. Work on a DataFrame copy.
    df = df.copy()
    # 2. Fill missing values in `view` with 0.
    df["view"] = df["view"].fillna(0)
    # 3. Fill missing values in `waterfront` with 0.
    df["waterfront"] = df["waterfront"].fillna(0)
    # 4. Return the cleaned DataFrame.
    return df


def main() -> None:
    """Load the teaching dataset and list the starter tasks."""

    data_path = (
        Path(__file__).resolve().parents[3]
        / "data"
        / "King_County_House_prices_dataset.csv"
    )
    df = pd.read_csv(data_path)

    print("King County starter module loaded successfully.")
    print(
        "This starter module runs successfully. The four cleaning functions are still yours to implement."
    )
    print(f"Loaded dataset shape: {df.shape}")
    print("Starter functions to complete:")
    print("- bath_bed_ratio_outlier(df)")
    print("- sqft_basement(df)")
    print("- calculate_last_change(df)")
    print("- fill_missings_view_wf(df)")


if __name__ == "__main__":
    main()
