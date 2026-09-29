# Assignment 2 Data Mining Report - Naive Bayes

## Program Inputs
- **Classifier Choice:** Naive Bayes
- **Live Terminal Output:** Yes
- **Training File:** A2--Bayes-Training set.csv
- **Test File:** A2--Bayes-TEST set.csv

## What This Method Does
Naive Bayes calculates one probability score for each possible Volume class and predicts the class with the largest score.
Categorical attributes use conditional probability tables.  Weight and Material are treated as continuous attributes and use the continuous probability formula from class notes.

## Main Result
Naive Bayes correctly classified 45.45% of the Bayes test records. Laplace smoothing was used because at least one categorical value/class combination had a zero count.

## Formula Notes
- ID3 entropy/MC: -sum(p * log2(p)).
- ID3 Gain: MC(D) - WMC(attribute).
- ID3 pre-pruning mixture ratio: alpha = c1 / |F1|.
- ID3 post-pruning: if (N - M) / Q <= gK, then the subtree can be removed.
- Naive Bayes prior: count(Volume class) / total training records.
- Naive Bayes categorical probability: count(attribute value and class) / count(class), with Laplace smoothing if needed.
- Naive Bayes continuous probability uses the Gaussian density formula with mean and sample standard deviation by class.

## Output Tables Created
- Bayes Class Distribution
- Bayes Class Priors
- Bayes Smoothing Decision
- Bayes Continuous Statistics
- Bayes Final Metrics
