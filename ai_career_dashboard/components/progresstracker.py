import streamlit as st
import pandas as pd
import plotly.express as px

def run():
    st.subheader("📈 Academic Progress Tracker")
    st.markdown("Upload your grades CSV to visualize your academic progress. Include at least these columns: Subject, Marks, Semester.")

    sample_data = {
        'Subject': ['Math', 'Science', 'English', 'CS', 'History'],
        'Marks': [85, 75, 90, 95, 70],
        'Semester': ['Sem 1'] * 5
    }

    uploaded_file = st.file_uploader("Upload your grade file", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.DataFrame(sample_data)
        st.info("Using sample data. Upload a CSV to try with your own.")

    if 'Subject' in df.columns and 'Marks' in df.columns:
        st.dataframe(df, use_container_width=True)

        st.markdown("### 📊 Subject-wise Performance")
        fig = px.bar(df, x="Subject", y="Marks", color="Marks", color_continuous_scale="Aggrnyl")
        st.plotly_chart(fig, use_container_width=True)

        avg = df["Marks"].mean()
        lowest = df[df["Marks"] == df["Marks"].min()]["Subject"].values[0]
        st.success(f"📘 Your average score is *{avg:.2f}*")
        st.warning(f"⚠ You may want to improve in *{lowest}*")

        if "Semester" in df.columns:
            st.markdown("### 🧭 Trend Across Semesters")
            trend = px.line(df, x="Semester", y="Marks", color="Subject", markers=True)
            st.plotly_chart(trend, use_container_width=True)

    else:
        st.error("Your CSV must include 'Subject' and 'Marks' columns.")