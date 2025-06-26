import streamlit as st
import plotly.express as px

def run():
    st.subheader("🔮 Career Recommendation Engine")
    st.markdown("Fill in the details below to get personalized career recommendations based on your *skills, **interests, and **values*.")

    with st.form("career_form"):
        col1, col2 = st.columns(2)

        with col1:
            skills = st.multiselect(
                "Select Your Skills",
                ['Python', 'Data Analysis', 'Design Thinking', 'Communication', 'Problem Solving', 'Marketing', 'Creativity'],
                help="Choose at least 3 skills you are confident in."
            )
            experience_level = st.slider("Rate Your Experience (Overall)", 1, 10, 5)

        with col2:
            interest_area = st.selectbox(
                "What Are You Interested In?",
                ['Technology', 'Business', 'Design', 'Research', 'Arts', 'Social Work']
            )
            work_style = st.radio(
                "Preferred Work Style",
                ['Remote', 'Hybrid', 'On-site']
            )

        values = st.selectbox("What Do You Value Most?", ['High Salary', 'Work-Life Balance', 'Impact', 'Stability'])

        submitted = st.form_submit_button("🔎 Get Career Suggestions")

    if submitted:
        st.success("✅ Top Career Matches Based on Your Profile:")

        # --- Simulated AI Prediction ---
        recommended_careers = ['Data Analyst', 'UX Designer', 'Business Consultant']
        match_scores = [88, 81, 74]

        # --- Display Results in Cards ---
        for i in range(len(recommended_careers)):
            with st.container():
                st.markdown(f"### {recommended_careers[i]}")
                st.progress(match_scores[i])
                st.markdown(f"*Match Score:* {match_scores[i]}%")
                st.markdown(f"*Why this fits you:* Great for {interest_area} with your skills in {', '.join(skills[:2])}.")

        # --- Graph of Career Scores ---
        fig = px.bar(
            x=recommended_careers,
            y=match_scores,
            labels={'x': "Career", 'y': "Fit Score"},
            title="🎯 Career Fit Comparison",
            color=match_scores,
            color_continuous_scale="Tealgrn"
        )
        st.plotly_chart(fig, use_container_width=True)

        # --- Learning Plan Preview ---
        st.markdown("### 📚 Suggested Learning Path for Your Top Match")
        st.info(
            "*Career Path: Data Analyst*\n\n"
            "- Learn Python and SQL (Weeks 1–4)\n"
            "- Master Excel and Tableau (Weeks 5–7)\n"
            "- Take a Data Analytics course on Coursera or Udemy\n"
            "- Work on 2-3 real-world datasets\n"
            "- Create a GitHub portfolio and start applying!"
        )

        # --- Future Enhancement Placeholder ---
        st.caption("Coming soon: GPT-powered roadmap generator + links to top courses from Udemy/Coursera/EdX.")