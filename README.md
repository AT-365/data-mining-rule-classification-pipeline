# Data Mining Rule-Classification Pipeline

[![Tests](https://github.com/AT-365/data-mining-rule-classification-pipeline/actions/workflows/tests.yml/badge.svg)](https://github.com/AT-365/data-mining-rule-classification-pipeline/actions/workflows/tests.yml)

An end-to-end Python data-mining project that transforms raw tabular data into an evaluated, interpretable association-rule classifier. The repository now includes the complete portfolio-ready pipeline in [`data_mining_pipeline.py`](data_mining_pipeline.py).

## Why this project matters

This project demonstrates more than model fitting. It covers data validation, preprocessing, feature analysis, discretization, association-rule mining, rule selection, prediction, evaluation, and auditable output generation. The result is interpreted honestly: the classifier made highly reliable positive predictions, but missed many positive cases.

## Pipeline

1. Load and validate a 414-record CSV dataset.
2. Remove statistical outliers using population mean and standard deviation rules.
3. Evaluate Pearson correlations at a 0.70 threshold.
4. Convert continuous variables into binary intervals using entropy-based split points.
5. Create a class-stratified 10% test set with a fixed random seed.
6. Mine frequent itemsets with an Apriori implementation.
7. Generate and filter association rules using support, confidence, balance, and validity criteria.
8. Apply deterministic conflict resolution to generate predictions.
9. Produce confusion-matrix metrics and 27 report-ready audit files.

## Verified results

| Measure | Result |
|---|---:|
| Raw records | 414 |
| Outliers removed | 105 |
| Cleaned records | 309 |
| Test records | 32 |
| Frequent itemsets | 719 |
| Final Treat-conclusion rules | 8 |
| Accuracy | 56.25% |
| Recall | 22.22% |
| Precision | 100.00% |

Confusion matrix: **TP 4, FN 14, FP 0, TN 14**.

The model was conservative: every positive prediction was correct in the held-out sample, but it identified only 4 of 18 positive cases. That tradeoff makes the project useful for discussing class coverage, threshold selection, and why one favorable metric should never be reported in isolation.

## Code highlights

- Input validation and portable command-line arguments
- Statistical outlier detection and correlation analysis
- Entropy and information-gain calculations
- Custom Apriori frequent-itemset mining
- Association-rule generation and deterministic conflict resolution
- Stratified holdout evaluation
- Reproducible CSV and JSON audit outputs

## Repository structure

| Path | Purpose |
|---|---|
| [`data_mining_pipeline.py`](data_mining_pipeline.py) | Complete executable analysis pipeline |
| [`requirements.txt`](requirements.txt) | Python dependencies |
| [`DATASET.md`](DATASET.md) | Input schema and dataset availability |
| [`tests/test_pipeline.py`](tests/test_pipeline.py) | Synthetic unit tests for core calculations and validation |
| [`docs/PUBLICATION_NOTES.md`](docs/PUBLICATION_NOTES.md) | Public-release boundaries |

## Run locally

```bash
python -m venv .venv
```

Activate the environment, then install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the pipeline with an eligible CSV file:

```bash
python data_mining_pipeline.py \
  --input path/to/input.csv \
  --output-dir outputs
```

The original course dataset is not distributed. See [`DATASET.md`](DATASET.md) for the required input schema.

## Automated tests

The public test suite uses small synthetic inputs rather than the protected course dataset. It checks input validation, entropy, Apriori support counting, invalid itemset detection, and confusion-matrix metrics.

```bash
python -m unittest discover -s tests -v
```

GitHub Actions runs the same tests automatically after each push and pull request.

## Technologies and methods

- Python, pandas, and NumPy
- CSV ingestion and structured exports
- Outlier detection and Pearson correlation
- Entropy-based discretization
- Apriori frequent-itemset mining
- Association-rule classification
- Class-stratified train/test splitting
- Confusion matrices, accuracy, recall, and precision

## What I learned

- A reproducible pipeline needs explicit configuration, deterministic sampling, and auditable intermediate outputs.
- Perfect precision can coexist with poor recall; the operational cost of false negatives matters.
- Support and confidence thresholds affect both rule quality and coverage.
- Interpretable rules make model behavior easier to inspect, but do not eliminate the need for rigorous evaluation.

## Repository scope

This public portfolio version includes the complete analysis code with portable file handling. The original assignment specification, professor-provided dataset, submitted report, and generated row-level outputs remain private to protect course materials and data. See [Publication Notes](docs/PUBLICATION_NOTES.md).

## Interview summary

> I built a reproducible Python pipeline that cleaned a 414-record dataset, performed feature analysis and entropy-based discretization, mined association rules, and evaluated a rule-based classifier on a stratified holdout set. The most important result was not just the 100% precision—it was recognizing that recall was only 22.22%, so the model was trustworthy when it predicted positive but too conservative for broad detection.

---

**Project type:** Completed graduate academic project  
**Course:** CSCI 7434 — Data Mining, Georgia Southern University  
**Author:** Autenia Murray
