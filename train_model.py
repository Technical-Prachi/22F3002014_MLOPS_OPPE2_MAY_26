import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

os.makedirs("artifacts", exist_ok=True)

# Load dataset
df = pd.read_csv("data/data.csv")

# Remove rows containing missing values
df = df.dropna().copy()

# Encode gender
gender_encoder = LabelEncoder()
df["gender"] = gender_encoder.fit_transform(df["gender"])

# Encode target: no = 0, yes = 1
target_encoder = LabelEncoder()
df["target"] = target_encoder.fit_transform(df["target"])

# Separate features and target
X = df.drop(columns=["target"])
y = df["target"]

# Save feature order and encoders
feature_columns = X.columns.tolist()

joblib.dump(gender_encoder, "artifacts/gender_encoder.joblib")
joblib.dump(target_encoder, "artifacts/target_encoder.joblib")
joblib.dump(feature_columns, "artifacts/feature_columns.joblib")

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# Logistic Regression model
model = LogisticRegression(
    max_iter=2000,
    random_state=42
)

model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
accuracy = accuracy_score(y_test, y_pred)

print("=" * 60)
print("HEART DISEASE MODEL TRAINING")
print("=" * 60)
print(f"Dataset shape after cleaning: {df.shape}")
print(f"Training shape: {X_train.shape}")
print(f"Testing shape: {X_test.shape}")
print(f"Accuracy: {accuracy:.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "artifacts/heart_disease_model.joblib")

# Save test data for SHAP and Fairlearn
X_test.to_csv("artifacts/X_test.csv", index=False)
y_test.to_csv("artifacts/y_test.csv", index=False)

print("=" * 60)
print("ARTIFACTS SAVED")
print("=" * 60)
print("artifacts/heart_disease_model.joblib")
print("artifacts/feature_columns.joblib")
print("artifacts/gender_encoder.joblib")
print("artifacts/target_encoder.joblib")
print("artifacts/X_test.csv")
print("artifacts/y_test.csv")
