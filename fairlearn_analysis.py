import os
import joblib
import pandas as pd

from sklearn.metrics import accuracy_score, precision_score, recall_score
from fairlearn.metrics import MetricFrame, selection_rate, demographic_parity_difference

os.makedirs("results", exist_ok=True)

# Load model and test data
model = joblib.load("artifacts/heart_disease_model.joblib")
X_test = pd.read_csv("artifacts/X_test.csv")
y_test = pd.read_csv("artifacts/y_test.csv").squeeze()

# Predictions
y_pred = model.predict(X_test)

# Age groups for interpretable fairness analysis
def age_group(age):
    if age < 40:
        return "<40"
    elif age < 60:
        return "40-59"
    else:
        return "60+"

age_groups = X_test["age"].apply(age_group)

# Metrics
metrics = {
    "accuracy": accuracy_score,
    "precision": precision_score,
    "recall": recall_score,
    "selection_rate": selection_rate
}

metric_frame = MetricFrame(
    metrics=metrics,
    y_true=y_test,
    y_pred=y_pred,
    sensitive_features=age_groups
)

print("=" * 70)
print("FAIRLEARN AGE-BASED FAIRNESS ANALYSIS")
print("=" * 70)

print("\nMetrics by age group:")
print(metric_frame.by_group)

print("\nOverall metrics:")
print(metric_frame.overall)

# Demographic parity difference
dp_difference = demographic_parity_difference(
    y_true=y_test,
    y_pred=y_pred,
    sensitive_features=age_groups
)

print(f"\nDemographic Parity Difference: {dp_difference:.4f}")

# Metric ranges
print("\nMetric ranges:")
print(metric_frame.by_group.max() - metric_frame.by_group.min())

# Save results
metric_frame.by_group.to_csv("results/fairlearn_by_age_group.csv")

with open("results/fairlearn_report.md", "w") as f:
    f.write("# Fairlearn Age-Based Fairness Report\n\n")
    f.write("## Sensitive Attribute\n")
    f.write("Age, grouped into <40, 40-59, and 60+.\n\n")

    f.write("## Metrics by Age Group\n\n")
    f.write(metric_frame.by_group.to_markdown())
    f.write("\n\n")

    f.write("## Overall Metrics\n\n")
    f.write(metric_frame.overall.to_frame().T.to_markdown(index=False))
    f.write("\n\n")

    f.write("## Demographic Parity Difference\n\n")
    f.write(f"{dp_difference:.4f}\n\n")

    f.write("## Interpretation\n\n")
    f.write(
        "Fairness metrics were evaluated across age groups. "
        "Differences between groups indicate that model predictions "
        "may vary across age categories. These differences should be "
        "reviewed alongside the clinical context and dataset size.\n"
    )

print("\nSaved:")
print("results/fairlearn_by_age_group.csv")
print("results/fairlearn_report.md")
