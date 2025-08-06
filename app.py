import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load("house_price_model.pkl")

# Streamlit app UI
st.set_page_config(page_title="House Price Predictor", layout="centered")
st.title("🏠 Bangalore House Price Predictor")

# User inputs
sqft = st.number_input("Total Square Feet (e.g., 1000)", min_value=300)
bath = st.number_input("Number of Bathrooms", min_value=1, step=1)
bhk = st.number_input("Number of Bedrooms (BHK)", min_value=1, step=1)

# NOTE: Simplified version: We don't include location & area_type to keep the model usable for now
# In advanced version, we can one-hot encode inputs too

# Predict Button
if st.button("Predict Price"):
    # Build input array — adjust this part if your model expects location/area_type
    input_data = np.zeros(1220)  # 1220 = number of features in X (excluding price)
    input_data[0] = sqft
    input_data[1] = bath
    input_data[2] = bhk

    # Reshape and predict
    prediction = model.predict([input_data])[0]
    st.success(f"🏷️ Estimated Price: ₹ {round(prediction * 1_00_000, 2)} INR")
