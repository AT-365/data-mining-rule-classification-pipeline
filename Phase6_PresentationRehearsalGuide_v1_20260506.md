# Phase 6 Presentation Rehearsal Guide

## Goal
Use the stable `.py` pipeline as the main Zoom demonstration.  Use Excel outputs, reports, and defense notes as backup evidence if Dr. Hashemi asks to inspect a specific calculation.

## Main Presentation Stack

1. VS Code terminal, main live run.
2. `outputs/id3/` or `outputs/bayes/`, calculation evidence.
3. `reports/id3/` or `reports/bayes/`, final report and defense notes.
4. Assignment directions PDF, backup for formulas and parameter requirements.

## Before the Zoom

1. Open the `DataMining_Assignment2Package_v1_20260506` folder in VS Code.
2. Confirm the `data/` folder contains all four CSV files.
3. Open the terminal in VS Code.
4. Run:

```bash
pip install -r requirements.txt
```

5. Keep these folders visible in VS Code Explorer:
   - `outputs/`
   - `reports/`
   - `data/`

## Live Run Command

Run:

```bash
python DataMining_Assignment2Pipeline_v1_20260506_FullSubmission.py
```

## Recommended Live Run Choices

### ID3 Run

Use ID3 first if you want the more visual, rule-based explanation.

Suggested inputs:

```text
Classifier choice: ID3
Show live section output: yes
T1: 0.20
g: 0.010
```

What to say:

```text
I selected ID3 because it builds a decision tree and extracts readable IF-THEN rules.  The program asks for T1 because T1 controls pre-pruning with the mixture ratio alpha = c1 / |F1|.  It also asks for g because g is part of the post-pruning formula from the assignment, and the assignment restricts g to 0 < g <= 0.015.
```

### Naive Bayes Run

Use Bayes second if Dr. Hashemi asks to see the other classifier option.

Suggested inputs:

```text
Classifier choice: Bayes
Show live section output: yes
```

What to say:

```text
I selected Naive Bayes because it calculates probability scores for each possible Volume class and predicts the class with the highest score.  The Bayes dataset keeps Weight and Material continuous, so the program handles those two attributes using the continuous probability formula and uses categorical probability tables for the other attributes.
```

## What to Show if Asked

### If asked about ID3 entropy or gain
Open:

```text
outputs/id3/07_id3_gain_calculations_by_node.xlsx
```

Say:

```text
This file shows the entropy, weighted entropy, and information gain calculations for the ID3 split decisions.
```

### If asked about ID3 pre-pruning
Open:

```text
outputs/id3/09_id3_pre_pruning_decisions.xlsx
```

Say:

```text
This file shows alpha = c1 / |F1| for each branch and whether the branch stopped early based on T1.
```

### If asked about ID3 post-pruning
Open:

```text
outputs/id3/14_id3_post_pruning_calculations.xlsx
```

Say:

```text
This file shows the assignment post-pruning check: if (N - M) / Q <= gK, then the subtree can be removed.
```

### If asked about Naive Bayes smoothing
Open:

```text
outputs/bayes/09_bayes_smoothing_decision.xlsx
```

Say:

```text
This file documents whether smoothing was needed.  Smoothing is checked because Naive Bayes multiplies probability values, and a zero probability can force an entire class score to zero.
```

### If asked about continuous attributes in Bayes
Open:

```text
outputs/bayes/11_bayes_continuous_statistics.xlsx
outputs/bayes/12_bayes_test_probability_details.xlsx
```

Say:

```text
These files show how Weight and Material were handled as continuous attributes.  The program calculates class-specific mean and standard deviation values, then uses the continuous probability component for each test record.
```

### If asked about final accuracy
Open:

```text
outputs/id3/18_id3_metrics_after_post_pruning.xlsx
outputs/bayes/16_bayes_metrics.xlsx
```

Say:

```text
These files show the final correct classification results for the selected method.
```

## What Not to Volunteer

1. Do not open a Jupyter notebook unless asked.
2. Do not discuss extra alternative formulas unless asked.
3. Do not over-explain smoothing unless asked.
4. Do not apologize for accuracy.  Explain that the result reflects the selected algorithm, training data, and assignment-required parameters.

## Short Closing Script

```text
The program gives DFCA a choice between ID3 and Naive Bayes.  ID3 produces a decision tree and readable rules, while Naive Bayes produces probability-based class predictions.  The outputs are saved step by step so each calculation can be inspected, and the final report explains what the selected method predicted for the test set.
```

## Final Folder Check

Before presenting, confirm these exist:

1. `DataMining_Assignment2Pipeline_v1_20260506_FullSubmission.py`
2. `requirements.txt`
3. `README.md`
4. `outputs/id3/`
5. `outputs/bayes/`
6. `reports/id3/`
7. `reports/bayes/`
8. `Phase4_ValidationSummary_v1_20260506.md`
9. `Phase6_PresentationRehearsalGuide_v1_20260506.md`
