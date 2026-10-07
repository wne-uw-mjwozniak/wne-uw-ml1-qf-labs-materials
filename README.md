# Machine Learning in Finance I (2400-QFU1MLF) — Lab Materials

Lab notebooks for the **Machine Learning in Finance I** course (Quantitative Finance, Faculty of Economic Sciences, University of Warsaw).

Lecturer: dr Michał Woźniak

## Lecture Materials

Slides are available here:
[Lecture Materials (Google Slides)](https://docs.google.com/presentation/d/1G5hvY6wKj9ig5f0dToDHKsznlwjw3UBT6wUsPASYiHQ/edit?usp=sharing)

## Course Schedule (Winter Semester 2026/27)

- **Lectures** (common for all groups): Tuesday 16:45–18:15, room A203 (Building A).
- **Labs**: all lab groups cover the same content. In the *Date* column, the first date is for the groups starting on 8 October (Thursday 13:15–14:45, Aula I, Building C; Thursday 15:00–16:30, room A102, Building A), the second date for the group starting on 15 October (Thursday 15:00–16:30, room A102, Building A).

| Class | Date | Topic | Materials |
|---|---|---|---|
| Lab 1 | 08.10 / 15.10 | Introduction to the course, what is machine learning, the course repository, Python refresher | this README, [SETUP.md](SETUP.md), `python_course.ipynb` |
| Lecture 1 | 13.10 | Introduction to Machine Learning: loss functions, gradient descent, linear and logistic regression | slides, Chapter 1 |
| Lab 2 | 22.10 / 29.10 | Opening mini-lecture (~20 min): ML project workflow, data preparation, EDA, imputation and feature engineering (slides, Chapter 4); then the lab: exploratory data analysis, data wrangling, data engineering | slides, Chapter 4 (first part); `eda_and_data_wrangling.ipynb` |
| Lecture 2 | 27.10 | Assessing model accuracy, machine learning diagnostics, cross-validation; regularization, hyperparameter tuning, feature selection | slides, Chapter 2 and Chapter 4 (second part) |
| Lab 3 | 05.11 / 12.11 | Linear and logistic regression in practice, the Kaggle League starter | `linear_and_logistic_regression.ipynb`, `kaggle_league_starter.ipynb` |
| Lecture 3 | 10.11 | K-nearest neighbours; class rebalancing, probability calibration, model drift | slides, Chapters 3 and 4 |
| Lab 4 | 19.11 / 26.11 | K-nearest neighbours | `knn.ipynb` |
| Lecture 4 | 24.11 | Support Vector Machines (SVM, SVR) | slides, Chapter 3 |
| Lab 5 | 03.12 / 10.12 | Support Vector Machines | `svm.ipynb` |
| Lecture 5 | 08.12 | Decision trees, Random Forest, ensembles | slides, Chapters 3 and 4 |
| Lab 6 | 17.12 / 07.01 | Decision trees and Random Forest | `decision_trees_and_random_forest.ipynb` |
| Lab 7 | 14.01 / 21.01 | Core machine learning techniques | `core_ml_techniques.ipynb` |
| Lecture 6 | 19.01 | Revision lecture, Kaggle League finale | — |

The final theoretical exam takes place in the winter examination session (date in USOS).

## Quick Start

```bash
git clone https://github.com/wne-uw-mjwozniak/wne-uw-ml1-qf-labs-materials.git
cd wne-uw-ml1-qf-labs-materials
uv sync
uv run jupyter lab
```

**New to `uv`, virtual environments or Git?** Follow the step-by-step guide in **[SETUP.md](SETUP.md)** — it explains what `uv` is, how to install it on Windows / macOS / Linux, how to select the kernel in VS Code, and how to fix the most common problems.

**New to Python, or a bit rusty?** Work through [`notebooks/python_course.ipynb`](notebooks/python_course.ipynb) — it is introduced in Lab 1 and should be completed during the first weeks of the semester.

## Notebooks

| Notebook | Used in | Topics |
|---|---|---|
| [`python_course.ipynb`](notebooks/python_course.ipynb) | Lab 1 + self-study | A complete Python course for independent work — no machine learning, that starts in the labs: language basics, collections, control flow, functions, errors, standard library, file I/O, OOP, generators, NumPy (incl. linear algebra and simulation), pandas, matplotlib / seaborn, code quality and reproducibility. 37 exercises with hidden solutions and a capstone project (multi-asset portfolio analysis). |
| [`eda_and_data_wrangling.ipynb`](notebooks/eda_and_data_wrangling.ipynb) | Lab 2 | Exploratory data analysis and data wrangling on a real bank-marketing dataset: ingestion, hidden missing values and sentinels, consistency checks, reconstructing the time dimension, target leakage, out-of-time vs. random splits, univariate / bivariate / multivariate analysis (confidence intervals, Cramér's V, Information Value, VIF, PCA), feature stability over time (PSI), stateless feature engineering, saving data, turning EDA findings into modelling decisions |
| [`linear_and_logistic_regression.ipynb`](notebooks/linear_and_logistic_regression.ipynb) | Lab 3 | Linear and logistic regression (from scratch, scikit-learn and statsmodels) and their regularized variants (Ridge, Lasso, Elastic Net, L1 / L2 / Elastic Net logistic regression) |
| [`knn.ipynb`](notebooks/knn.ipynb) | Lab 4 | K-Nearest Neighbors: from-scratch implementation, K-D trees, scikit-learn, cross-validation, hyperparameter tuning |
| [`svm.ipynb`](notebooks/svm.ipynb) | Lab 5 | Support Vector Machines: primal (sub-gradient) and dual (kernel) from-scratch implementations, SVC / SVR, cross-validation, hyperparameter tuning |
| [`decision_trees_and_random_forest.ipynb`](notebooks/decision_trees_and_random_forest.ipynb) | Lab 6 | CART and Random Forest from scratch; tree inspection, overfitting, cost-complexity pruning, instability, extrapolation; bagging vs. Random Forest vs. Extra Trees, OOB error, MDI vs. permutation importance, predicted probabilities; hyperparameter tuning; a complete credit-scoring pipeline with categorical features, class weights and a cost-based decision threshold |
| [`kaggle_league_starter.ipynb`](notebooks/kaggle_league_starter.ipynb) | Lab 3, Kaggle League | Submission template that satisfies all formal rules of the League: header cell, raw Kaggle files, preprocessing in a pipeline, model restricted to the edition's family (enforced by an assertion), cross-validated score vs. the naive baseline, fixed seeds, submission file in `sample_submission` format with an MD5 checksum for the reproducibility check. Runs on a synthetic demo dataset until the real competitions open |
| [`core_ml_techniques.ipynb`](notebooks/core_ml_techniques.ipynb) | Lab 7 (Sections 1–4 also support Lab 3) | Core ML techniques: imputation, feature engineering, regularization, feature selection, class rebalancing, ensembles, calibration, drift, evaluation metrics, CV variants, Bayesian hyperparameter search |

Every model notebook follows the same structure: theory → from-scratch implementation → scikit-learn → cross-validation and hyperparameter tuning → complete pipeline → best practices → homework assignment.

The notebooks are committed **without outputs** — run them yourself (`Run → Run All Cells`).

### Kaggle League

Each edition of the Kaggle League is restricted to one model family, and the corresponding notebook is your starting point. Editions open on Monday at 12:00 and close on Sunday at 23:59 (Warsaw time):

| Edition | Model family | Opens | Closes | Notebook |
|---|---|---|---|---|
| 1 | Linear & logistic regression | 16.11.2026 | 29.11.2026 | `linear_and_logistic_regression.ipynb` |
| 2 | K-nearest neighbours | 30.11.2026 | 13.12.2026 | `knn.ipynb` |
| 3 | Support Vector Machines | 14.12.2026 | 27.12.2026 | `svm.ipynb` |
| 4 | Decision trees & Random Forest | 28.12.2026 | 10.01.2027 | `decision_trees_and_random_forest.ipynb` |

Register your team by **Sunday 25.10.2026, 23:59**. The finale (final results and presentations of the top-3 teams) takes place at the last lecture on 19.01.2027.

Preprocessing, feature engineering, feature selection, tuning and calibration techniques from `core_ml_techniques.ipynb` are allowed in every edition. Start every submission from [`kaggle_league_starter.ipynb`](notebooks/kaggle_league_starter.ipynb). The full rules are in the lecture slides.

## Data

Most notebooks use datasets bundled with scikit-learn or downloaded by it on first use (cached in `~/scikit_learn_data`, so the first run needs an internet connection). Three real datasets (Bank Marketing, German Credit, Default of Credit Card Clients — all CC BY 4.0 from the UCI repository) and a synthetic Kaggle-format demo ship in `data/` and are documented in [`data/README.md`](data/README.md).

## External Tutorial — Kedro

In addition to the notebooks above, we recommend a self-study project-structuring tutorial
using the [Kedro](https://kedro.org/) framework. It is a
Python framework for building production-grade, reproducible data science pipelines
(data catalog, nodes, pipelines, parameters, experiment tracking).

**Follow the official Spaceflights tutorial:**
[https://docs.kedro.org/en/stable/tutorials/spaceflights_tutorial/](https://docs.kedro.org/en/stable/tutorials/spaceflights_tutorial/)

By the end of the tutorial you will have built a Kedro project that ingests raw data,
engineers features, trains a regression model, and reports metrics — all through
declarative pipeline configuration rather than one-off notebook cells.

## Repository Structure

```text
.
├── notebooks/               # lab notebooks (see the table above)
├── data/                    # datasets shipped with the repository + their documentation
│   └── kaggle_demo/         # synthetic train/test/sample_submission files for the Kaggle League starter
├── SETUP.md                 # step-by-step environment setup guide for students
├── pyproject.toml           # project dependencies
├── uv.lock                  # exact, cross-platform pinned versions of all packages
├── .python-version          # Python version used by uv (3.12)
└── .pre-commit-config.yaml  # code-quality hooks (for contributors)
```

## Setup (short version)

This project uses [uv](https://docs.astral.sh/uv/) for dependency management. The detailed guide is in [SETUP.md](SETUP.md).

### Installing uv

**macOS / Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

After installation, restart your terminal.

### Install dependencies and launch JupyterLab

```bash
uv sync
uv run jupyter lab
```

> **Recommendation:** While JupyterLab/Notebook works fine, we recommend running notebooks inside a full IDE such as [VS Code](https://code.visualstudio.com/), [PyCharm](https://www.jetbrains.com/pycharm/), or [Cursor](https://www.cursor.com/). IDEs provide better code completion, debugging, and Git integration. After running `uv sync`, select the `.venv` environment as your Python interpreter in the IDE.

### Keeping up to date

```bash
git pull
uv sync
```

## Contributing / Development

### Pre-commit hooks

This project uses [pre-commit](https://pre-commit.com/) to enforce code quality on every commit. Install the hooks after syncing dependencies:

```bash
uv sync --dev
uv run pre-commit install
```

The following hooks run automatically on `git commit`:

| Hook | What it does |
|---|---|
| `trailing-whitespace` | Strips trailing whitespace from all files |
| `end-of-file-fixer` | Ensures files end with a single newline |
| `check-yaml` / `check-toml` | Validates YAML and TOML syntax |
| `check-merge-conflict` | Catches leftover merge conflict markers |
| `ruff-check` | Lints and auto-fixes Python files (E, F, W, I rules) |
| `ruff-format` | Formats Python files (Black-compatible) |
| `nbqa-ruff` | Runs ruff linting on notebook cells |
| `nbqa-ruff-format` | Runs ruff formatter on notebook cells |
| `nbstripout` | Cleans notebook metadata before committing. It is configured with `--keep-output --keep-count`, i.e. it does **not** remove cell outputs — clear them yourself (`Edit → Clear Outputs of All Cells`) before committing a lab notebook |

To run all hooks manually against all files:

```bash
uv run pre-commit run --all-files
```

The `ruff` and `nbstripout` hook versions in `.pre-commit-config.yaml` are kept equal to the versions pinned in `uv.lock`, so that `uv run ruff ...` and the hooks always agree.

### Linting rules

Ruff is configured in `pyproject.toml` with:
- **Line length:** 120 characters
- **Rules:** `E` (pycodestyle errors), `F` (pyflakes), `W` (pycodestyle warnings), `I` (isort)
- **Notebook-specific ignores:** `E402` (import-not-at-top, expected in cells), `E501` (line-too-long, alignment-heavy print statements)

## Dependencies

- `numpy`, `pandas` – data manipulation
- `matplotlib`, `seaborn` – visualization
- `scikit-learn` – machine learning models and utilities
- `scipy` – scientific computing
- `statsmodels` – classical statistical inference (OLS, GLM, p-values, confidence intervals)
- `scikit-optimize` – Bayesian hyperparameter search (`BayesSearchCV`)
- `imbalanced-learn` – handling imbalanced datasets
- `jupyter`, `ipykernel` – notebook environment

### Dev dependencies

- `ruff` – linter and formatter
- `pre-commit` – git hook manager
- `nbqa` – run linters on Jupyter notebooks
- `nbstripout` – clean notebook metadata before committing
