# Results and Interpretation

## Dataset flow

| Stage | Records |
|---|---:|
| Initial dataset | 414 |
| Removed as outliers | 105 |
| Cleaned dataset | 309 |
| Held-out test set | 32 |

## Model evaluation

| Metric | Value |
|---|---:|
| True positives | 4 |
| False negatives | 14 |
| False positives | 0 |
| True negatives | 14 |
| Accuracy | 56.25% |
| Recall | 22.22% |
| Precision | 100.00% |

## Interpretation

The classifier produced no false positive predictions in the test set, which resulted in perfect precision. However, it missed 14 of 18 positive cases, so recall was low. This means the rules were reliable when they fired but did not cover enough of the positive class.

The outcome points to several responsible next steps:

- Tune support and confidence thresholds using cross-validation rather than a single holdout split.
- Compare precision-recall tradeoffs across threshold settings.
- Expand rule coverage while monitoring false positives.
- Compare the rule-based classifier with baseline models.
- Evaluate stability across multiple stratified splits.

These are proposed extensions, not claims about work already completed.
