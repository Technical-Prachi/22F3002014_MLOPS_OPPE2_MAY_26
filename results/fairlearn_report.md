# Fairlearn Age-Based Fairness Report

## Sensitive Attribute
Age, grouped into <40, 40-59, and 60+.

## Metrics by Age Group

| age   |   accuracy |   precision |   recall |   selection_rate |
|:------|-----------:|------------:|---------:|-----------------:|
| 40-59 |          1 |           1 |        1 |         0.583333 |
| 60+   |          1 |           1 |        1 |         0.5      |
| <40   |          1 |           1 |        1 |         0.333333 |

## Overall Metrics

|   accuracy |   precision |   recall |   selection_rate |
|-----------:|------------:|---------:|-----------------:|
|          1 |           1 |        1 |         0.542373 |

## Demographic Parity Difference

0.2500

## Interpretation

Fairness metrics were evaluated across age groups. Differences between groups indicate that model predictions may vary across age categories. These differences should be reviewed alongside the clinical context and dataset size.
