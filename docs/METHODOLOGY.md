# Methodology

## Objective

Build an interpretable binary classifier from tabular data and retain enough intermediate evidence to audit every major transformation.

## Data preparation

The pipeline began with 414 records. Numeric outliers were identified using population statistics and removed before downstream analysis, leaving 309 records. Pearson correlations were then evaluated against a 0.70 threshold; no pair exceeded that cutoff.

Continuous variables were discretized with entropy-based split selection. This converted numeric measurements into categorical intervals suitable for frequent-itemset and rule mining.

## Evaluation design

A fixed random seed and class-stratified sampling were used to create a 10% holdout set. The test set contained 32 records: 18 positive and 14 negative examples.

## Rule mining and prediction

The workflow generated frequent itemsets and association rules, then filtered the rules for validity, minimum support, prediction target, and confidence. A minimum support count of 17 was used because the initially tested count of 20 produced no usable target-prediction rules.

The selected rule set contained eight target-conclusion rules. Prediction used a deterministic conflict-resolution strategy so repeated runs produced the same result.

## Reproducibility controls

- Centralized configuration values
- Fixed random seed
- Population-standard-deviation setting documented explicitly
- Intermediate CSV exports for calculations and decisions
- Separate training and holdout evaluation
- Confusion-matrix reporting rather than accuracy alone

## Scope note

This document summarizes the workflow at a portfolio level. It intentionally omits the professor's assignment instructions, the private dataset, implementation code, and submitted academic artifacts.
