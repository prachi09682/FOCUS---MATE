import streamlit as st

st.set_page_config(page_title="Focus Mate", layout="centered")

st.title("🎯 Focus Mate")
st.subheader("Study Focus Predictor")

st.write("Enter your study details below:")

study_duration = st.number_input("Study Duration (minutes)", min_value=0, step=10)
idle_time = st.number_input("Idle Time (minutes)", min_value=0, step=1)
breaks = st.number_input("Number of Breaks", min_value=0, step=1)

time_of_day = st.selectbox(
    "Time of Day",
    ["morning", "afternoon", "evening", "night"]
)

if st.button("Predict Focus"):
    st.success("✅ Input received successfully!")
    st.write("Prediction feature can be connected to ML model.")

st.caption("Built by Prachi Patidar")
