# Data Mining Rule-Classification Pipeline

An end-to-end academic data-mining case study that turns a raw tabular dataset into an evaluated, interpretable rule-based classifier.

## Why this project matters

This project demonstrates more than model fitting. It covers the full analytical workflow: data validation, preprocessing, feature analysis, discretization, association-rule mining, rule selection, prediction, and evaluation. The final model was intentionally interpreted honestly: it made highly reliable positive predictions, but missed many positive cases.

## Pipeline

1. Loaded and validated a 414-record CSV dataset.
2. Removed 105 statistical outliers using population mean and standard deviation rules.
3. Evaluated Pearson correlations at a 0.70 threshold.
4. Converted continuous variables into categorical intervals using entropy-based split points.
5. Created a class-stratified 10% test set with a fixed random seed.
6. Generated frequent itemsets and association rules.
7. Selected Treat-conclusion rules using support, confidence, imbalance, and validity criteria.
8. Applied deterministic conflict resolution to generate predictions.
9. Produced confusion-matrix metrics and report-ready audit files.

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

The model was conservative: every positive prediction was correct in the held-out sample, but it identified only 4 of 18 positive cases. That tradeoff makes the project useful for discussing threshold selection, class coverage, and why a single favorable metric should never be reported in isolation.

## Technologies and methods

- Python
- pandas and NumPy
- CSV-based data ingestion and exports
- Outlier detection
- Pearson correlation analysis
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

This public version is a portfolio case study. The original assignment specification, professor-provided dataset, submitted report, and source code are intentionally withheld to protect course materials and academic integrity. See [Publication Notes](docs/PUBLICATION_NOTES.md).

## Interview summary

> I built a reproducible Python pipeline that cleaned a 414-record dataset, performed feature analysis and entropy-based discretization, mined association rules, and evaluated a rule-based classifier on a stratified holdout set. The most important result was not just the 100% precision—it was recognizing that recall was only 22.22%, so the model was trustworthy when it predicted positive but too conservative for broad detection.

---

**Project type:** Completed graduate academic project  
**Course:** CSCI 7434 — Data Mining, Georgia Southern University  
**Author:** Autenia Murray
