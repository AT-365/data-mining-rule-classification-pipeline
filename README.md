# Data Mining Rule-Classification Pipeline

<<<<<<< HEAD
## Purpose

This folder contains the Python pipeline for Data Mining Assignment 2. The program lets the user choose either ID3 or Naive Bayes, then runs the selected method from start to finish.
=======
[![Tests](https://github.com/AT-365/data-mining-rule-classification-pipeline/actions/workflows/tests.yml/badge.svg)](https://github.com/AT-365/data-mining-rule-classification-pipeline/actions/workflows/tests.yml)

An end-to-end Python data-mining project that transforms raw tabular data into an evaluated, interpretable association-rule classifier. The repository now includes the complete portfolio-ready pipeline in [`data_mining_pipeline.py`](data_mining_pipeline.py).

## Why this project matters
>>>>>>> parent of 4508527 (Add files via upload)

This project demonstrates more than model fitting. It covers data validation, preprocessing, feature analysis, discretization, association-rule mining, rule selection, prediction, evaluation, and auditable output generation. The result is interpreted honestly: the classifier made highly reliable positive predictions, but missed many positive cases.

## Pipeline

<<<<<<< HEAD
```text
data-mining-rule-classification-pipeline/
|-- dm_assignment2_package/
|   |-- Assignment2_DefenseNotes_Bayes.pdf
|   |-- Assignment2_DefenseNotes_ID3.pdf
|   |-- Assignment2_Report_Bayes.pdf
|   |-- Assignment2_Report_ID3.pdf
|   |-- DM-Assignment 2-Directions.pdf
|   |-- DataMining_Assignment2Pipeline_v1_20260506_FullSubmission.py
|   |-- DataMining_PresentationScript_v1_20260506_Assignments1and2.pdf
|   |-- bayes/
|   |-- data/
|   |   |-- A2--ID3-Training set.csv
|   |   |-- A2--ID3-TEST set.csv
|   |   |-- A2--Bayes-Training set.csv
|   |   `-- A2--Bayes-TEST set.csv
|   |-- id3/
|   |-- FILES_MANIFEST.txt
|   `-- README.md
|-- requirements.txt
`-- README.md
```

## Setup

Prerequisites on any computer:

- Python 3.10 or newer must be installed first.
- `pip` must be available in that Python installation.
- After Python is installed, open a terminal in the project folder and run `python -m pip install -r requirements.txt`.

If `python` does not work on a computer, try:

```powershell
py -m pip install -r requirements.txt
py dm_assignment2_package/DataMining_Assignment2Pipeline_v1_20260506_FullSubmission.py
```

1. Open the full folder in VS Code or another development environment.
2. Open a terminal in the project folder.
3. Create and activate a fresh virtual environment on that computer.

Important:

- Do not rely on a copied `.venv` from another machine. Python virtual environments contain machine-specific paths and often break when moved.
- Use Python 3.10 or newer.
- Install the packages from `requirements.txt` before running the pipeline.
=======
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
>>>>>>> parent of 4508527 (Add files via upload)

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
<<<<<<< HEAD
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
=======
>>>>>>> parent of 4508527 (Add files via upload)
```

Activate the environment, then install the dependencies:

```bash
<<<<<<< HEAD
python3 -m venv .venv
source .venv/bin/activate
=======
>>>>>>> parent of 4508527 (Add files via upload)
python -m pip install -r requirements.txt
```

Run the pipeline with an eligible CSV file:

<<<<<<< HEAD
```powershell
python dm_assignment2_package/DataMining_Assignment2Pipeline_v1_20260506_FullSubmission.py
```

If the required packages are missing, the script now stops immediately and prints a setup message instead of failing later during Excel, DOCX, or PDF export.

It also checks that all four assignment CSV files are present before asking for user input.

Recommended first-time setup on another computer:

```powershell
python -m pip install -r requirements.txt
python dm_assignment2_package/DataMining_Assignment2Pipeline_v1_20260506_FullSubmission.py
=======
```bash
python data_mining_pipeline.py \
  --input path/to/input.csv \
  --output-dir outputs
>>>>>>> parent of 4508527 (Add files via upload)
```

The original course dataset is not distributed. See [`DATASET.md`](DATASET.md) for the required input schema.

## Automated tests

<<<<<<< HEAD
## Example Inputs

### ID3

```text
Classifier choice: ID3
Show live section output: yes
T1: 0.80
g: 0.010
```

### Naive Bayes
=======
The public test suite uses small synthetic inputs rather than the protected course dataset. It checks input validation, entropy, Apriori support counting, invalid itemset detection, and confusion-matrix metrics.

```bash
python -m unittest discover -s tests -v
```

GitHub Actions runs the same tests automatically after each push and pull request.
>>>>>>> parent of 4508527 (Add files via upload)

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

<<<<<<< HEAD
This shows that files are being generated during the live run.
=======
## Interview summary
>>>>>>> parent of 4508527 (Add files via upload)

> I built a reproducible Python pipeline that cleaned a 414-record dataset, performed feature analysis and entropy-based discretization, mined association rules, and evaluated a rule-based classifier on a stratified holdout set. The most important result was not just the 100% precision—it was recognizing that recall was only 22.22%, so the model was trustworthy when it predicted positive but too conservative for broad detection.

---

<<<<<<< HEAD
- `.txt`
- `.md`
- `.html`
- `.docx`
- `.pdf`

Reports are saved in either `reports/id3/` or `reports/bayes/`.

## Generated Excel Files

Excel files are saved in either `outputs/id3/` or `outputs/bayes/`. Each file corresponds to one major step or calculation, such as dataset overview, entropy/gain, pruning decisions, probability tables, predictions, confusion matrix, metrics, and defense notes.

## Portability Notes

- Share the project folder contents, not your local `.venv`.
- On each computer, recreate the environment and run `python -m pip install -r requirements.txt`.
- Run the script from the project root so the relative `data/`, `outputs/`, and `reports/` folders resolve correctly.
=======
**Project type:** Completed graduate academic project  
**Course:** CSCI 7434 — Data Mining, Georgia Southern University  
**Author:** Autenia Murray
>>>>>>> parent of 4508527 (Add files via upload)
