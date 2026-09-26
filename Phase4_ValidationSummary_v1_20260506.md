# Phase 4 Validation Summary

Validated at: 2026-05-06 06:15:18

## Run Tests

### ID3 Branch

- Status: Passed, script completed without runtime error.
- Test input used: classifier = ID3, live output = no, T1 = 0.20, g = 0.010.
- Training records: 365
- Test records: 44
- Rules before post-pruning: 209
- Rules after post-pruning: 2
- Final accuracy percent: 47.73%

### Naive Bayes Branch

- Status: Passed, script completed without runtime error.
- Test input used: classifier = Bayes, live output = yes.
- Training records: 365
- Test records: 44
- Smoothing used: Yes
- Final accuracy percent: 45.45%

## Dependency Check

- pandas
- openpyxl
- python-docx
- reportlab
- jupyter
- ipykernel

No NumPy import found in code: Yes
No scikit-learn reference found in code: Yes

## Output File Check

- ID3 Excel files found: 21
- Bayes Excel files found: 18
- ID3 report files found: 10
- Bayes report files found: 10

## Notes

- The latest ID3 sample outputs in the package reflect T1 = 0.20 and g = 0.010.
- The program allows the user to choose different valid values during the live run.
- File save messages print to the VS Code terminal as each output file is generated.