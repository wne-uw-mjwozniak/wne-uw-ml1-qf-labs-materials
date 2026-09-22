# Machine Learning in Finance I (2400-QFU1MLF) — Lab Materials

Lab notebooks for the **Machine Learning in Finance I** course (Quantitative Finance, Faculty of Economic Sciences, University of Warsaw).

Lecturer: dr Michał Woźniak

## Lecture Materials

Slides are available here:
[Lecture Materials (Google Slides)](https://docs.google.com/presentation/d/1G5hvY6wKj9ig5f0dToDHKsznlwjw3UBT6wUsPASYiHQ/edit?usp=sharing)

## Quick Start

```bash
git clone https://github.com/wne-uw-mjwozniak/wne-uw-ml1-qf-labs-materials.git
cd wne-uw-ml1-qf-labs-materials
uv sync
uv run jupyter lab
```

**New to `uv`, virtual environments or Git?** Follow the step-by-step guide in **[SETUP.md](SETUP.md)** — it explains what `uv` is, how to install it on Windows / macOS / Linux, how to select the kernel in VS Code, and how to fix the most common problems.

**New to Python, or a bit rusty?** Work through [`notebooks/python_course.ipynb`](notebooks/python_course.ipynb) before the first lab.

## Notebooks

| Notebook | Used in | Topics |
|---|---|---|
| [`python_course.ipynb`](notebooks/python_course.ipynb) | Self-study (before Lab 1) | A complete Python course for independent work: language basics, collections, control flow, functions, errors, standard library, file I/O, OOP (incl. a scikit-learn-style estimator), generators, NumPy, pandas, matplotlib / seaborn, a first scikit-learn pipeline, code quality. 41 exercises with hidden solutions and a capstone project. |
| [`eda_and_econometric_models.ipynb`](notebooks/eda_and_econometric_models.ipynb) | Lab 1 | Exploratory data analysis, data wrangling and a first econometric model on a real bank-marketing dataset: ingestion, hidden missing values and sentinels, consistency checks, reconstructing the time dimension, target leakage, out-of-time vs. random splits, univariate / bivariate / multivariate analysis (confidence intervals, Cramér's V, Information Value, VIF, PCA), feature engineering, saving data, linear probability model and logit with odds ratios and marginal effects, multicollinearity in practice, time-aware validation |
| [`linear_and_logistic_regression.ipynb`](notebooks/linear_and_logistic_regression.ipynb) | Lab 1 | Linear and logistic regression (from scratch, scikit-learn and statsmodels) and their regularized variants (Ridge, Lasso, Elastic Net, L1 / L2 / Elastic Net logistic regression) |
| [`knn.ipynb`](notebooks/knn.ipynb) | Lab 2 | K-Nearest Neighbors: from-scratch implementation, K-D trees, scikit-learn, cross-validation, hyperparameter tuning |
| [`svm.ipynb`](notebooks/svm.ipynb) | Lab 3 | Support Vector Machines: primal (sub-gradient) and dual (kernel) from-scratch implementations, SVC / SVR, cross-validation, hyperparameter tuning |
| [`decision_trees_and_random_forest.ipynb`](notebooks/decision_trees_and_random_forest.ipynb) | Lecture 5 / self-study | CART and Random Forest from scratch; tree inspection, overfitting, cost-complexity pruning, instability, extrapolation; bagging vs. Random Forest vs. Extra Trees, OOB error, MDI vs. permutation importance, predicted probabilities; hyperparameter tuning; a complete credit-scoring pipeline with categorical features, class weights and a cost-based decision threshold |
| [`kaggle_league_starter.ipynb`](notebooks/kaggle_league_starter.ipynb) | Kaggle League | Submission template that satisfies all formal rules of the League: header cell, raw Kaggle files, preprocessing in a pipeline, model restricted to the edition's family (enforced by an assertion), cross-validated score vs. the naive baseline, fixed seeds, submission file in `sample_submission` format with an MD5 checksum for the reproducibility check. Runs on a synthetic demo dataset until the real competitions open |
| [`core_ml_techniques.ipynb`](notebooks/core_ml_techniques.ipynb) | Labs 4–5 | Core ML techniques: imputation, feature engineering, regularization, feature selection, class rebalancing, ensembles, calibration, drift, evaluation metrics, CV variants, Bayesian hyperparameter search |

Every model notebook follows the same structure: theory → from-scratch implementation → scikit-learn → cross-validation and hyperparameter tuning → complete pipeline → best practices → homework assignment.

The notebooks are committed **without outputs** — run them yourself (`Run → Run All Cells`).

### Kaggle League

Each edition of the Kaggle League is restricted to one model family, and the corresponding notebook is your starting point:

| Edition | Model family | Notebook |
|---|---|---|
| 1 | Linear & logistic regression | `linear_and_logistic_regression.ipynb` |
| 2 | K-nearest neighbours | `knn.ipynb` |
| 3 | Support Vector Machines | `svm.ipynb` |
| 4 | Decision trees & Random Forest | `decision_trees_and_random_forest.ipynb` |

Preprocessing, feature engineering, feature selection, tuning and calibration techniques from `core_ml_techniques.ipynb` are allowed in every edition. Start every submission from [`kaggle_league_starter.ipynb`](notebooks/kaggle_league_starter.ipynb). The full rules are in the lecture slides.

## Data

Most notebooks use datasets bundled with scikit-learn or downloaded by it on first use (cached in `~/scikit_learn_data`, so the first run needs an internet connection). Three real datasets (Bank Marketing, German Credit, Default of Credit Card Clients — all CC BY 4.0 from the UCI repository) and a synthetic Kaggle-format demo ship in `data/` and are documented in [`data/README.md`](data/README.md).

## External Tutorial — Kedro

In addition to the notebooks above, the course covers a project-structuring tutorial
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
