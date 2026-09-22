"""Rebuild `german_credit.csv` from the original UCI "Statlog (German Credit Data)" files.

Usage (from the repository root):

    curl -L -o german.zip "https://archive.ics.uci.edu/static/public/144/statlog+german+credit+data.zip"
    unzip german.zip german.data
    uv run python data/prepare_german_credit.py german.data data/german_credit.csv

The category labels below follow `german.doc` shipped with the dataset (lightly shortened). The label "none" is
deliberately avoided, so that no CSV reader can mistake it for a missing value.
"""

import sys

import pandas as pd

COLUMNS = [
    "checking_status",
    "duration_months",
    "credit_history",
    "purpose",
    "credit_amount",
    "savings_status",
    "employment_since",
    "installment_rate_pct_income",
    "personal_status_sex",
    "other_debtors",
    "residence_since",
    "property",
    "age_years",
    "other_installment_plans",
    "housing",
    "existing_credits_at_bank",
    "job",
    "people_liable_for",
    "telephone",
    "foreign_worker",
    "credit_risk",
]

LABELS = {
    "checking_status": {
        "A11": "< 0 DM",
        "A12": "0 to < 200 DM",
        "A13": ">= 200 DM or salary assignments >= 1 year",
        "A14": "no checking account",
    },
    "credit_history": {
        "A30": "no credits taken / all paid back duly",
        "A31": "all credits at this bank paid back duly",
        "A32": "existing credits paid back duly till now",
        "A33": "delay in paying off in the past",
        "A34": "critical account / other credits elsewhere",
    },
    "purpose": {
        "A40": "car (new)",
        "A41": "car (used)",
        "A42": "furniture/equipment",
        "A43": "radio/television",
        "A44": "domestic appliances",
        "A45": "repairs",
        "A46": "education",
        "A47": "vacation",
        "A48": "retraining",
        "A49": "business",
        "A410": "others",
    },
    "savings_status": {
        "A61": "< 100 DM",
        "A62": "100 to < 500 DM",
        "A63": "500 to < 1000 DM",
        "A64": ">= 1000 DM",
        "A65": "unknown / no savings account",
    },
    "employment_since": {
        "A71": "unemployed",
        "A72": "< 1 year",
        "A73": "1 to < 4 years",
        "A74": "4 to < 7 years",
        "A75": ">= 7 years",
    },
    "personal_status_sex": {
        "A91": "male: divorced/separated",
        "A92": "female: divorced/separated/married",
        "A93": "male: single",
        "A94": "male: married/widowed",
        "A95": "female: single",
    },
    "other_debtors": {"A101": "no other debtors", "A102": "co-applicant", "A103": "guarantor"},
    "property": {
        "A121": "real estate",
        "A122": "building society savings / life insurance",
        "A123": "car or other",
        "A124": "unknown / no property",
    },
    "other_installment_plans": {"A141": "bank", "A142": "stores", "A143": "no other plans"},
    "housing": {"A151": "rent", "A152": "own", "A153": "for free"},
    "job": {
        "A171": "unemployed / unskilled non-resident",
        "A172": "unskilled resident",
        "A173": "skilled employee / official",
        "A174": "management / self-employed / highly qualified",
    },
    "telephone": {"A191": "no", "A192": "yes"},
    "foreign_worker": {"A201": "yes", "A202": "no"},
    "credit_risk": {1: "good", 2: "bad"},
}


def main(source: str, destination: str) -> None:
    df = pd.read_csv(source, sep=" ", header=None, names=COLUMNS)
    for column, mapping in LABELS.items():
        unknown = set(df[column].unique()) - set(mapping)
        if unknown:
            raise ValueError(f"Unmapped codes in {column}: {unknown}")
        df[column] = df[column].map(mapping)
    df.to_csv(destination, index=False)
    print(f"Wrote {destination}: {df.shape[0]} rows, {df.shape[1]} columns")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
