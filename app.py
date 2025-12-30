# app.py
import streamlit as st
import pandas as pd
import joblib

# -----------------------
# Load model
# -----------------------
try:
    model = joblib.load("model_focus.pkl")
except:
    st.error("Model file not found. Please upload 'model_focus.pkl' in the same folder.")

# -----------------------
# App Title
# -----------------------
st.title("Focus Mate")
st.caption("Built by Prachi Patidar")

# -----------------------
# Input Fields
# -----------------------
study_duration = st.number_input("Study Duration (minutes)", min_value=0, value=60)
idle_time = st.number_input("Idle Time (minutes)", min_value=0, value=10)
num_breaks = st.number_input("Number of Breaks", min_value=0, value=2)
time_of_day = st.selectbox("Time of Day", ["morning", "afternoon", "night"])

# Map time of day to numeric values as model expects
time_map = {"morning": 0, "afternoon": 1, "night": 2}

# Prepare input data in dataframe for model
input_data = pd.DataFrame({
    "study_duration": [study_duration],
    "idle_time": [idle_time],
    "break": [num_breaks],
    "time_of_day": [time_map[time_of_day]]
})

# -----------------------
# Prediction Button
# -----------------------
if st.button("Predict Focus"):
    try:
        prediction = model.predict(input_data)[0]
        if prediction == 1:
            st.success("✅ You are Focused!")
        else:
            st.error("❌ You are Not Focused.")
    except Exception as e:
        st.error(f"Error in prediction: {e}")
