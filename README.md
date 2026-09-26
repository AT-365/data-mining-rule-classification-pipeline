# Data Mining Assignment 2 Package

Edited at: 2026-05-06 05:55

## Purpose

This folder contains the VS Code-ready Python pipeline for Data Mining Assignment 2.  The program lets the user choose either ID3 or Naive Bayes, then runs the selected method from start to finish.

The pipeline creates step-by-step Excel files, report files, and defense notes while printing progress messages in the VS Code terminal.

## Folder Structure

```text
DataMining_Assignment2Package_v1_20260506/
├── data/
│   ├── A2--ID3-Training set.csv
│   ├── A2--ID3-TEST set.csv
│   ├── A2--Bayes-Training set.csv
│   └── A2--Bayes-TEST set.csv
├── outputs/
│   ├── id3/
│   └── bayes/
├── reports/
│   ├── id3/
│   └── bayes/
├── notebooks/
├── DataMining_Assignment2Pipeline_v1_20260506_FullSubmission.py
├── requirements.txt
└── README.md
```

## VS Code Setup

1. Open the full folder in VS Code.
2. Open the terminal inside VS Code.
3. Create and activate a virtual environment if desired.

Windows PowerShell example:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Mac/Linux example:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## How to Run

From the project folder, run:

```bash
python DataMining_Assignment2Pipeline_v1_20260506_FullSubmission.py
```

The program will ask:

1. Whether to run ID3 or Bayes.
2. Whether to show live section output in the terminal.
3. If ID3 is selected, it will ask for T1 and g.

## Suggested Zoom Demo Inputs

### ID3 Demo

```text
Classifier choice: ID3
Show live section output: yes
T1: 0.80
g: 0.010
```

### Naive Bayes Demo

```text
Classifier choice: Bayes
Show live section output: yes
```

## Important Algorithm Notes

- ID3 is implemented from scratch.
- Naive Bayes probability calculations are implemented from scratch.
- The program does not use scikit-learn or a packaged classifier.
- Pandas is used for reading CSV files and building tables.
- Openpyxl is used for Excel output.
- Python's standard math library is used for probability formulas.

## Output Behavior

As the `.py` pipeline runs, the VS Code terminal prints progress messages such as:

```text
--- Calculating entropy and information gain ---
Saved: outputs/id3/07_id3_gain_calculations_by_node.xlsx
```

This lets the professor see that files are being generated during the live run.

## Generated Report Formats

Each selected method creates:

- `.txt`
- `.md`
- `.html`
- `.docx`
- `.pdf`

Reports are saved in either `reports/id3/` or `reports/bayes/`.

## Generated Excel Files

Excel files are saved in either `outputs/id3/` or `outputs/bayes/`.  Each file corresponds to one major step or calculation, such as dataset overview, entropy/gain, pruning decisions, probability tables, predictions, confusion matrix, metrics, and defense notes.
