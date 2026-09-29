# Assignment 1 — Association-Rule Classification

This independent graduate Data Mining project builds an interpretable association-rule classifier for a 414-record macroeconomic dataset. The pipeline cleans the data, analyzes correlation, discretizes continuous attributes, mines frequent itemsets with Apriori, creates classification rules, and evaluates predictions on a stratified holdout set.

## Assignment Context

The instructor required three connected parts:

1. remove outliers, calculate Pearson correlations, and perform entropy-based discretization;
2. create a 10% stratified test set, run Apriori, and generate association rules; and
3. classify the test records and calculate accuracy, recall, and precision.

The correlation and confidence thresholds were student-selected values. The portfolio run uses a correlation threshold of `0.70`, confidence threshold of `0.70`, minimum support count of `17`, and random seed of `100`.

## Pipeline

```text
414 raw records
    ↓
Outlier removal (mean ± 2 population standard deviations)
    ↓
309 cleaned records
    ↓
Pearson correlation + entropy-based discretization
    ↓
277 training records + 32 test records
    ↓
Apriori frequent-itemset mining
    ↓
Treat-conclusion rules + deterministic predictions
    ↓
Confusion matrix, accuracy, recall, and precision
```

## Verified Results

| Measure | Result |
|---|---:|
| Raw records | 414 |
| Outliers removed | 105 |
| Cleaned records | 309 |
| Training records | 277 |
| Test records | 32 |
| Frequent itemsets | 719 |
| Final Treat-conclusion rules | 8 |
| True positives / false negatives | 4 / 14 |
| False positives / true negatives | 0 / 14 |
| Accuracy | 56.25% |
| Recall | 22.22% |
| Precision | 100.00% |

These values are recorded in [`outputs/00_run_summary.json`](outputs/00_run_summary.json), [`outputs/19_part2_frequent_itemsets.csv`](outputs/19_part2_frequent_itemsets.csv), and [`outputs/25_part3_metrics.csv`](outputs/25_part3_metrics.csv).

The classifier was conservative: every positive prediction was correct in this holdout sample, but it detected only 4 of 18 positive cases. The result is useful for discussing why precision must be interpreted together with recall.

## Run the Pipeline

```bash
cd assignment1_package
python -m venv .venv
```

Activate the environment, then run:

```bash
python -m pip install -r requirements.txt
python DataMining_Assignment1Pipeline_v1_20260402_FullSubmission.py
```

The program reads [`data/Assignment-1-Data.csv`](data/Assignment-1-Data.csv) and recreates the files in [`outputs/`](outputs/).

## Folder Guide

| Path | Purpose |
|---|---|
| [`DataMining_Assignment1Pipeline_v1_20260402_FullSubmission.py`](DataMining_Assignment1Pipeline_v1_20260402_FullSubmission.py) | Complete executable pipeline |
| [`data/`](data/) | Economy input dataset |
| [`outputs/`](outputs/) | Reproducible CSV and JSON audit trail |
| [`docs/assignment-directions.pdf`](docs/assignment-directions.pdf) | Original instructor directions |
| [`docs/defense-notes.txt`](docs/defense-notes.txt) | Notes used to explain the implementation |
| [`requirements.txt`](requirements.txt) | Python dependencies |

## Skills Demonstrated

- Python and pandas data processing
- NumPy-based numerical work
- population-standard-deviation outlier detection
- Pearson correlation analysis
- entropy and information gain
- class-stratified sampling
- Apriori frequent-itemset mining from scratch
- association-rule generation and deterministic conflict resolution
- confusion-matrix evaluation
- reproducible, inspectable intermediate outputs

## Academic Scope

This is an academic implementation rather than a production forecasting system. The reported metrics describe one documented holdout run with assignment-selected thresholds; they should not be interpreted as evidence of performance on other populations.

