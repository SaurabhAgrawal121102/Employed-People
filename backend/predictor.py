import joblib
import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get environment variables
MODEL_DIR = os.getenv("MODEL_DIR")
MODEL_FILENAME = os.getenv("MODEL_FILENAME")

# Build full path
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_FILENAME)

# Load model
model = joblib.load(MODEL_PATH)


def unemployment_prediction(
    region,
    unemployment_rate,
    labour_participate_rate,
    area,
    day,
    month,
    year
):

    input_data = pd.DataFrame([{
        "region": region,
        "unemployment_rate (%)": unemployment_rate,
        "labour_participate_rate (%)": labour_participate_rate,
        "area": area,
        "day": day,
        "month": month,
        "year": year
    }])

    prediction = model.predict(input_data)
    

    return prediction[0]


if __name__ == "__main__":

    # price = unemployment_prediction(
    #     region="Andhra Pradesh",
    #     unemployment_rate=3.05,
    #     labour_participate_rate=42.05,
    #     area="Rural",
    #     day=30,
    #     month=6,
    #     year=2019
    # )

    # print("Predicted Value:", price)