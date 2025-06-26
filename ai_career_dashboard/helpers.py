# helpers.py
import pandas as pd
import streamlit as st

@st.cache_data
def load_career_data(path="career_pathway_dashboard.csv"):
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        st.error("CSV file not found.")
        return pd.DataFrame()
