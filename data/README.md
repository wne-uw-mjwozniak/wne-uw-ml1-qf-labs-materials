# Data

Small datasets that ship with the repository, so that the notebooks using them run without an internet connection.

## `german_credit.csv`

| | |
|---|---|
| **Used in** | `notebooks/decision_trees_and_random_forest.ipynb` (Sections 4.5 and 6) |
| **Content** | 1,000 loan applicants of a German bank, 20 features (7 numerical, 13 categorical) and the target `credit_risk` (`good`: 700, `bad`: 300) |
| **Source** | Hofmann, H. (1994). *Statlog (German Credit Data)*. UCI Machine Learning Repository. <https://doi.org/10.24432/C5NC77> |
| **Licence** | [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) |
| **Changes made** | The original file (`german.data`) has no header and stores categories as codes (`A11`, `A34`, ...). We added column names and replaced the codes with the descriptions from the original documentation (`german.doc`). No rows or values were added, removed or altered. |

The file can be regenerated from the original UCI archive with [`prepare_german_credit.py`](prepare_german_credit.py) (instructions in its docstring).

**Cost matrix.** The dataset documentation prescribes asymmetric misclassification costs: classifying a *bad* client as good costs **5**, classifying a *good* client as bad costs **1**.

**Known caveats** — worth keeping in mind when interpreting models built on this data:

- The data is from the early 1970s and amounts are in Deutsche Mark. It is a teaching dataset, not a basis for real credit decisions.
- Bad credits were deliberately **oversampled** (30% of the file; the true default rate was far lower), so predicted probabilities are not real-world probabilities of default.
- Grömping (2019, [*South German Credit Data: Correcting a Widely Used Data Set*](https://www1.beuth-hochschule.de/FB_II/reports/Report-2019-004.pdf)) showed that the UCI documentation mislabels some category codes (for example, `personal_status_sex` does not in fact separate the sexes cleanly); a corrected version is available from UCI as [*South German Credit (UPDATE)*](https://archive.ics.uci.edu/dataset/573/south+german+credit+update). We keep the labels of the original documentation, because this is the version used throughout the literature — be careful with substantive interpretation of individual categories.
- Attributes such as sex, marital status, age or foreign-worker status are protected characteristics; using them in a real credit scoring model would be illegal or heavily restricted in the EU.

## `bank_marketing.csv.gz`

| | |
|---|---|
| **Used in** | `notebooks/eda_and_data_wrangling.ipynb` |
| **Content** | 41,188 phone contacts of a Portuguese bank's telemarketing campaigns (May 2008 – November 2010), 20 features (client data, current and previous campaign, macro-economic context) and the target `y` (subscribed to a term deposit: yes 11.3%) |
| **Source** | Moro, S., Rita, P., Cortez, P. (2014). *Bank Marketing*. UCI Machine Learning Repository. <https://doi.org/10.24432/C5K306> — the file `bank-additional-full.csv` of the archive. Paper: Moro, S., Cortez, P., Rita, P. (2014). A Data-Driven Approach to Predict the Success of Bank Telemarketing. *Decision Support Systems*, 62, 22–31 |
| **Licence** | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| **Changes made** | None — the original semicolon-separated file, gzip-compressed. Read it with `pd.read_csv(path, sep=";")`. |

**Known quirks** (all discussed in the notebook): missing values are coded as `"unknown"`; `pdays == 999` means "not previously contacted" (but see the notebook for a subtlety); `duration` is a leaky feature (it is only known after the call); the rows are ordered by date and the year is not given.

## `credit_card_default.csv.gz`

| | |
|---|---|
| **Used in** | Homework assignments of `eda_and_data_wrangling.ipynb` and `decision_trees_and_random_forest.ipynb` |
| **Content** | 30,000 credit card clients of a Taiwanese bank (April–September 2005), 23 features (credit limit, sex, education, marital status, age, six months of repayment status `PAY_0`–`PAY_6`, bill amounts `BILL_AMT1`–`6`, payment amounts `PAY_AMT1`–`6`) and the target `default_next_month` (1 = default: 22.1%) |
| **Source** | Yeh, I-C. (2016). *Default of Credit Card Clients*. UCI Machine Learning Repository. <https://doi.org/10.24432/C55S3H> |
| **Licence** | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| **Changes made** | Converted from the original Excel file (`.xls`, second header row) to CSV; the `ID` column was dropped and the target column `default payment next month` was renamed to `default_next_month`. No rows or values were altered. |

**Known quirks:** `EDUCATION` and `MARRIAGE` contain undocumented codes (0, 5, 6); the `PAY_*` columns contain the values −2 and 0, which the documentation does not explain (they are commonly read as "no consumption" and "revolving credit / paid minimum"); note the naming gap (`PAY_0`, then `PAY_2`–`PAY_6`).

## `kaggle_demo/`

Two small **synthetic** datasets in the format of a Kaggle competition (`train.csv`, `test.csv`, `sample_submission.csv`), one for a classification task (target `default`, metric ROC AUC) and one for a regression task (target `loss`, metric RMSE). They exist only so that `notebooks/kaggle_league_starter.ipynb` runs end-to-end before the real competitions open; they carry no real information. Generated by [`kaggle_demo/make_demo_data.py`](kaggle_demo/make_demo_data.py) with a fixed seed.
