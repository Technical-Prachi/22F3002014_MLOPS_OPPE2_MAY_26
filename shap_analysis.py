import os
import joblib
import pandas as pd
import shap
import matplotlib.pyplot as plt

os.makedirs("results", exist_ok=True)

# Load model and test data
model = joblib.load("artifacts/heart_disease_model.joblib")
X_test = pd.read_csv("artifacts/X_test.csv")

# SHAP explainer for Logistic Regression
explainer = shap.LinearExplainer(model, X_test)
shap_values = explainer(X_test)

# Mean absolute SHAP importance
importance = pd.DataFrame({
    "feature": X_test.columns,
    "mean_abs_shap": abs(shap_values.values).mean(axis=0)
}).sort_values("mean_abs_shap", ascending=False)

print("=" * 60)
print("SHAP FEATURE IMPORTANCE")
print("=" * 60)
print(importance.to_string(index=False))

# Save importance table
importance.to_csv("results/shap_feature_importance.csv", index=False)

# Save SHAP summary plot
plt.figure()
shap.summary_plot(shap_values, X_test, show=False)
plt.tight_layout()
plt.savefig("results/shap_summary.png", dpi=200, bbox_inches="tight")
plt.close()

# Least-impact features
least = importance.tail(3)

print("\nLeast impactful features:")
print(least.to_string(index=False))

with open("results/shap_report.md", "w") as f:
    f.write("# SHAP Explainability Report\n\n")
    f.write("## Model\n")
    f.write("Logistic Regression heart disease classifier.\n\n")
    f.write("## Feature Importance\n\n")
    f.write(importance.to_markdown(index=False))
    f.write("\n\n## Least Impactful Features\n\n")
    f.write(least.to_markdown(index=False))
    f.write("\n")

print("\nSaved:")
print("results/shap_feature_importance.csv")
print("results/shap_summary.png")
print("results/shap_report.md")
