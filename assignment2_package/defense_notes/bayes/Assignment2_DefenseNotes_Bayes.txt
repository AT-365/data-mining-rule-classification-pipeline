# Assignment 2 Defense Notes - Naive Bayes

## Quick Setup
- Classifier Choice: Naive Bayes
- Live Terminal Output: Yes
- Training File: A2--Bayes-Training set.csv
- Test File: A2--Bayes-TEST set.csv

## Who, What, When, Where, Why, How
- Who: DFCA wants a classifier for product order Volume.
- What: Naive Bayes calculates probability scores for each possible Volume class.
- When: Probability tables are learned from the Bayes training set, then applied to the Bayes test set.
- Where: Categorical probabilities, continuous statistics, scores, and predictions are exported to Excel.
- Why: Naive Bayes can handle both categorical attributes and continuous Weight/Material values.
- How: The program multiplies the prior probability, categorical probability components, and continuous probability components for each class.
- Smoothing: Laplace smoothing was used because at least one categorical value/class combination had a zero count.

## Formula Checklist
- Entropy/MC = -sum(p * log2(p)).
- Gain = MC(D) - WMC(attribute).
- ID3 alpha = c1 / |F1|.
- ID3 post-pruning: if (N - M) / Q <= gK, remove subtree.
- Naive Bayes prior = count(class) / total records.
- Laplace smoothing = (count + 1) / (class count + number of possible values).
- Continuous probability = 1/(sqrt(2*pi)*std) * e^-((value-mean)^2/(2*std^2)).
