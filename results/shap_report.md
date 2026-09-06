# SHAP Explainability Report

## Model
Logistic Regression heart disease classifier.

## Feature Importance

| feature   |   mean_abs_shap |
|:----------|----------------:|
| sno       |      64.2738    |
| thalach   |       1.663     |
| age       |       0.710195  |
| trestbps  |       0.296574  |
| oldpeak   |       0.104387  |
| ca        |       0.0662457 |
| slope     |       0.0452623 |
| chol      |       0.0396979 |
| cp        |       0.0377041 |
| thal      |       0.0257816 |
| restecg   |       0.0197645 |
| exang     |       0.0154697 |
| gender    |       0.0118536 |
| fbs       |       0.0116512 |

## Least Impactful Features

| feature   |   mean_abs_shap |
|:----------|----------------:|
| exang     |       0.0154697 |
| gender    |       0.0118536 |
| fbs       |       0.0116512 |
