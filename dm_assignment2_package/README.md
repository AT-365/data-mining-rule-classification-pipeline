# Assignment 2: Naive Bayes and ID3 Decision Tree Classification

This folder contains the complete Assignment 2 submission for CSCI 7434 Data Mining at Georgia Southern University.

## Contents

### Core Files
- **Pipeline implementation:** `DataMining_Assignment2Pipeline_v1_20260506_FullSubmission.py`
- **Presentation script:** `DataMining_PresentationScript_v1_20260506_Assignments1and2.pdf`
- **Assignment directions:** `DM-Assignment 2-Directions.pdf`

### Naive Bayes (Bayes)
- **Report:** `Assignment2_Report_Bayes.pdf`
- **Defense notes:** `Assignment2_DefenseNotes_Bayes.pdf`
- **Training set:** `A2--Bayes-Training set.csv`
- **Test set:** `A2--Bayes-TEST set.csv`
- **Analysis files:** `*_bayes_*.xlsx` (15 detailed analysis spreadsheets)

### ID3 Decision Tree (ID3)
- **Report:** `Assignment2_Report_ID3.pdf`
- **Defense notes:** `Assignment2_DefenseNotes_ID3.pdf`
- **Training set:** `A2--ID3-Training set.csv`
- **Test set:** `A2--ID3-TEST set.csv`
- **Analysis files:** `*_id3_*.xlsx` (18 detailed analysis spreadsheets)

### Validation & Documentation
- **Validation summary:** `Phase4_ValidationSummary_v1_20260506.md`
- **Presentation rehearsal guide:** `Phase6_PresentationRehearsalGuide_v1_20260506.md`

## Key Algorithms

**Naive Bayes:** Probabilistic classifier using class priors and conditional probabilities with Laplace smoothing for categorical attributes and Gaussian distribution for continuous attributes.

**ID3:** Recursive decision tree builder using information gain (entropy-based) with pre-pruning and post-pruning to prevent overfitting.

## Structure

Each algorithm includes:
- Training dataset overview and class distribution analysis
- Attribute type classification
- Model-specific calculations (priors for Bayes, gain calculations for ID3)
- Test predictions with detailed probability/confidence scores
- Confusion matrix and performance metrics
- Defense notes explaining all methodology decisions
