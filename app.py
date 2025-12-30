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
    if study_duration >= 45 and idle_time <= 10 and breaks <= 2:
        st.success("🎯 Prediction: You are Focused")
    else:
        st.warning("⚠️ Prediction: You are Not Focused")

    st.write("Study Duration:", study_duration)
    st.write("Idle Time:", idle_time)
    st.write("Breaks:", breaks)
    st.write("Time of Day:", time_of_day)   
st.caption("Build by Prachi Patidar")
