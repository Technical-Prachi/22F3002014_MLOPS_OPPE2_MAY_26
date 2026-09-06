# AI Usage Documentation

Chatgpt chat Link - https://chatgpt.com/share/6a9d2f99-9ac8-83ee-bd75-33cc39f6f62b

## 1. Purpose

Generative AI tools were used as development assistance during the implementation of the MLOps OPPE-2 project.

AI assistance was used primarily for:

- Understanding assignment requirements
- Structuring the MLOps workflow
- Debugging implementation issues
- Generating initial code templates
- Troubleshooting Docker and Kubernetes configuration
- Troubleshooting GitHub Actions CI/CD
- Understanding SHAP and Fairlearn implementation
- Creating documentation and reports

All generated code and suggestions were reviewed, tested, and adapted before being included in the project.

---

## 2. Areas Where AI Assistance Was Used

### 2.1 Model Training

AI assistance was used to help structure the Logistic Regression training pipeline, including:

- Loading the dataset
- Handling missing values
- Encoding categorical variables
- Splitting the dataset
- Training the model
- Saving model artifacts using joblib

The resulting implementation was executed and validated in the GCP Vertex AI Workbench environment.

---

### 2.2 SHAP Explainability

AI assistance was used to help implement SHAP-based model explainability.

The implementation included:

- Loading the trained model
- Using SHAP LinearExplainer
- Calculating feature importance
- Generating a SHAP summary plot
- Creating a textual interpretation of feature importance

The generated results were independently executed and reviewed.

---

### 2.3 Fairlearn Analysis

AI assistance was used to help structure the Fairlearn analysis.

The implementation included:

- Creating age-based groups
- Calculating accuracy
- Calculating precision
- Calculating recall
- Calculating selection rate
- Calculating demographic parity difference
- Saving the fairness results

The assignment-required sensitive attribute was `age`.

---

### 2.4 FastAPI

AI assistance was used to help create the FastAPI serving layer.

The API implementation provides:

```text
GET /health
POST /predict

AI assistance helped with:

Request validation
Feature encoding
Model prediction
Response formatting
Error handling
Prediction logging

The API was manually tested before deployment.

2.5 Docker

AI assistance was used to help prepare:

Dockerfile
requirements.txt
.dockerignore

The Docker image was then built locally and pushed to Google Artifact Registry.

2.6 Kubernetes and GKE

AI assistance was used for Kubernetes configuration and troubleshooting.

This included:

Deployment configuration
LoadBalancer service
Health probes
Resource requests and limits
Horizontal Pod Autoscaling
GKE authentication
Troubleshooting deployment and service issues

The resulting Kubernetes resources were applied and verified on the GKE cluster.

2.7 GitHub Actions CI/CD

AI assistance was used extensively for troubleshooting the CI/CD pipeline.

The workflow performs:

GitHub checkout
Google Cloud authentication
Docker configuration
Docker image build
Artifact Registry push
GKE authentication
Kubernetes deployment update
Rollout verification

Workload Identity Federation was configured so that the GitHub Actions workflow could authenticate to Google Cloud without storing a long-lived service account JSON key.

The workflow was executed successfully through GitHub Actions.

2.8 Cloud Logging

AI assistance was used to help implement structured prediction logging.

Each prediction log contains:

Timestamp
Input features
Prediction

The logs were verified using Google Cloud Logging.

2.9 Load Testing

AI assistance was used to help prepare the wrk POST request script and load-testing command.

The final test used:

8 threads
2001 concurrent connections
30 seconds

The test output was reviewed to analyze:

Throughput
Latency
Latency percentiles
Socket errors
Timeouts
2.10 Input Drift

AI assistance was used to implement PSI-based input drift analysis.

The analysis compares:

Training data distribution
        vs
100-row prediction dataset

The results were saved as CSV and Markdown reports.

3. Human Verification and Responsibility

AI-generated suggestions were not treated as automatically correct.

The implementation was:

Executed in the GCP environment
Tested through terminal commands
Verified through Kubernetes commands
Verified through GitHub Actions
Verified through API requests
Verified through Cloud Logging
Verified through load testing
Reviewed through generated result files

The final implementation and submission decisions were made by the student.

4. AI Limitations Identified During the Project

During development, AI assistance occasionally produced suggestions that required modification or debugging.

Examples included:

Docker configuration issues
GitHub Actions authentication issues
GKE authentication requirements
Service deployment troubleshooting
Dependency/version compatibility considerations

These issues were resolved through iterative testing.

5. Security Considerations

No Google Cloud service-account private key was stored in the GitHub repository.

GitHub Actions authentication uses Workload Identity Federation.

Secrets and credentials were not intentionally included in source files.

6. Final Statement

AI tools were used as development and learning assistants rather than as a replacement for implementation, testing, or verification.

The student reviewed and executed the implementation and validated the final outputs in the GCP environment.
