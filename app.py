import streamlit as st
import pandas as pd

# Load dataset
df = pd.read_csv("StudentsPerformance.csv")

# Dashboard Title
st.title("Student Performance Analysis Dashboard")

# Show Dataset
st.subheader("Dataset Preview")
st.dataframe(df)

# Statistics
st.subheader("Statistical Summary")
st.write(df.describe())

# Average Scores
st.subheader("Average Scores")

avg_scores = df[['math score',
                 'reading score',
                 'writing score']].mean()

st.bar_chart(avg_scores)