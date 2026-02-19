import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("Machine_efficiency.pkl")

st.set_page_config(page_title="Machine Efficiency Prediction", layout="centered")

st.title("🏭 Industrial Machine Efficiency Prediction")
st.write("Predict whether machine efficiency will drop significantly or not.")

st.markdown("---")

st.sidebar.header("Enter Machine Values")

# Sidebar Inputs (MATCHING DATASET)
vibration = st.sidebar.number_input("Vibration", format="%.3f")
acoustic = st.sidebar.number_input("Acoustic[Sound Intensity in dB]", format="%.3f")
temperature = st.sidebar.number_input("Temperature (°C)", format="%.2f")
current = st.sidebar.number_input("Current (Ampere)", format="%.2f")
imf1 = st.sidebar.number_input("IMF_1", format="%.3f")
imf2 = st.sidebar.number_input("IMF_2", format="%.3f")
imf3 = st.sidebar.number_input("IMF_3", format="%.3f")

# Create input dataframe
input_data = pd.DataFrame({
    'vibration': [vibration],
    'acoustic': [acoustic],
    'temperature': [temperature],
    'current': [current],
    'IMF_1': [imf1],
    'IMF_2': [imf2],
    'IMF_3': [imf3]
})

st.write("### 📋 Input Data")
st.write(input_data)

# Prediction
if st.button("Predict Efficiency"):
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ Efficiency Drop Predicted![Maintenance Required]")
    else:
        st.success("✅ Machine Operating Normally.")
