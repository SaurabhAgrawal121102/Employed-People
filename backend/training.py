import numpy as np
import pandas as pd
import os
import logging
from dotenv import load_dotenv

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer

import joblib

# Load environment variables
load_dotenv()


def train_model():

    # ================= ENV VARIABLES =================
    DATASET_NAME = os.getenv("DATASET_NAME")
    MODEL_FILENAME = os.getenv("MODEL_FILENAME")
    MODEL_DIR = os.getenv("MODEL_DIR")
    TARGET_COLUMN = os.getenv("TARGET_COLUMN")
    TEST_SIZE = float(os.getenv("TEST_SIZE"))
    LOG_DIR = os.getenv("LOG_DIR")
    LOG_NAME = os.getenv("LOG_NAME")

    if not all([DATASET_NAME, MODEL_FILENAME, MODEL_DIR, TARGET_COLUMN, TEST_SIZE, LOG_DIR, LOG_NAME]):
        raise ValueError("Missing environment variables in .env file")

    # ================= LOGGING =================
    os.makedirs(LOG_DIR, exist_ok=True)
    logging.basicConfig(
        filename=os.path.join(LOG_DIR, LOG_NAME),
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    try:
        # ================= LOAD DATA =================
        data = pd.read_csv(DATASET_NAME)

        if TARGET_COLUMN not in data.columns:
            raise ValueError(f"Target column '{TARGET_COLUMN}' not found")
        data = data[data[TARGET_COLUMN].notna()]
        X = data.drop(TARGET_COLUMN, axis=1)
        y = data[TARGET_COLUMN]

        # ================= COLUMN TYPES =================
        categorical_cols = X.select_dtypes(include=['object']).columns
        numerical_cols = X.select_dtypes(exclude=['object']).columns

        # ================= NUMERIC PIPELINE =================
        numeric_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler())
        ])

        # ================= CATEGORICAL PIPELINE =================
        categorical_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('onehot', OneHotEncoder(handle_unknown='ignore'))
        ])

        # ================= PREPROCESSOR =================
        preprocessor = ColumnTransformer(
            transformers=[
                ('num', numeric_transformer, numerical_cols),
                ('cat', categorical_transformer, categorical_cols)
            ]
        )

        # ================= MODEL PIPELINE =================
        model = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('regressor', LinearRegression())
        ])

        # ================= TRAIN TEST SPLIT =================
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=TEST_SIZE, random_state=42
        )

        # ================= TRAIN MODEL =================
        model.fit(X_train, y_train)

        # ================= PREDICT =================
        y_pred = model.predict(X_test)

        # ================= EVALUATION =================
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)

        logging.info(f"MSE: {mse}")
        logging.info(f"RMSE: {rmse}")
        logging.info(f"R2 Score: {r2}")
        logging.info(f"MAE: {mae}")

        # ================= SAVE MODEL =================
        os.makedirs(MODEL_DIR, exist_ok=True)
        model_path = os.path.join(MODEL_DIR, MODEL_FILENAME)

       

        logging.info(f"Model saved at {model_path}")

        print("✅ Training completed successfully!")
        print("📦 Model saved at:", model_path)

    except Exception as e:
        logging.error(f"Error during training: {e}")
        print("❌ Error:", e)


if __name__ == "__main__":
    train_model()