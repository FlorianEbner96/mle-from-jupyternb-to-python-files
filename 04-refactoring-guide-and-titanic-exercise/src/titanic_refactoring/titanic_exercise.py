"""Starter script for the Titanic notebook-to-Python refactoring exercise.

Use this file to turn the exploratory Titanic notebook into a small,
reusable Python workflow. The starter stays incomplete on purpose so you can
implement the key preprocessing and model-comparison steps yourself.
"""

from pathlib import Path

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier


def load_data() -> pd.DataFrame:
    """Load the local Titanic dataset.

    Data loading is already implemented so the exercise can focus on the two
    main refactoring tasks: preprocessing and model comparison.
    """

    data_path = Path(__file__).resolve().parents[3] / "data" / "titanic.csv"
    return pd.read_csv(data_path)


def preprocess(dataframe: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    # Convert raw Titanic rows into model-ready features and labels.

    # Exercise steps:
    # 1. Work on a copy of the incoming DataFrame so helper functions stay safe.

    df = dataframe.copy()

    # 2. Fill missing values in `Age`, `Fare` and `Embarked`.
    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Fare"] = df["Fare"].fillna(df["Fare"].dropna().median())
    freq_port = df.Embarked.dropna().mode()[0]
    df["Embarked"] = df["Embarked"].fillna(freq_port)

    # 3. Build `y` from `Survived`.
    y = df["Survived"].astype(int)

    # 4. Drop columns that are not part of this simple baseline feature set.
    features = df.drop(
        columns=["Survived", "PassengerId", "Name", "Ticket", "Cabin"])

    # 5. One-hot encode categorical columns and return `(X, y)`.
    X = pd.get_dummies(features, columns=["Sex", "Embarked"], drop_first=True)
    return X, y


def train_and_score_models(X: pd.DataFrame, y: pd.Series) -> pd.DataFrame:
    # Train a few baseline models and compare their validation accuracy.

    # Exercise steps:
    # 1. Split `(X, y)` into training and validation sets.
    X_train, X_valid, y_train, y_valid = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    # 2. Fit the baseline models listed below.
    ModelList = {
        "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
        "Decision Tree": DecisionTreeClassifier(random_state=42),
        "Random Forest": RandomForestClassifier(n_estimators=200, random_state=42),
        "Gaussian NB": GaussianNB(),
    }
    # 3. Score each model on the validation split, not on the full training data.
    scores: list[dict[str, float | str]] = []
    for name, model in ModelList.items():
        # Fit on the training split, then score on held-out validation data.
        model.fit(X_train, y_train)
        score = model.score(X_valid, y_valid)
        scores.append({"Model": name, "ValidationAccuracy": round(score, 4)})

    # 4. Return a sorted DataFrame with readable model names and scores.
    return (
        pd.DataFrame(scores)
        .sort_values("ValidationAccuracy", ascending=False)
        .reset_index(drop=True)
    )


def main() -> None:
    """Load the dataset and explain the next implementation steps.

    The starter is meant to run, show the dataset shape, and point you toward
    the two functions you still need to complete.
    """

    data = load_data()
    print(
        f"Loaded Titanic data: {data.shape[0]} rows x {data.shape[1]} columns")
    print(
        "This starter module runs successfully, and the two core refactoring steps are still yours to implement."
    )

    try:
        X, y = preprocess(data)
        results = train_and_score_models(X, y)
    except NotImplementedError as exc:
        print(exc)
        print(
            "Next step: complete preprocess() and train_and_score_models() "
            "based on the notebook workflow. After your own attempt, "
            "titanic_solution.py can help you review your approach."
        )
        return

    print(results.to_string(index=False))


if __name__ == "__main__":
    main()
