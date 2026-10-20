# From Jupyter Notebooks to Python Programs

This repository teaches a practical workflow for moving from exploratory notebooks to reusable Python code. You will practice feature engineering in pandas, move those steps into scikit-learn transformers and pipelines, refactor notebook logic into importable Python modules, and complete a guided refactoring exercise on the Titanic dataset.

## Learning Objectives

By the end of this repository, you should be able to:

- Distinguish exploratory notebook steps from stable logic that belongs in reusable code.
- Refactor pandas cleaning and feature-engineering workflows into focused Python functions and modules.
- Implement scikit-learn-compatible custom transformers and compose them into preprocessing pipelines.
- Fit preprocessing steps on training data and reuse them on new data to prevent data leakage.
- Run refactored workflows from Python scripts without relying on notebook state.

## Learning Path

### 01 - Feature Engineering with Pandas

| File | Description |
|---|---|
| [**01 - Feature Engineering with Pandas**](01-feature-engineering-with-pandas/01-feature-engineering-with-pandas.ipynb) | Introduces feature engineering on the Seattle weather dataset using pandas, including data validation with Pydantic, cleaning messy values, standardizing categories, converting types, and handling missing data in a train/new-data-safe way. |

### 02 - Feature Engineering with Scikit-Learn Pipelines

| File | Description |
|---|---|
| [**02 - Feature Engineering with Scikit-Learn Pipelines**](02-feature-engineering-with-sklearn-pipelines/02-feature-engineering-with-sklearn-pipelines.ipynb) | Rebuilds the Seattle weather preprocessing flow with custom scikit-learn transformers and pipelines, focusing on `fit`/`transform` separation, reusable cleanup steps, and safer preprocessing for new data. |
| [**src**](02-feature-engineering-with-sklearn-pipelines/src/) | Custom transformer and pipeline modules, including the worked solution. |

### 03 - Notebook to Python Scripts

| File | Description |
|---|---|
| [**03 - From Jupyter Notebook to Python Script Example**](03-notebook-to-python-scripts/03-from-jupyter-notebook-to-python-scripts-example.ipynb) | Uses the King County housing dataset to show how exploratory notebook work becomes reusable Python code by separating one-off analysis from stable cleaning rules that should be moved into modules. |
| [**King County Data Preparation**](03-notebook-to-python-scripts/king-county-data-preparation.ipynb) | Walks through turning the King County notebook cleaning logic into small reusable functions, including outlier filtering, basement feature rebuilding, last-change calculation, and missing-value filling. |
| [**src**](03-notebook-to-python-scripts/src/) | Refactored King County data preparation functions, including the worked solution. |

### 04 - Refactoring Guide and Titanic Exercise

| File | Description |
|---|---|
| [**04 - Refactoring Guide**](04-refactoring-guide-and-titanic-exercise/04-refactoring-guide.md) | Explains how to decide which parts of the Titanic notebook should stay exploratory and which parts should move into reusable Python functions such as `load_data()`, `preprocess()`, and model-evaluation helpers. |
| [**Titanic Exercise Notebook**](04-refactoring-guide-and-titanic-exercise/titanic-original.ipynb) | Provides a notebook-style Titanic baseline with quick EDA, feature-engineering candidates, age imputation logic, and model comparison steps to be refactored into the accompanying Python exercise file. |
| [**src**](04-refactoring-guide-and-titanic-exercise/src/) | The exercise file to complete and the worked solution as a reference. |

### Additional Folders and Files

| File / Folder | Description |
|---|---|
| [**assets**](assets/) | Visual aids referenced in the repository. |
| [**data**](data/) | Datasets shared across all exercises. |
| [**pyproject.toml**](pyproject.toml) | Project configuration and dependencies. |
| [**uv.lock**](uv.lock) | Dependency lock file. |

## Setup

> [!NOTE]
> Throughout these steps, text in angle brackets like `<repo-name>` is a **placeholder**. Replace it, including the `< >` brackets, with your own value. For example, `cd <repo-name>` becomes `cd mle-from-jupyternb-to-python-files`.

### 1. Create the Repository from the Template

Click **Use this template** on GitHub.

When creating the repository:

- Set yourself as the **Owner**
- Choose a repository name
- Disable **Include all branches**
- Click **Create repository**

> [!IMPORTANT]
> If you are working in pairs or groups, only **one person** should complete this step.

---

### 2. Add Collaborators (Pairs/Groups Only)

If working with teammates:

1. Open the repository on GitHub
2. Go to **Settings → Collaborators**
3. Add your teammates as collaborators
4. Share the repository link with your team

Teammates should accept the invitation before continuing.

---

### 3. Clone the Repository

Copy the SSH URL from the **Code** button on GitHub, then run:

```bash
git clone <copied-ssh-url>
```

The copied SSH URL will look like `git@github.com:<your-username>/<repo-name>.git`.

---

### 4. Move into the Project Folder and Install Dependencies

This installs all dependencies and creates a virtual environment in `.venv/`.

```bash
cd <repo-name>
uv sync
```

---

### 5. Open the Repository in VS Code

> [!NOTE]
> Make sure you open VS Code from the project root so it automatically detects the environment created by `uv sync`.

Launch VS Code in the project root folder:

```bash
code .
```

Then open a notebook and select the Python environment created by `uv sync` as the kernel.

## Suggested Workflow

1. Work through the exercise folders in order: [01 - Feature Engineering with Pandas](01-feature-engineering-with-pandas) -> [02 - Feature Engineering with Scikit-learn Pipelines](02-feature-engineering-with-sklearn-pipelines) -> [03 - Notebook to Python Scripts](03-notebook-to-python-scripts) -> [04 - Refactoring Guide and Titanic Exercise](04-refactoring-guide-and-titanic-exercise/).
2. Open each notebook or guide from its exercise folder. Starter files stay local to each exercise, while datasets are shared from the root [data/](data/) folder.
3. For exercise 04, complete [titanic_exercise.py](04-refactoring-guide-and-titanic-exercise/src/titanic_refactoring/titanic_exercise.py).
4. After your own attempt, use [titanic_solution.py](04-refactoring-guide-and-titanic-exercise/src/titanic_refactoring/titanic_solution.py) as a reference.

## References & Further Reading

- [**Pipelines and composite estimators**](https://scikit-learn.org/stable/modules/compose.html): Official scikit-learn guide to chaining transformers and estimators.
- [**Developing scikit-learn estimators**](https://scikit-learn.org/stable/developers/develop.html): Official guide to writing custom, scikit-learn-compatible transformers.
- [**Cookiecutter Data Science**](https://cookiecutter-data-science.drivendata.org/): A widely used real-world template for organizing data science projects, from notebooks to production code.
