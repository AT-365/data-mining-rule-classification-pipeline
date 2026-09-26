# Data Mining Assignment 2 Package

## Purpose

This folder contains the Python pipeline for Data Mining Assignment 2. The program lets the user choose either ID3 or Naive Bayes, then runs the selected method from start to finish.

The pipeline creates step-by-step Excel files, report files, and defense notes while printing progress messages in the VS Code terminal.

## Folder Structure

```text
DataMining_Assignment2Package_v1_20260506/
|-- data/
|   |-- A2--ID3-Training set.csv
|   |-- A2--ID3-TEST set.csv
|   |-- A2--Bayes-Training set.csv
|   `-- A2--Bayes-TEST set.csv
|-- outputs/
|   |-- id3/
|   `-- bayes/
|-- reports/
|   |-- id3/
|   `-- bayes/
|-- DataMining_Assignment2Pipeline_v1_20260506_FullSubmission.py
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
py DataMining_Assignment2Pipeline_v1_20260506_FullSubmission.py
```

1. Open the full folder in VS Code or another development environment.
2. Open a terminal in the project folder.
3. Create and activate a fresh virtual environment on that computer.

Important:

- Do not rely on a copied `.venv` from another machine. Python virtual environments contain machine-specific paths and often break when moved.
- Use Python 3.10 or newer.
- Install the packages from `requirements.txt` before running the pipeline.

Windows PowerShell example:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Mac/Linux example:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## How to Run

From the project folder, run:

```powershell
python DataMining_Assignment2Pipeline_v1_20260506_FullSubmission.py
```

If the required packages are missing, the script now stops immediately and prints a setup message instead of failing later during Excel, DOCX, or PDF export.

It also checks that all four assignment CSV files are present before asking for user input.

Recommended first-time setup on another computer:

```powershell
python -m pip install -r requirements.txt
python DataMining_Assignment2Pipeline_v1_20260506_FullSubmission.py
```

The program will ask:

1. Whether to run ID3 or Bayes.
2. Whether to show live section output in the terminal.
3. If ID3 is selected, it will ask for T1 and g.

## Example Inputs

### ID3

```text
Classifier choice: ID3
Show live section output: yes
T1: 0.80
g: 0.010
```

### Naive Bayes

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

This shows that files are being generated during the live run.

## Generated Report Formats

Each selected method creates:

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
