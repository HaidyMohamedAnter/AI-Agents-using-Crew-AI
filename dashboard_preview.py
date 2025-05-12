import streamlit as st
import pandas as pd
import json
import matplotlib.pyplot as plt

def load_jobs(path="structured_jobs.json"):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def get_trends(jobs):
    df = pd.DataFrame(jobs)
    top_titles = df['title'].value_counts().nlargest(10)
    top_locations = df['location'].value_counts().nlargest(10)
    top_skills = df['skills'].explode().value_counts().nlargest(10)
    return top_titles, top_locations, top_skills


st.title("📊 AI/ML Jobs Trends in MENA (Preview)")

jobs = load_jobs()
titles, locations, skills = get_trends(jobs)

st.subheader("🔹 Top Job Titles")
st.bar_chart(titles)

st.subheader("🔸 Top Locations")
st.bar_chart(locations)

st.subheader("🟢 Top Skills")
st.bar_chart(skills)

st.info(f"Total Jobs Loaded: {len(jobs)}")
