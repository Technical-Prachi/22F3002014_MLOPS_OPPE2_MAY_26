import json
import logging
from datetime import datetime, timezone

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Heart Disease Prediction API", version="1.0")

model = joblib.load("artifacts/heart_disease_model.joblib")
gender_encoder = joblib.load("artifacts/gender_encoder.joblib")
target_encoder = joblib.load("artifacts/target_encoder.joblib")
feature_columns = joblib.load("artifacts/feature_columns.joblib")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("heart-api")


@app.get("/")
def root():
    return {
        "service": "Heart Disease Prediction API",
        "status": "healthy"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict")
def predict(features: dict):
    try:
        input_df = pd.DataFrame([features])

        missing = [c for c in feature_columns if c not in input_df.columns]

        if missing:
            raise HTTPException(
                status_code=400,
                detail=f"Missing features: {missing}"
            )

        input_df = input_df[feature_columns].copy()

        # Encode gender BEFORE numeric conversion
        if isinstance(input_df.loc[0, "gender"], str):
            gender_value = input_df.loc[0, "gender"].strip().lower()

            if gender_value not in ["male", "female"]:
                raise HTTPException(
                    status_code=400,
                    detail="gender must be male or female"
                )

            input_df["gender"] = gender_encoder.transform([gender_value])

        # Convert all columns to numeric
        for col in feature_columns:
            input_df[col] = pd.to_numeric(input_df[col], errors="raise")

        prediction = int(model.predict(input_df)[0])

        prediction_label = target_encoder.inverse_transform(
            [prediction]
        )[0]

        timestamp = datetime.now(timezone.utc).isoformat()

        log_record = {
            "timestamp": timestamp,
            "features": features,
            "prediction": prediction_label
        }

        logger.info(json.dumps(log_record))

        return {
            "prediction": prediction_label,
            "prediction_encoded": prediction,
            "timestamp": timestamp
        }

    except HTTPException:
        raise

    except Exception as e:
        logger.exception("Prediction failed")
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
