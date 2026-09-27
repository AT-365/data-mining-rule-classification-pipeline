# Data Mining Rule-Classification Pipeline

[![Tests](https://github.com/AT-365/data-mining-rule-classification-pipeline/actions/workflows/tests.yml/badge.svg)](https://github.com/AT-365/data-mining-rule-classification-pipeline/actions/workflows/tests.yml)

This repository contains two related deliverables:

- the public `data_mining_pipeline.py` rule-classification pipeline and its tests
- the packaged Assignment 2 submission materials under `dm_assignment2_package/`

## Repository structure

| Path | Purpose |
|---|---|
| [`data_mining_pipeline.py`](data_mining_pipeline.py) | Public association-rule classification pipeline |
| [`tests/test_pipeline.py`](tests/test_pipeline.py) | Synthetic unit tests for core calculations and validation |
| [`DATASET.md`](DATASET.md) | Input schema and dataset availability for the public pipeline |
| [`docs/`](docs) | Public documentation and release notes |
| [`dm_assignment2_package/`](dm_assignment2_package) | Organized Assignment 2 package with reports, datasets, and analysis artifacts |
| [`requirements.txt`](requirements.txt) | Python dependencies |

## Assignment 2 package layout

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
|   |-- id3/
|   |-- FILES_MANIFEST.txt
|   `-- README.md
|-- requirements.txt
`-- README.md
```

## Run the public pipeline locally

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python data_mining_pipeline.py --input path/to/input.csv --output-dir outputs
```

The original course dataset is not distributed. See [`DATASET.md`](DATASET.md) for the required input schema.

## Run the packaged Assignment 2 pipeline

```bash
python -m pip install -r requirements.txt
python dm_assignment2_package/DataMining_Assignment2Pipeline_v1_20260506_FullSubmission.py
```

The Assignment 2 script expects its `data/` directory to remain inside `dm_assignment2_package/`.

## Automated tests

The public test suite uses small synthetic inputs rather than the protected course dataset.

```bash
python -m unittest discover -s tests -v
```
