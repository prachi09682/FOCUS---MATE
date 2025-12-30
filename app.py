import streamlit as st
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Focus Mate",
    page_icon="🎯",
    layout="centered"
)

# ---------------- TITLE ----------------
st.title("🎯 Focus Mate")
st.caption("Built by Prachi Patidar")

st.write("A simple study companion to help you focus better.")

st.divider()

# ---------------- INPUTS ----------------
study_duration = st.number_input(
    "Study Duration (minutes)",
    min_value=1,
    max_value=300,
    value=25
)

break_duration = st.number_input(
    "Break Duration (minutes)",
    min_value=1,
    max_value=60,
    value=5
)

task_name = st.text_input(
    "What are you studying right now?",
    placeholder="Eg: Physics, Coding, Maths"
)

st.divider()

# ---------------- START BUTTON ----------------
if st.button("🚀 Start Focus Session"):
    if task_name.strip() == "":
        st.warning("Please enter what you are studying.")
    else:
        st.success(f"Focus session started for **{task_name}**")

        # Study Timer
        st.write("⏳ Study time started...")
        study_seconds = int(study_duration * 60)

        progress_bar = st.progress(0)
        for i in range(study_seconds):
            time.sleep(1)
            progress_bar.progress((i + 1) / study_seconds)

        st.success("✅ Study session completed!")

        # Break Timer
        st.write("☕ Break time started...")
        break_seconds = int(break_duration * 60)

        progress_bar = st.progress(0)
        for i in range(break_seconds):
            time.sleep(1)
            progress_bar.progress((i + 1) / break_seconds)

        st.success("🎉 Break over! Ready for the next session.")

st.divider()

# ---------------- FOOTER ----------------
st.markdown(
    "<center>💡 Stay consistent. Small focus sessions build big results.</center>",
    unsafe_allow_html=True
)

