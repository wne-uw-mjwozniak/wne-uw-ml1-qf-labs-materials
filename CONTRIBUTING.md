# Contributing / Development

This file is for people who **edit** the materials. Students only need [README.md](README.md) and [SETUP.md](SETUP.md).

## Environment

```bash
uv sync --dev          # the course environment plus the development tools
uv run pre-commit install
```

## Pre-commit hooks

This project uses [pre-commit](https://pre-commit.com/) to enforce code quality on every commit. The following hooks run automatically on `git commit`:

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

## Linting rules

Ruff is configured in `pyproject.toml` with:

- **Line length:** 120 characters
- **Rules:** `E` (pycodestyle errors), `F` (pyflakes), `W` (pycodestyle warnings), `I` (isort)
- **Notebook-specific ignores:** `E402` (import-not-at-top, expected in cells), `E501` (line-too-long, alignment-heavy print statements)

## Editing notebooks

- Notebooks are committed **without outputs**. Before committing, execute the notebook top-to-bottom in a clean kernel and check that no cell produces an error or a warning, then clear the outputs. A convenient check from the command line:

  ```bash
  uv run jupyter nbconvert --to notebook --execute notebooks/<name>.ipynb --output-dir /tmp/nb-check
  ```

- Each notebook owns its topic. Do not re-teach material that lives in another notebook — link to it instead (see the "Used in" column of the notebook table in the README for the intended place of every topic).
- Do not write interpretive claims about results into markdown cells before seeing the executed output.
- Prefer datasets bundled in `data/` over live downloads; document every new dataset (source, licence, changes made) in `data/README.md`.

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

Adding a dependency: `uv add <package>` (or `uv add --dev <package>`), then commit both `pyproject.toml` and `uv.lock`. Do not run `uv lock --upgrade` casually — every student's environment is pinned to the lock file.
