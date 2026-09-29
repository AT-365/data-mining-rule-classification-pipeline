# Assignment 2 Data Mining Report - ID3

## Program Inputs
- **Classifier Choice:** ID3
- **Live Terminal Output:** Yes
- **T1 Threshold:** 0.8
- **g Parameter:** 0.01
- **Training File:** A2--ID3-Training set.csv
- **Test File:** A2--ID3-TEST set.csv

## What This Method Does
ID3 builds a decision tree from the training set, extracts readable IF-THEN rules, and uses those rules to classify the test set.
The pre-pruning threshold T1 controls early stopping during tree construction.  The post-pruning parameter g controls whether a completed subtree can be removed after testing the effect on classification quality.

## Main Result
After post-pruning, ID3 correctly classified 47.73% of the ID3 test records.

## Formula Notes
- ID3 entropy/MC: -sum(p * log2(p)).
- ID3 Gain: MC(D) - WMC(attribute).
- ID3 pre-pruning mixture ratio: alpha = c1 / |F1|.
- ID3 post-pruning: if (N - M) / Q <= gK, then the subtree can be removed.
- Naive Bayes prior: count(Volume class) / total training records.
- Naive Bayes categorical probability: count(attribute value and class) / count(class), with Laplace smoothing if needed.
- Naive Bayes continuous probability uses the Gaussian density formula with mean and sample standard deviation by class.

## Output Tables Created
- ID3 Class Distribution
- ID3 Gain Calculations
- ID3 Pre-Pruning Decisions
- ID3 Post-Pruning Decisions
- ID3 Final Metrics
