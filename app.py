import streamlit as st
import openai
import pandas as pd

# OpenAI API Key (Replace with your key or use env variables)
openai.api_key = "AIzaSyDXRM5ejT1rSCfJr_-qRlMQEfJVwW-co0o"

# Function to generate study plan using OpenAI API
def generate_study_plan(subject, hours_per_day, days):
    prompt = f"Create a {days}-day study plan for {subject}, studying {hours_per_day} hours per day."
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are an AI study planner."},
                  {"role": "user", "content": prompt}]
    )
    
    return response['choices'][0]['message']['content']

# Streamlit UI
st.set_page_config(page_title="AI Study Planner", layout="wide")

st.title("📚 AI-Powered Study Planner")

# User Inputs
subject = st.text_input("Enter Subject (e.g., Math, Physics)")
hours_per_day = st.slider("Study Hours Per Day", 1, 10, 3)
days = st.slider("Study Duration (Days)", 1, 30, 7)

if st.button("Generate Study Plan"):
    if subject:
        study_plan = generate_study_plan(subject, hours_per_day, days)
        st.subheader("📅 Your Study Plan")
        st.write(study_plan)
    else:
        st.error("Please enter a subject!")

