# 📊 Employment Prediction System

## 🌐 Live Demo

🚀 **Try the Application Here**

http://54.242.240.207:8502/

The application predicts the estimated number of employed people based on unemployment statistics, labour participation rate, region, area type, and date information using Machine Learning.

---

# 📌 Project Overview

The Employment Prediction System is an end-to-end Machine Learning project developed to estimate the number of employed people in a given region using historical unemployment data and socio-economic indicators.

The project covers the complete Machine Learning lifecycle:

* Data Collection
* Data Cleaning
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Model Training
* Model Evaluation
* Model Deployment
* API Development
* Cloud Deployment on AWS EC2

The trained model is served through FastAPI and integrated with a Streamlit web application for real-time predictions.

---

# 🎯 Problem Statement

Employment trends play a crucial role in economic planning and workforce management.

This project aims to predict the estimated employed population using factors such as:

* Region
* Area Type (Urban/Rural)
* Unemployment Rate
* Labour Participation Rate
* Date Information

The prediction helps in understanding employment patterns and workforce distribution across different regions.

---

# 📂 Dataset

### Dataset Used

**Unemployment in India Dataset**

The dataset contains unemployment statistics collected from different regions of India.

### Features

| Feature                       | Description                                            |
| ----------------------------- | ------------------------------------------------------ |
| Region                        | State/Region Name                                      |
| Area                          | Urban or Rural                                         |
| Unemployment Rate (%)         | Percentage of unemployed population                    |
| Labour Participation Rate (%) | Percentage of population participating in labour force |
| Day                           | Day extracted from date                                |
| Month                         | Month extracted from date                              |
| Year                          | Year extracted from date                               |

### Target Variable

| Target             |
| ------------------ |
| Estimated Employed |

---

# 🔍 Exploratory Data Analysis (EDA)

The following analyses were performed:

* Missing Value Analysis
* Data Cleaning
* Distribution Analysis
* Correlation Analysis
* Employment Trend Analysis
* Feature Relationship Visualization
* Outlier Detection

---

# ⚙️ Data Preprocessing

The following preprocessing steps were applied:

* Missing Value Handling
* Categorical Feature Encoding
* Feature Selection
* Date Feature Extraction
* Data Transformation
* Train-Test Split

---

# 🤖 Machine Learning Model

The project uses the **XGBoost Regressor** algorithm for prediction.

### Why XGBoost?

* High Prediction Accuracy
* Handles Complex Relationships
* Fast Training
* Robust Performance
* Excellent Generalization

---

# 🏗️ Project Architecture

Dataset → Data Preprocessing → Feature Engineering → XGBoost Model → FastAPI Backend → Streamlit Frontend → AWS EC2 Deployment

---

# 📁 Project Structure

```bash
Employed-People/
│
├── backend/
│   └── main.py
│
├── frontend/
│   └── app.py
│
├── Dataset/
│   └── Unemployment in India.csv
│
├── model_dir/
│   └── xgb_model.joblib
│
├── .env
├── requirements.txt
├── README.md
└── env_template.txt
```

# 🛠️ Technologies Used

### Programming Language

* Python

### Machine Learning

* Scikit-Learn
* XGBoost
* Pandas
* NumPy

### Backend

* FastAPI
* Uvicorn

### Frontend

* Streamlit

### Deployment

* AWS EC2
* Linux

### Development Tools

* Jupyter Notebook
* VS Code
* Git
* GitHub

---

# 🚀 FastAPI Endpoints

## Health Check

```http
GET /status
```

Response:

```json
{
    "message": "Unemployment Prediction API is running 🚀"
}
```

## Prediction Endpoint

```http
POST /predict
```

Request Example:

```json
{
    "region": "Andhra Pradesh",
    "unemployment_rate": 3.05,
    "labour_participate_rate": 42.05,
    "area": "Urban",
    "day": 30,
    "month": 6,
    "year": 2024
}
```

Response Example:

```json
{
    "prediction": 5123456.78
}
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/SaurabhAgrawal121102/Employed-People.git
```

```bash
cd Employed-People
```

## Create Virtual Environment

```bash
python -m venv .venv
```

## Activate Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux

```bash
source .venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run FastAPI Server

```bash
uvicorn backend.main:app --host 0.0.0.0 --port 7000
```

### Run in Background

```bash
nohup uvicorn backend.main:app --host 0.0.0.0 --port 7000 > uvicorn.log 2>&1 &
```

---

# 🎨 Run Streamlit Application

```bash
streamlit run frontend/app.py --server.port 8502
```

### Run in Background

```bash
nohup streamlit run frontend/app.py --server.port 8502 > streamlit.log 2>&1 &
```

---

# ☁️ Deployment

The project is deployed on:

* AWS EC2 Instance
* Ubuntu Linux Server
* FastAPI Backend
* Streamlit Frontend

Live Application:

http://54.242.240.207:8502/

---

# 📊 Future Enhancements

* Interactive Dashboard
* Real-Time Employment Analytics
* Automated Model Retraining
* Docker Containerization
* CI/CD Integration
* Advanced Forecasting Models

---

# 👨‍💻 Author

### Saurabh Agrawal

Machine Learning Enthusiast | Python Developer | Data Science Learner

GitHub: https://github.com/SaurabhAgrawal121102

---

# ⭐ Support

If you found this project useful, please consider:

⭐ Starring the repository

🍴 Forking the repository

📢 Sharing the project with others

Thank you for visiting this project!
