from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# =========================
# Load Model
# =========================
MODEL_DIR = os.getenv("MODEL_DIR")
MODEL_FILENAME = os.getenv("MODEL_FILENAME")

MODEL_PATH = os.path.join(MODEL_DIR, MODEL_FILENAME)
print(f"Loading model from: {MODEL_PATH}")

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model not found: {MODEL_PATH}")

model = joblib.load(MODEL_PATH)

# =========================
# FastAPI App
# =========================
app = FastAPI(title="Unemployment Prediction API")


# =========================
# Input Schema (POST body)
# =========================
class InputData(BaseModel):
    region: str
    unemployment_rate: float
    labour_participate_rate: float
    area: str
    day: int
    month: int
    year: int


# =========================
# GET Endpoint (Health Check)
# =========================
@app.get("/status")
def status():
    return {
        "message": "Unemployment Prediction API is running 🚀"
    }


# =========================
# POST Endpoint (Prediction)
# =========================
@app.post("/predict")
def predict(data: InputData):

    input_df = pd.DataFrame([{
        "region": data.region,
        "unemployment_rate (%)": data.unemployment_rate,
        "labour_participate_rate (%)": data.labour_participate_rate,
        "area": data.area,
        "day": data.day,
        "month": data.month,
        "year": data.year
    }])

    prediction = model.predict(input_df)[0]

    # ✅ FIX FASTAPI SERIALIZATION ERROR
    prediction = float(prediction)

    return {
        "prediction": prediction
    }