# Kaggle League 2026/27 - team repository template

Machine Learning in Finance I (2400-QFU1MLF). Every team keeps **one private GitHub repository** for all eight
competitions of the League. This folder is its template: one subfolder per competition, each a separate
[uv](https://docs.astral.sh/uv/) project with its own environment, pinned to exactly the package versions of the course.

| Folder | Edition | Dataset | Kaggle competition |
|---|---|---|---|
| `e1_linear_claims/` | 1 - Linear & logistic regression | Travel Claims (classification, ROC AUC) | `ml1-qf-2027-e1-linear-claims` |
| `e1_linear_salary/` | 1 - Linear & logistic regression | Developer Salary (regression, RMSE) | `ml1-qf-2027-e1-linear-salary` |
| `e2_knn_claims/` | 2 - K-nearest neighbours | Travel Claims (classification, ROC AUC) | `ml1-qf-2027-e2-knn-claims` |
| `e2_knn_salary/` | 2 - K-nearest neighbours | Developer Salary (regression, RMSE) | `ml1-qf-2027-e2-knn-salary` |
| `e3_svm_claims/` | 3 - Support Vector Machines | Travel Claims (classification, ROC AUC) | `ml1-qf-2027-e3-svm-claims` |
| `e3_svm_salary/` | 3 - Support Vector Machines | Developer Salary (regression, RMSE) | `ml1-qf-2027-e3-svm-salary` |
| `e4_trees_claims/` | 4 - Decision trees & Random Forest | Travel Claims (classification, ROC AUC) | `ml1-qf-2027-e4-trees-claims` |
| `e4_trees_salary/` | 4 - Decision trees & Random Forest | Developer Salary (regression, RMSE) | `ml1-qf-2027-e4-trees-salary` |

Each folder contains:

```text
e1_linear_claims/
├── pyproject.toml          # the folder's own uv project (course package versions, pinned)
├── uv.lock                 # exact versions of everything - do not delete
├── .python-version         # 3.12
├── e1_linear_claims.ipynb  # the starter notebook, already set to this competition
├── data/                   # train.csv, test.csv, sample_submission.csv - git-ignored, never committed
└── submission.csv          # written by the notebook; committed together with it
```

## One-time setup (before Sunday 25.10.2026, together with the team registration)

1. Copy this folder out of the course repository and turn it into a new repository (**not** a fork - forks of a public
   repository are always public):

   ```bash
   cp -r kaggle_league_template ~/ml1-kaggle-league-surname1-surname2
   cd ~/ml1-kaggle-league-surname1-surname2
   git init && git add . && git commit -m "Kaggle League template"
   gh repo create ml1-kaggle-league-surname1-surname2 --private --source . --push   # or create it on github.com
   ```

2. On GitHub: *Settings -> Collaborators -> Add people*: add your teammate and the lecturer, GitHub user
   **michaelwozniak**.
3. Put the repository link into the team-registration e-mail.

The repository stays **private** until the League has ended (sharing code between teams is sanctioned); afterwards you
may make it public, e.g. as a portfolio project.

## Workflow for every competition

```bash
cd e1_linear_claims
uv sync                                   # creates .venv with the course versions
# download train.csv, test.csv, sample_submission.csv into data/
uv run jupyter lab e1_linear_claims.ipynb # or open the folder in VS Code and pick .venv as the kernel
```

1. Develop in the notebook (it already knows its edition, task and data folder). `uv add <package>` inside the folder
   adds a package to this competition only; the other folders are not affected.
2. For the submission you want graded: **Restart Kernel and Run All** - this writes `submission.csv` and prints its MD5.
3. Commit the notebook, `submission.csv`, `pyproject.toml` and `uv.lock`; push.
4. Upload exactly that `submission.csv` to Kaggle with the description

   ```text
   commit <short commit hash> md5 <MD5 printed by the notebook>
   ```

   (`git rev-parse --short HEAD` prints the hash). Kaggle timestamps the description - this is the proof that the
   code existed before the deadline. Later commits do not matter for that submission.
5. Before the deadline, **select** that submission on Kaggle (one per competition).

## How the lecturer checks a submission

```bash
git clone <your repository> && cd <repository> && git checkout <commit from the description>
cd e1_linear_claims && uv sync
# the competition files are copied into data/
uv run jupyter nbconvert --to notebook --execute e1_linear_claims.ipynb --output checked.ipynb
md5 submission.csv            # must equal the md5 in the Kaggle description
```

Missing folder or commit, a notebook that does not run after `uv sync`, an MD5 that does not match, or predictions
from a model outside the edition's family -> 0 points for that leaderboard (full rules: lecture slides 11-18 and the
Rules tab of every competition).
