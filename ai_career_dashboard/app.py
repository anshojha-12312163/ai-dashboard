import streamlit as st
from components import careerpredictor, progresstracker, timetracker, chatbot
from datetime import date

# Set page config
st.set_page_config(page_title="AI Career Dashboard", layout="wide", page_icon="🎓")

# ---------- Dummy Login System ----------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

def login_page():
    st.markdown("<h1 style='text-align: center;'>🔐 AI Career Dashboard Login</h1>", unsafe_allow_html=True)
    st.markdown("#### Please use the test credentials below:")
    st.code("Username: student\nPassword: pass123", language="bash")

    with st.form("login_form", clear_on_submit=True):
        st.markdown("### Login Credentials")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")
        if submitted:
            if username == "student" and password == "pass123":
                st.session_state.authenticated = True
            else:
                st.error("❌ Invalid username or password.")

# ---------- User Info Form ----------
def collect_user_info():
    st.markdown("<h2 style='text-align: center;'>🎓 Welcome! Let's Set Up Your Profile</h2>", unsafe_allow_html=True)
    
    with st.form("info_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("👤 Full Name")
            college = st.text_input("🏫 College Name")
            course = st.text_input("📘 Course / Branch")
        with col2:
            start_year = st.selectbox("🎓 Start Year", list(range(2015, date.today().year + 1)))
            end_year = st.selectbox("🎓 Graduation Year", list(range(2019, 2031)))
        
        submitted = st.form_submit_button("Save & Continue")
        if submitted:
            if not all([name, college, course]):
                st.warning("Please fill in all fields.")
            else:
                st.session_state.user_info = {
                    "name": name,
                    "college": college,
                    "course": course,
                    "start_year": start_year,
                    "end_year": end_year
                }
                st.session_state.info_done = True
                st.success("🎉 Profile saved successfully!")

# ---------- Sidebar Profile Card ----------
def show_sidebar_profile():
    user = st.session_state.get("user_info", {})
    st.sidebar.image("https://cdn-icons-png.flaticon.com/512/219/219983.png", width=100)
    st.sidebar.markdown(f"### 👤 {user.get('name', '')}")
    st.sidebar.markdown(f"🏫 *{user.get('college', '')}*")
    st.sidebar.markdown(f"📘 {user.get('course', '')}")
    st.sidebar.markdown(f"🎓 {user.get('start_year', '')} - {user.get('end_year', '')}")
    st.sidebar.markdown("---")

# ---------- Dashboard Main Tabs ----------
def show_dashboard():
    show_sidebar_profile()
    st.title("📊 AI Career Dashboard")

    with st.container():
        st.markdown("### 🚀 Choose a Section")
        tab1, tab2, tab3, tab4 = st.tabs([
            "🔮 Career Predictor", 
            "📈 Progress Tracker", 
            "⏱ Time Tracker", 
            "💬 Career Chatbot"
        ])

        with tab1:
            careerpredictor.run()
        with tab2:
            progresstracker.run()
        with tab3:
            timetracker.run()
        with tab4:
            chatbot.run()

# ---------- App Flow ----------
if not st.session_state.authenticated:
    login_page()
elif "info_done" not in st.session_state:
    collect_user_info()
else:
    show_dashboard()