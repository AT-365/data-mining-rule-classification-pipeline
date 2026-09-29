# Data Mining Classification Portfolio

[![portfolio-checks](https://github.com/AT-365/data-mining-rule-classification-pipeline/actions/workflows/tests.yml/badge.svg)](https://github.com/AT-365/data-mining-rule-classification-pipeline/actions/workflows/tests.yml)

A graduate Data Mining portfolio containing two independent, from-scratch Python projects: an association-rule classifier and an interactive ID3/Naive Bayes classification pipeline.

> **Project type:** Two independent graduate academic projects  
> **Portfolio focus:** Reproducible preprocessing, interpretable classification, transparent evaluation, and calculation-level evidence  
> **Author:** Autenia Murray

## Why This Project Matters

This repository demonstrates practical skills relevant to entry-level data, analytics, and machine-learning roles:

- translating algorithm specifications into complete Python workflows;
- cleaning, transforming, and validating tabular data;
- implementing Apriori, ID3, and Naive Bayes without classifier libraries;
- exposing intermediate calculations for review instead of reporting only final scores;
- evaluating models honestly with confusion matrices, accuracy, recall, and precision;
- designing reproducible command-line programs with validated user input; and
- documenting academic constraints and modeling limitations clearly.

## Project Overview

The repository contains two separate assignments completed in the same graduate Data Mining course. They share a course context but are not phases of the same project.

## Assignment 1 and Assignment 2

### Assignment 1 — Association-Rule Classification

Assignment 1 processes a 414-record macroeconomic dataset through outlier removal, Pearson correlation analysis, entropy-based discretization, a stratified train/test split, Apriori mining, association-rule generation, prediction, and evaluation.

The final holdout run produced 100% precision and 22.22% recall. That contrast is presented directly because it demonstrates the importance of interpreting model coverage alongside prediction reliability.

Start with [`assignment1_package/README.md`](assignment1_package/README.md).

### Assignment 2 — From-Scratch ID3 and Naive Bayes

Assignment 2 provides an interactive choice between ID3 and Naive Bayes. ID3 includes user-controlled pre- and post-pruning; Naive Bayes handles categorical and continuous attributes and applies Laplace smoothing when zero-frequency cases are detected.

The official evaluation emphasized live program execution and explanation during a one-to-one Zoom defense. Test-set use during ID3 post-pruning was an explicit instructor requirement.

Start with [`assignment2_package/README.md`](assignment2_package/README.md).

## Verified Portfolio Metrics

| Metric | Value |
|---|---:|
| Independent projects | 2 |
| Classifiers implemented from scratch | 3 |
| Assignment 1 raw records | 414 |
| Assignment 1 cleaned records | 309 |
| Assignment 1 frequent itemsets | 719 |
| Assignment 1 final Treat-conclusion rules | 8 |
| Assignment 1 accuracy | 56.25% |
| Assignment 1 precision / recall | 100.00% / 22.22% |
| Assignment 2 training / test records per classifier | 365 / 44 |
| Assignment 2 ID3 accuracy | 47.73% |
| Assignment 2 Naive Bayes accuracy | 45.45% |
| Valid Assignment 2 calculation workbooks | 37 |
| Automated repository checks | 8 |

Metrics are sourced from committed run summaries and output files, not reconstructed from memory.

## What I Built

- a reproducible association-rule classification pipeline with 26 CSV audit outputs;
- entropy-based discretization and Apriori frequent-itemset mining;
- deterministic association-rule prediction and binary evaluation;
- an interactive ID3 implementation with pre-pruning, post-pruning, and rule extraction;
- a Naive Bayes implementation with categorical probabilities, Gaussian components, and Laplace smoothing;
- 37 validated Excel calculation workbooks across the two Assignment 2 runs;
- multi-format generated reports and live-defense notes; and
- automated checks for code integrity, documented metrics, Office-file validity, and repository structure.

## Quick Start

Run Assignment 1:

```bash
cd assignment1_package
python -m pip install -r requirements.txt
python DataMining_Assignment1Pipeline_v1_20260402_FullSubmission.py
```

Run Assignment 2:

```bash
cd assignment2_package
python -m pip install -r requirements.txt
python DataMining_Assignment2Pipeline_v1_20260506_FullSubmission.py
```

Use a virtual environment for either project. Assignment 2 requires Python 3.10 or newer.

Run the repository checks from the root:

```bash
python -m unittest discover -s tests -v
```

## Repository Map

| Path | Purpose |
|---|---|
| [`assignment1_package/`](assignment1_package/) | Association-rule classification project |
| [`assignment1_package/data/`](assignment1_package/data/) | Assignment 1 input data |
| [`assignment1_package/outputs/`](assignment1_package/outputs/) | Assignment 1 CSV/JSON audit trail |
| [`assignment2_package/`](assignment2_package/) | ID3 and Naive Bayes project |
| [`assignment2_package/data/`](assignment2_package/data/) | Assignment 2 training/test datasets |
| [`assignment2_package/outputs/`](assignment2_package/outputs/) | Valid ID3 and Naive Bayes calculation workbooks |
| [`assignment2_package/reports/`](assignment2_package/reports/) | Generated reports in five formats |
| [`assignment2_package/defense_notes/`](assignment2_package/defense_notes/) | Live-defense reference materials |
| [`tests/`](tests/) | Automated portfolio-integrity checks |

## Design Highlights

### Reproducible Association-Rule Pipeline

Assignment 1 uses a fixed random seed, records selected thresholds, and exports each major transformation. A reviewer can trace the work from the raw data through final predictions and metrics.

### Interpretable Classification

The ID3 tree becomes readable IF-THEN rules. The association classifier also retains the rules applied to each record. Both approaches make the prediction path inspectable.

### Calculation-Level Evidence

Assignment 2 generates workbooks for dataset inspection, entropy and gain, pruning decisions, probability tables, class scores, predictions, confusion matrices, and final metrics.

### Honest Evaluation

The repository reports modest accuracy and uneven class performance rather than presenting only favorable values. These results support discussion of threshold sensitivity, class coverage, and the difference between academic implementation and production validation.

## Technologies & Methods

- **Python:** end-to-end pipeline development and command-line interaction
- **pandas and NumPy:** tabular processing and numerical calculations
- **openpyxl:** Excel output generation
- **python-docx and ReportLab:** generated DOCX and PDF reports
- **Statistical preprocessing:** outlier removal and Pearson correlation
- **Feature engineering:** entropy-based discretization
- **Association analysis:** Apriori, support, confidence, and rule filtering
- **Decision trees:** ID3, information gain, pre-pruning, and post-pruning
- **Probabilistic classification:** priors, conditional probabilities, Gaussian density, and Laplace smoothing
- **Evaluation:** confusion matrices, accuracy, precision, and recall
- **Git/GitHub:** version control and automated repository checks

## How to Review This Project

For a quick employer review:

1. Read this README.
2. Open the [Assignment 1 overview](assignment1_package/README.md) and inspect its run summary and final metrics.
3. Open the [Assignment 2 overview](assignment2_package/README.md) and compare the ID3 and Naive Bayes results.
4. Review the two main Python files to see the from-scratch algorithms.
5. Inspect the generated reports and selected calculation workbooks.
6. Review [`tests/test_portfolio.py`](tests/test_portfolio.py) for the automated evidence checks.

## Academic Scope and Attribution

This repository is a historical portfolio artifact based on work completed independently by Autenia Murray for graduate Data Mining coursework at Georgia Southern University.

The original Assignment 2 directions included classmates' individual presentation times. The public copy was redacted to protect their privacy. No collaborators are claimed for either project.

These programs demonstrate algorithm understanding and reproducible execution. They are not presented as production systems, and the documented course requirements are distinguished from general production practices.

## What I Learned

- **A strong metric can hide an important weakness.** Assignment 1 achieved perfect precision in its holdout sample, but low recall showed that many positive cases were missed.
- **From-scratch implementation makes assumptions visible.** Writing entropy, information gain, pruning, smoothing, and Gaussian calculations directly made each design choice inspectable.
- **Intermediate evidence improves technical communication.** Calculation-level outputs supported debugging and made the live defense easier to explain.
- **Academic constraints should be documented plainly.** The professor-required post-pruning procedure is preserved, while the README explains how production validation would differ.
