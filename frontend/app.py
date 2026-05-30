import streamlit as st
import requests
import os
from dotenv import load_dotenv

# =========================
# LOAD ENV
# =========================
load_dotenv()
API_URL = st.secrets.get("API_URL")
# Safety check
if not API_URL:
    st.error("❌ API_URL not found in .env file")
    st.stop()

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Employment Prediction App",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Employment Prediction System")
st.write("Enter details to get ML prediction from FastAPI backend")

# =========================
# INPUTS
# =========================
st.sidebar.header("📌 Input Features")

region = st.sidebar.text_input("Region", "Andhra Pradesh")
area = st.sidebar.selectbox("Area", ["Urban", "Rural"])

unemployment_rate = st.sidebar.number_input("Unemployment Rate (%)", value=3.05)
labour_participate_rate = st.sidebar.number_input("Labour Participation Rate (%)", value=42.05)

day = st.sidebar.number_input("Day", 1, 31, 30)
month = st.sidebar.number_input("Month", 1, 12, 6)
year = st.sidebar.number_input("Year", 2000, 2100, 2024)

# =========================
# PREDICT BUTTON
# =========================
if st.button("🚀 Predict"):

    payload = {
        "region": region,
        "unemployment_rate": unemployment_rate,
        "labour_participate_rate": labour_participate_rate,
        "area": area,
        "day": day,
        "month": month,
        "year": year
    }

    try:
        url = f"{API_URL}/predict"

        st.write("API URL:", url)

        response = requests.post(url, json=payload)

        st.write("Status Code:", response.status_code)
        st.write("Response:", response.text)

        if response.status_code == 200:
            result = response.json()

            st.success("✅ Prediction Successful")
            st.json(result)

        else:
            st.error(f"❌ API Error ({response.status_code})")

    except Exception as e:
        st.error(f"❌ Connection Error: {e}")