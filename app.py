import joblib
import pandas as pd
import streamlit as st
st.title("Focus Mate")
st.caption("Built by Prachi Patidar")

# Load trained model
model = joblib.load("model_focus.pkl")

print("📘 Study Focus Predictor")
print("------------------------")

# Take user input
study_duration = int(input("Enter study duration (minutes): "))
idle_time = int(input("Enter idle time (minutes): "))
breaks = int(input("Enter number of breaks: "))
time_of_day = input("Enter time of day (morning/afternoon/night): ").lower()

# Convert time_of_day to number
if time_of_day == "morning":
    time_of_day = 0
elif time_of_day == "afternoon":
    time_of_day = 1
elif time_of_day == "night":
    time_of_day = 2
else:
    print("❌ Invalid time of day")
    exit()

# Create input DataFrame
input_data = pd.DataFrame({
    "study_duration": [study_duration],
    "idle_time": [idle_time],
    "break": [breaks],
    "time of day": [time_of_day]
})

# Predict
prediction = model.predict(input_data)

# Output
if prediction[0] == 1:
    print("\n✅ You are likely to be FOCUSED")
else:

    print("\n❌ You are likely to be NOT FOCUSED")
