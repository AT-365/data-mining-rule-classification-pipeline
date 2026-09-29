# Assignment 2 Defense Notes - ID3

## Quick Setup
- Classifier Choice: ID3
- Live Terminal Output: Yes
- T1 Threshold: 0.8
- g Parameter: 0.01
- Training File: A2--ID3-Training set.csv
- Test File: A2--ID3-TEST set.csv

## Who, What, When, Where, Why, How
- Who: DFCA wants a classifier for product order Volume.
- What: ID3 creates a decision tree and IF-THEN rules.
- When: The tree is built from the ID3 training set and tested against the ID3 test set.
- Where: The logic runs in the Python pipeline; each calculation table is exported to Excel.
- Why: ID3 gives readable rules, which helps explain why a Volume class was predicted.
- How: The program calculates entropy, weighted entropy, information gain, pre-pruning alpha, post-pruning loss, and final predictions.
- T1: User-chosen pre-pruning threshold. Higher T1 usually stops more branches early. Lower T1 usually allows deeper splitting.
- g: User-chosen post-pruning parameter, valid range 0 < g <= 0.015. Higher g allows more pruning. Lower g allows less pruning.

## Formula Checklist
- Entropy/MC = -sum(p * log2(p)).
- Gain = MC(D) - WMC(attribute).
- ID3 alpha = c1 / |F1|.
- ID3 post-pruning: if (N - M) / Q <= gK, remove subtree.
- Naive Bayes prior = count(class) / total records.
- Laplace smoothing = (count + 1) / (class count + number of possible values).
- Continuous probability = 1/(sqrt(2*pi)*std) * e^-((value-mean)^2/(2*std^2)).
