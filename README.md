# MLOps OPPE-2 — Heart Disease Prediction

## 1. Project Overview

This project implements an end-to-end MLOps pipeline for a heart disease prediction system.

The project covers:

- Machine learning model training
- SHAP-based model explainability
- Fairness analysis using Fairlearn
- FastAPI model serving
- Docker containerization
- Google Artifact Registry
- Deployment on Google Kubernetes Engine (GKE)
- Horizontal Pod Autoscaling (HPA)
- GitHub Actions CI/CD
- Per-sample prediction logging using Google Cloud Logging
- High-concurrency performance testing using `wrk`
- Input data drift monitoring using Population Stability Index (PSI)

---

## 2. Repository Information

**Repository:** `22F3002014_MLOPS_OPPE2_MAY_26`

**Cloud Project:** `iris-mlops-500704`

**GCP Region:** `us-central1`

**GKE Cluster:** `exam-cluster`

**GKE Zone:** `us-central1-a`

**Artifact Registry Repository:** `oppe2-repo`

---

## 3. Dataset

The project uses the heart disease dataset stored at:

```text
data/data.csv

The dataset contains 303 records and 15 columns.

Features include:

sno
age
gender
cp
trestbps
chol
fbs
restecg
thalach
exang
oldpeak
slope
ca
thal

The target variable is:

target

Missing values are removed before model training.

4. Model Training

The model is trained using Logistic Regression from scikit-learn.

Training configuration:

Train/Test split: 80/20
Random state: 42
Stratification: enabled
Maximum iterations: 2000

Training is performed using:

train_model.py

Generated model artifacts:

artifacts/heart_disease_model.joblib
artifacts/feature_columns.joblib
artifacts/gender_encoder.joblib
artifacts/target_encoder.joblib

The trained model achieved an accuracy of:

1.0000

on the held-out test set of 59 samples.

5. SHAP Explainability — D2

SHAP was used to explain the model predictions.

Script:

shap_analysis.py

Generated outputs:

results/shap_feature_importance.csv
results/shap_summary.png
results/shap_report.md

The mean absolute SHAP analysis identified the most influential features and the least impactful features.

The least impactful features included:

fbs
gender
exang

The SHAP analysis provides an interpretable view of how individual input features contribute to model predictions.

6. Fairness Analysis — D3

Fairness analysis was performed using the Fairlearn library.

The assignment-required sensitive attribute was:

age

Age was grouped into:

<40
40-59
60+

Metrics evaluated:

Accuracy
Precision
Recall
Selection rate
Demographic Parity Difference

Generated outputs:

results/fairlearn_by_age_group.csv
results/fairlearn_report.md

Observed demographic parity difference:

0.2500

Accuracy, precision and recall were 1.0 for all evaluated age groups on the test dataset.

The selection rate showed differences across age groups, which should be considered when evaluating fairness in a real-world deployment.

7. API Serving

The trained model is exposed through a FastAPI application.

Application:

app.py

Available endpoints:

Health Check
GET /health

Returns:

{
  "status": "healthy"
}
Prediction
POST /predict

The endpoint accepts the model input features and returns a heart disease prediction.

Example request:

{
  "sno": 1000,
  "age": 55,
  "gender": "male",
  "cp": 1,
  "trestbps": 130,
  "chol": 250,
  "fbs": 0,
  "restecg": 1,
  "thalach": 150,
  "exang": 0,
  "oldpeak": 1.0,
  "slope": 2,
  "ca": 0,
  "thal": 2
}
8. Dockerization

The API is containerized using Docker.

Files:

Dockerfile
requirements.txt
.dockerignore

The Docker image is stored in Google Artifact Registry.

Image repository:

us-central1-docker.pkg.dev/iris-mlops-500704/oppe2-repo/heart-api
9. GKE Deployment — D4

The Dockerized API is deployed on Google Kubernetes Engine.

Kubernetes resources:

deployment.yaml
service.yaml
hpa.yaml

Deployment:

heart-api

Service:

heart-api-service

The service uses a Google Cloud LoadBalancer.

The Horizontal Pod Autoscaler is configured with:

Minimum replicas: 1
Maximum replicas: 3
CPU target: 60%

The deployment also includes:

Readiness probe
Liveness probe
CPU/memory resource requests
CPU/memory resource limits
10. CI/CD — D4

GitHub Actions is used to automate the deployment pipeline.

Workflow:

.github/workflows/deploy.yaml

Pipeline steps:

Checkout source code
Authenticate to Google Cloud using Workload Identity Federation
Configure Docker authentication
Build Docker image
Push image to Artifact Registry
Authenticate to GKE
Verify Kubernetes access
Update the Kubernetes deployment
Wait for successful rollout

Workload Identity Federation is used instead of storing a long-lived Google Cloud service account key in GitHub.

11. Prediction Logging — D5

A random dataset containing 100 samples was generated using:

scripts/generate_100.py

Generated file:

results/random_100.csv

The 100 samples were sent to the deployed API using:

scripts/predict_100.py

Generated output:

results/predictions_100.csv

All 100 prediction requests were successfully processed.

For every prediction, the API logs:

Input features
Prediction
Timestamp

These logs are available through Google Cloud Logging.

12. Load Testing — D6

The deployed API was tested using wrk.

The test used:

Threads: 8
Concurrent connections: 2001
Duration: 30 seconds

Command:

wrk -t8 -c2001 -d30s --latency -s scripts/wrk_post.lua http://136.64.123.205

Observed results:

Total requests: 2686
Throughput: 89.23 requests/sec
Average latency: 1.35 sec
50th percentile: 1.44 sec
75th percentile: 1.63 sec
90th percentile: 1.91 sec
99th percentile: 1.92 sec
Timeouts: 2581
Connect errors: 0
Read errors: 0
Write errors: 0

The test demonstrates that the service was able to handle more than 2,000 concurrent connections.

However, the high number of timeouts indicates that the current deployment becomes capacity-constrained under extreme concurrency.

Load test output:

results/wrk_2001.txt
13. Input Drift Monitoring — D7

Input drift was evaluated by comparing the training data distribution with the same 100-row prediction dataset.

Population Stability Index (PSI) was used.

Interpretation:

PSI < 0.10  -> No significant drift
0.10-0.25   -> Moderate drift
> 0.25      -> Significant drift

Generated outputs:

results/drift_report.csv
results/drift_report.md

The maximum observed PSI was:

oldpeak = 0.081447

Since all feature PSI values were below 0.10, no significant input drift was detected.

14. Project Structure
22F3002014_MLOPS_OPPE2_MAY_26/
│
├── artifacts/
│   ├── heart_disease_model.joblib
│   ├── feature_columns.joblib
│   ├── gender_encoder.joblib
│   ├── target_encoder.joblib
│   ├── X_test.csv
│   └── y_test.csv
│
├── data/
│   └── data.csv
│
├── results/
│   ├── shap_feature_importance.csv
│   ├── shap_summary.png
│   ├── shap_report.md
│   ├── fairlearn_by_age_group.csv
│   ├── fairlearn_report.md
│   ├── random_100.csv
│   ├── predictions_100.csv
│   ├── wrk_2001.txt
│   ├── drift_report.csv
│   └── drift_report.md
│
├── scripts/
│   ├── generate_100.py
│   ├── predict_100.py
│   ├── drift_analysis.py
│   └── wrk_post.lua
│
├── .github/
│   └── workflows/
│       └── deploy.yaml
│
├── app.py
├── train_model.py
├── shap_analysis.py
├── fairlearn_analysis.py
├── Dockerfile
├── requirements.txt
├── .dockerignore
├── deployment.yaml
├── service.yaml
├── hpa.yaml
└── README.md
15. Key MLOps Architecture
Dataset
   |
   v
Data Cleaning
   |
   v
Model Training
   |
   +----> SHAP Explainability
   |
   +----> Fairlearn Fairness Analysis
   |
   v
Model Artifact
   |
   v
FastAPI
   |
   v
Docker Image
   |
   v
Artifact Registry
   |
   v
GKE Deployment
   |
   +----> HPA
   |
   +----> Cloud Logging
   |
   +----> Load Testing
   |
   +----> Input Drift Monitoring

GitHub
   |
   v
GitHub Actions
   |
   v
Workload Identity Federation
   |
   v
Google Cloud
16. Limitations

The dataset contains a column named sno, which is an identifier rather than a meaningful medical feature. It was retained to remain consistent with the implemented assignment pipeline.

The very high test accuracy should therefore be interpreted cautiously. In a production ML system, identifier columns should generally be excluded and the model should be validated using stronger leakage checks and independent validation data.

The 100-row drift dataset was randomly sampled from the same underlying dataset, so the low observed drift is expected and does not represent a production monitoring scenario with genuinely new incoming data.

17. Conclusion

This project demonstrates an end-to-end MLOps workflow for deploying and monitoring a machine learning prediction API.

The implementation covers explainability, fairness, containerization, Kubernetes deployment, autoscaling, CI/CD, cloud logging, performance testing, and input drift monitoring.

All OPPE-2 technical deliverables D2-D7 have been implemented and the repository has been pushed to GitHub.

D1 repository collaboration access has also been configured and accepted.
