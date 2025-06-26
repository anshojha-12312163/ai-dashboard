import streamlit as st
import datetime
import pandas as pd
import plotly.express as px

def run():
    st.subheader("⏱ Time Tracker & Productivity Log")
    st.markdown("Track your study/focus sessions. Get weekly stats and motivation.")

    if "focus_log" not in st.session_state:
        st.session_state.focus_log = []

    st.markdown("### 🔵 Log a Focus Session")
    with st.form("focus_form"):
        task = st.text_input("Task or Subject")
        duration = st.slider("How many minutes did you focus?", 15, 180, step=15)
        notes = st.text_area("Any notes or distractions?")
        submitted = st.form_submit_button("Add Session")

        if submitted and task:
            st.session_state.focus_log.append({
                "Date": datetime.date.today().strftime("%Y-%m-%d"),
                "Task": task,
                "Duration": duration,
                "Notes": notes
            })
            st.success(f"Logged {duration} mins for {task}")

    if st.session_state.focus_log:
        df = pd.DataFrame(st.session_state.focus_log)

        st.markdown("### 📅 Focus History")
        st.dataframe(df, use_container_width=True)

        st.markdown("### 📈 Weekly Focus Chart")
        focus_df = df.groupby("Date")["Duration"].sum().reset_index()
        fig = px.bar(focus_df, x="Date", y="Duration", title="Focus Minutes Per Day", color="Duration", color_continuous_scale="Tealgrn")
        st.plotly_chart(fig, use_container_width=True)

        total = df["Duration"].sum()
        st.info(f"✅ You’ve focused for *{total} minutes* in total!")