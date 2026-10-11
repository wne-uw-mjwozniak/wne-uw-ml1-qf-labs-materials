"""Generate the small synthetic datasets in Kaggle-competition format used by `notebooks/kaggle_league_starter.ipynb`.

Two tasks, each with train.csv / test.csv / sample_submission.csv:
  classification/  target `default` (0/1, ~5 % positives), metric ROC AUC - mirrors the claims data:
                   a mostly-missing categorical whose missingness is informative, a high-cardinality category,
                   an integer column that is really a code, no multi-select columns
  regression/      target `loss` (positive, skewed), metric RMSE - mirrors the salary data:
                   two semicolon-separated multi-select columns, an ordinal column stored as text,
                   numeric columns with ~30 % informative missingness

Both carry an id column, an irrelevant feature and a rare category. The positive share of the classification task
(~5 %) is deliberately higher than the 1.7 % of the claims data: with 3,000 rows, 1.7 % would leave ~10 positives
per fold. Run from the repository root:

    uv run python data/kaggle_demo/make_demo_data.py
"""

from pathlib import Path

import numpy as np
import pandas as pd

OUT = Path(__file__).parent
rng = np.random.default_rng(2026)
N_TRAIN, N_TEST = 3000, 1500


def common_features(n):
    income = rng.lognormal(mean=10.5, sigma=0.5, size=n)
    age = rng.integers(21, 70, size=n)
    debt_ratio = np.clip(rng.beta(2, 5, size=n) * 1.5, 0, 2)
    n_loans = rng.poisson(1.2, size=n)
    region = rng.choice(["north", "south", "east", "west", "islands"], size=n, p=[0.3, 0.3, 0.2, 0.19, 0.01])
    employment = rng.choice(["employed", "self-employed", "unemployed", "retired"], size=n, p=[0.6, 0.2, 0.1, 0.1])
    df = pd.DataFrame(
        {
            "income": income.round(0),
            "age": age,
            "debt_ratio": debt_ratio.round(3),
            "n_loans": n_loans,
            "region": region,
            "employment": employment,
            "random_score": rng.normal(size=n).round(3),  # irrelevant feature
        }
    )
    df.loc[rng.random(n) < 0.08, "income"] = np.nan
    df.loc[rng.random(n) < 0.05, "employment"] = np.nan
    return df


def multiselect(n, items, probs):
    items = np.array(items)
    chosen = rng.random((n, len(items))) < np.array(probs)
    return [";".join(sorted(items[row])) if row.any() else np.nan for row in chosen]  # sorted, like the real data


def classification_features(n):
    df = common_features(n)
    df["segment"] = rng.choice(["retail", "premium", "private banking"], size=n, p=[0.7, 0.25, 0.05])
    df["branch_code"] = rng.integers(1000, 1120, size=n)  # 120 branches: an integer column that is really a category
    df["channel_id"] = rng.choice([1, 2, 3], size=n, p=[0.6, 0.3, 0.1])  # a small integer code
    # mostly missing, and the missingness is informative: segment is recorded mainly for riskier clients
    recorded = rng.random(n) < np.where(df["debt_ratio"] > 1.0, 0.6, 0.2)
    df.loc[~recorded, "segment"] = np.nan
    return df


def regression_features(n):
    df = common_features(n)
    df["education"] = rng.choice(
        ["primary", "secondary", "bachelor", "master", "doctorate"], size=n, p=[0.05, 0.3, 0.4, 0.2, 0.05]
    )
    df["products"] = multiselect(
        n,
        [
            "current account",
            "savings",
            "mortgage",
            "credit card",
            "car loan",
            "overdraft",
            "fx account",
            "brokerage",
            "insurance",
            "crypto",
        ],
        [0.6, 0.45, 0.25, 0.4, 0.15, 0.2, 0.05, 0.08, 0.3, 0.02],
    )
    df["channels"] = multiselect(n, ["branch", "web", "mobile app", "phone", "advisor"], [0.5, 0.7, 0.6, 0.2, 0.1])
    df["years_with_bank"] = rng.integers(0, 30, size=n).astype(float)
    # informative missingness: tenure is unknown mostly for new, riskier clients
    df.loc[rng.random(n) < np.where(df["debt_ratio"] > 1.0, 0.5, 0.2), "years_with_bank"] = np.nan
    return df


def latent(df):
    emp = df["employment"].map({"employed": -0.5, "self-employed": 0.2, "unemployed": 1.0, "retired": 0.0}).fillna(0.3)
    inc = np.log(df["income"].fillna(df["income"].median()))
    z = -1.6 + 2.2 * df["debt_ratio"] - 0.8 * (inc - 10.5) + 0.35 * df["n_loans"] + emp - 0.01 * (df["age"] - 45)
    if "education" in df:  # regression task
        edu = df["education"].map({"primary": 0, "secondary": 1, "bachelor": 2, "master": 3, "doctorate": 4})
        products = df["products"].fillna("")
        z = (
            z
            - 0.25 * edu
            + 0.9 * products.str.contains("overdraft")
            - 0.15 * products.map(lambda s: len(s.split(";")) if s else 0)
        )
        z = z + 0.4 * df["years_with_bank"].isna() - 0.02 * df["years_with_bank"].fillna(0)
    else:  # classification task
        z = z + 0.5 * df["segment"].isna() + 0.3 * (df["channel_id"] == 3)
    return z


for task, make in (("classification", classification_features), ("regression", regression_features)):
    (OUT / task).mkdir(exist_ok=True)
    features = make(N_TRAIN + N_TEST)
    z = latent(features) + rng.normal(0, 0.7, size=len(features))
    if task == "classification":
        target = (rng.random(len(features)) < 1 / (1 + np.exp(-(z - 3.5)))).astype(int)  # rare positives (~5 %)
        target_name = "default"
    else:
        target = (1000 * np.exp(0.6 * z + rng.normal(0, 0.3, size=len(features)))).round(2)  # positive, skewed
        target_name = "loss"
    features.insert(0, "id", np.arange(1, len(features) + 1))
    train = features.iloc[:N_TRAIN].assign(**{target_name: target[:N_TRAIN]})
    test = features.iloc[N_TRAIN:]
    train.to_csv(OUT / task / "train.csv", index=False)
    test.to_csv(OUT / task / "test.csv", index=False)
    constant = (
        round(float(train[target_name].mean()), 4)
        if task == "classification"
        else round(float(train[target_name].mean()), 2)
    )
    sample = pd.DataFrame({"id": test["id"], target_name: constant})
    sample.to_csv(OUT / task / "sample_submission.csv", index=False)
    print(f"{task}: train {train.shape}, test {test.shape}, target mean {train[target_name].mean():.3f}")
