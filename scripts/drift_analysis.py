import pandas as pd
import numpy as np

TRAIN_FILE = "data/data.csv"
PRED_FILE = "results/random_100.csv"

train = pd.read_csv(TRAIN_FILE).dropna()
pred = pd.read_csv(PRED_FILE)

# Remove target from training data
train = train.drop(columns=["target"], errors="ignore")

# Keep only common features
features = [c for c in train.columns if c in pred.columns]

results = []

def psi_numeric(expected, actual, bins=10):
    expected = pd.to_numeric(expected, errors="coerce").dropna()
    actual = pd.to_numeric(actual, errors="coerce").dropna()

    if expected.nunique() < 2:
        return 0.0

    edges = np.unique(np.quantile(expected, np.linspace(0, 1, bins + 1)))

    if len(edges) < 3:
        return 0.0

    expected_counts, _ = np.histogram(expected, bins=edges)
    actual_counts, _ = np.histogram(actual, bins=edges)

    expected_pct = expected_counts / max(len(expected), 1)
    actual_pct = actual_counts / max(len(actual), 1)

    expected_pct = np.where(expected_pct == 0, 0.0001, expected_pct)
    actual_pct = np.where(actual_pct == 0, 0.0001, actual_pct)

    return float(np.sum(
        (actual_pct - expected_pct) *
        np.log(actual_pct / expected_pct)
    ))

def psi_categorical(expected, actual):
    categories = sorted(
        set(expected.dropna().astype(str)) |
        set(actual.dropna().astype(str))
    )

    if not categories:
        return 0.0

    expected_pct = expected.astype(str).value_counts(
        normalize=True
    ).reindex(categories, fill_value=0.0001)

    actual_pct = actual.astype(str).value_counts(
        normalize=True
    ).reindex(categories, fill_value=0.0001)

    expected_pct = expected_pct.clip(lower=0.0001)
    actual_pct = actual_pct.clip(lower=0.0001)

    return float(np.sum(
        (actual_pct - expected_pct) *
        np.log(actual_pct / expected_pct)
    ))

for feature in features:
    if train[feature].dtype == "object" or pred[feature].dtype == "object":
        psi = psi_categorical(train[feature], pred[feature])
    else:
        psi = psi_numeric(train[feature], pred[feature])

    if psi < 0.10:
        status = "No significant drift"
    elif psi < 0.25:
        status = "Moderate drift"
    else:
        status = "Significant drift"

    results.append({
        "feature": feature,
        "PSI": round(psi, 6),
        "status": status
    })

report = pd.DataFrame(results).sort_values("PSI", ascending=False)

report.to_csv("results/drift_report.csv", index=False)

with open("results/drift_report.md", "w") as f:
    f.write("# Input Drift Analysis\n\n")
    f.write("Training distribution was compared with the same 100-row prediction dataset using Population Stability Index (PSI).\n\n")
    f.write("## Interpretation\n")
    f.write("- PSI < 0.10: No significant drift\n")
    f.write("- PSI 0.10–0.25: Moderate drift\n")
    f.write("- PSI > 0.25: Significant drift\n\n")
    f.write("## Results\n\n")
    f.write(report.to_markdown(index=False))
    f.write("\n")

print("\n=== DRIFT REPORT ===")
print(report.to_string(index=False))
print("\nSaved: results/drift_report.csv")
print("Saved: results/drift_report.md")
