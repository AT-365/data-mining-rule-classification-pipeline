# Assignment 2: Naive Bayes and ID3 Decision Tree Classification

This folder contains the tracked Assignment 2 submission artifacts for CSCI 7434 Data Mining at Georgia Southern University.

## Layout

- `DataMining_Assignment2Pipeline_v1_20260506_FullSubmission.py` — Assignment 2 pipeline implementation
- `Assignment2_Report_Bayes.pdf`, `Assignment2_Report_ID3.pdf` — final reports
- `Assignment2_DefenseNotes_Bayes.pdf`, `Assignment2_DefenseNotes_ID3.pdf` — defense notes
- `DM-Assignment 2-Directions.pdf` — assignment directions
- `DataMining_PresentationScript_v1_20260506_Assignments1and2.pdf` — presentation script
- `data/` — Bayes and ID3 training/test CSV datasets
- `bayes/` — Naive Bayes analysis workbooks and summary files
- `id3/` — ID3 analysis workbooks and summary files

## Key algorithms

- **Naive Bayes:** Probabilistic classifier using class priors and conditional probabilities with Laplace smoothing for categorical attributes and Gaussian distribution for continuous attributes.
- **ID3:** Recursive decision tree builder using information gain (entropy-based) with pre-pruning and post-pruning to prevent overfitting.

## Notes

- The pipeline expects the `data/` directory to live beside the Assignment 2 script inside this package.
- `FILES_MANIFEST.txt` lists the tracked Assignment 2 artifacts currently stored in this package.
