"""Generate the small synthetic datasets in Kaggle-competition format used by `notebooks/kaggle_league_starter.ipynb`.

Two tasks, each with train.csv / test.csv / sample_submission.csv:
  classification/  target `default` (0/1, ~20% positives), metric ROC AUC
  regression/      target `loss` (continuous), metric RMSE

The files mimic the traps of real competition data: an id column, mixed numerical and categorical
features, missing values, an irrelevant feature and a rare category. Run from the repository root:

    uv run python data/kaggle_demo/make_demo_data.py
"""

from pathlib import Path

import numpy as np
import pandas as pd

OUT = Path(__file__).parent
rng = np.random.default_rng(2026)
N_TRAIN, N_TEST = 3000, 1500


def make_features(n):
    income = rng.lognormal(mean=10.5, sigma=0.5, size=n)
    age = rng.integers(21, 70, size=n)
    debt_ratio = np.clip(rng.beta(2, 5, size=n) * 1.5, 0, 2)
    n_loans = rng.poisson(1.2, size=n)
    region = rng.choice(["north", "south", "east", "west", "islands"], size=n, p=[0.3, 0.3, 0.2, 0.19, 0.01])
    employment = rng.choice(["employed", "self-employed", "unemployed", "retired"], size=n, p=[0.6, 0.2, 0.1, 0.1])
    noise = rng.normal(size=n)  # irrelevant feature
    df = pd.DataFrame(
        {
            "income": income.round(0),
            "age": age,
            "debt_ratio": debt_ratio.round(3),
            "n_loans": n_loans,
            "region": region,
            "employment": employment,
            "random_score": noise.round(3),
        }
    )
    # Missing values in two columns
    df.loc[rng.random(n) < 0.08, "income"] = np.nan
    df.loc[rng.random(n) < 0.05, "employment"] = np.nan
    return df


def latent(df):
    emp = df["employment"].map({"employed": -0.5, "self-employed": 0.2, "unemployed": 1.0, "retired": 0.0}).fillna(0.3)
    inc = np.log(df["income"].fillna(df["income"].median()))
    return -1.6 + 2.2 * df["debt_ratio"] - 0.8 * (inc - 10.5) + 0.35 * df["n_loans"] + emp - 0.01 * (df["age"] - 45)


for task in ("classification", "regression"):
    (OUT / task).mkdir(exist_ok=True)
    features = make_features(N_TRAIN + N_TEST)
    z = latent(features) + rng.normal(0, 0.7, size=len(features))
    if task == "classification":
        target = (rng.random(len(features)) < 1 / (1 + np.exp(-(z - 0.9)))).astype(int)
        target_name = "default"
    else:
        target = (1000 * np.exp(0.6 * z) + rng.normal(0, 300, size=len(features))).round(2)
        target_name = "loss"
    features.insert(0, "id", np.arange(1, len(features) + 1))
    train = features.iloc[:N_TRAIN].assign(**{target_name: target[:N_TRAIN]})
    test = features.iloc[N_TRAIN:]
    train.to_csv(OUT / task / "train.csv", index=False)
    test.to_csv(OUT / task / "test.csv", index=False)
    constant = 0.5 if task == "classification" else train[target_name].mean()
    sample = pd.DataFrame({"id": test["id"], target_name: constant})
    sample.to_csv(OUT / task / "sample_submission.csv", index=False)
    print(f"{task}: train {train.shape}, test {test.shape}, target mean {train[target_name].mean():.3f}")
