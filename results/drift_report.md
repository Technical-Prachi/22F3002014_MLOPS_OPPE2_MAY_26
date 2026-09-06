# Input Drift Analysis

Training distribution was compared with the same 100-row prediction dataset using Population Stability Index (PSI).

## Interpretation
- PSI < 0.10: No significant drift
- PSI 0.10–0.25: Moderate drift
- PSI > 0.25: Significant drift

## Results

| feature   |      PSI | status               |
|:----------|---------:|:---------------------|
| oldpeak   | 0.081447 | No significant drift |
| sno       | 0.071814 | No significant drift |
| cp        | 0.061148 | No significant drift |
| trestbps  | 0.055197 | No significant drift |
| thalach   | 0.046393 | No significant drift |
| age       | 0.041838 | No significant drift |
| chol      | 0.033787 | No significant drift |
| restecg   | 0.022711 | No significant drift |
| slope     | 0.019535 | No significant drift |
| ca        | 0.010528 | No significant drift |
| thal      | 0.000402 | No significant drift |
| gender    | 0        | No significant drift |
| exang     | 0        | No significant drift |
| fbs       | 0        | No significant drift |
