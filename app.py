import streamlit as st

# =================================================
# PAGE CONFIG
# =================================================
st.set_page_config(
    page_title="Placement-Preparation-Dashboard",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =================================================
# AUTH MODULES
# =================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user" not in st.session_state:
    st.session_state.user = None

if "login_time" not in st.session_state:
    st.session_state.login_time = None

if "active_menu" not in st.session_state:
    st.session_state.active_menu = "🏠 Overview"



from auth.login import login_ui
from auth.register import register_ui

# =================================================
# DASHBOARD MODULES
# =================================================
from dashboard.overview import overview_ui

# =================================================
# PREPARATION MODULES
# =================================================
from preparation.dsa import dsa_ui
from preparation.aptitude import aptitude_ui
from preparation.core_subjects import core_subjects_ui
from projects.project_tracker import project_tracker_ui
from preparation.conding_contests import coding_contests_ui

# =================================================
# COMPANY MODULES
# =================================================
from companies.tcs import tcs_ui
from companies.sap import sap_ui
from companies.infosys import infosys_ui
from companies.wipro import wipro_ui
from companies.accenture import accenture_ui
from companies.product_based import product_based_ui
from companies.service_based import service_based_ui
from companies.all_companies import all_companies_ui
from companies.deloitte import deloitte_ui

# =================================================
# CAREER MODULES
# =================================================
from resume.resume_upload import resume_upload_ui
from interview.hr_questions import hr_ui
from interview.mock_interview import mock_interview_ui
from career.internships import internships_ui
from career.offcampus import offcampus_ui

# =================================================
# SETTINGS MODULES
# =================================================
from settings.profile import profile_ui
from settings.logout import logout_ui

# =================================================
# SESSION STATE
# =================================================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# =================================================
# AUTH FLOW
# =================================================
if not st.session_state.logged_in:

    st.sidebar.title("🔐 Authentication")
    auth_menu = st.sidebar.radio("Select Option", ["Register", "Login"])

    st.markdown("""
        <h1 style='text-align:center;font-size:42px;'>🎓 Placement-Preparation-Dashboard</h1>
        <p style='text-align:center;color:gray;font-size:18px;'>
        One complete platform for B.Tech, M.Tech & MCA students
        </p>
    """, unsafe_allow_html=True)

    if auth_menu == "Register":
        register_ui()
    else:
        login_ui()
    st.stop()

    if st.session_state.login_time is None:
        st.session_state.login_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    

# =================================================
# MAIN DASHBOARD
# =================================================
else:

    # ================= SIDEBAR STYLING =================
    st.markdown("""
    <style>
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f172a, #020617);
        padding-top: 20px;
    }
    section[data-testid="stSidebar"] span {
        font-size: 20px !important;
    }
    section[data-testid="stSidebar"] label {
        font-size: 17px !important;
    }
    .sidebar-divider {
        margin: 18px 0;
        border-top: 1px solid #334155;
    }
    </style>
    """, unsafe_allow_html=True)

    # =================================================
    # WELCOME BANNER
    # =================================================
    st.markdown(
        f"""
        <div style="
            background: linear-gradient(90deg,#0f766e,#10b981);
            padding:18px;
            border-radius:14px;
            color:white;
            margin-bottom:18px;
        ">
            <h3 style="margin:0;">👋 Welcome Back!</h3>
            <p style="margin:0;font-size:16px;">
            Logged in as <b>{st.session_state.user}</b> | Session Active
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


    # ================= SIDEBAR HEADER =================
    st.sidebar.markdown("## ** 📌 NAVIGATION PANEL **")
    st.sidebar.caption("Placement Control Center")

    # ================= USER SNAPSHOT =================
    st.sidebar.markdown("### 👤 STUDENT SNAPSHOT")
    st.sidebar.markdown("**Name:** Rajneesh kushwaha")
    st.sidebar.markdown("**Branch:** CSE(AIML)")
    st.sidebar.markdown("**Target:** Product + Service Companies")

    st.sidebar.markdown("<div class='sidebar-divider'></div>", unsafe_allow_html=True)

    # ================= PROGRESS ANALYTICS =================
    st.sidebar.markdown("### 📊 ** PROGRESS ANALYTICS **")

    st.sidebar.markdown("**DSA Completion**")
    st.sidebar.progress(0.68)

    st.sidebar.markdown("**Aptitude Accuracy**")
    st.sidebar.progress(0.72)

    st.sidebar.markdown("**Core Subjects Coverage**")
    st.sidebar.progress(0.55)

    st.sidebar.markdown("<div class='sidebar-divider'></div>", unsafe_allow_html=True)

    # ================= DAILY STUDY PLANNER =================
    st.sidebar.markdown("### 🗓 Daily Study Planner")
    st.sidebar.checkbox("Solve 3 DSA Problems")
    st.sidebar.checkbox("Revise OS / DBMS")
    st.sidebar.checkbox("1 Coding Contest Question")
    st.sidebar.checkbox("HR Interview Practice")

    st.sidebar.markdown("<div class='sidebar-divider'></div>", unsafe_allow_html=True)

    # ================= MAIN NAVIGATION =================
    st.markdown("""
        <style>
        /* ===== TARGET ONLY SIDEBAR RADIO MENU ===== */
        section[data-testid="stSidebar"] div[role="radiogroup"] label {
            font-size: 20px !important;
            text-transform: uppercase;
            letter-spacing: 0.6px;
            padding: 10px 14px;
            margin-bottom: 6px;
            border-radius: 10px;
            transition: all 0.25s ease;
        }

        /* Hover Effect */
        section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
            background: rgba(16, 185, 129, 0.15);
            transform: translateX(4px);
        }

        /* Selected Item */
        section[data-testid="stSidebar"] div[role="radiogroup"] label[data-selected="true"] {
            background: linear-gradient(90deg, #0f766e, #10b981);
            color: white !important;
            font-weight: 700;
        }

        /* Radio Circle Bigger */
        section[data-testid="stSidebar"] input[type="radio"] {
            transform: scale(1.3);
            margin-right: 12px;
        }
        </style>
    """, unsafe_allow_html=True)

    menu = st.sidebar.radio(
        "🚀 ** SELECT MODULE **",
        [
            "🏠 Overview",

            "📘 DSA Tracker",
            "🧮 Aptitude Tracker",
            "📚 Core Subjects",
            "🛠 Projects & Research",
            "🏆 Coding Contests",

            "🏢 Service-Based Companies",
            "🚀 Product-Based Companies",
            "⌛ All Companies",

            "📄 Resume Manager",
            "🎤 HR Interview",
            "🤖 Mock Interview",

            "💼 Internships",
            "🌐 Off-Campus Jobs",

            "👤 My Profile",
            "🚪 Logout"
        ]
    )

    st.sidebar.markdown("<div class='sidebar-divider'></div>", unsafe_allow_html=True)

    # ================= QUICK ACTIONS =================
    st.sidebar.markdown("### ⚡ Quick Actions")
    st.sidebar.button("📄 Upload Resume")
    st.sidebar.button("🧠 Take Mock Interview")
    st.sidebar.button("🏆 Practice Coding")
    st.sidebar.button("📊 View Analytics")

    st.sidebar.markdown("<div class='sidebar-divider'></div>", unsafe_allow_html=True)

    # ================= SMART TOOLS =================
    st.sidebar.markdown("### 🤖 Smart Tools")
    st.sidebar.toggle("AI Study Suggestions")
    st.sidebar.toggle("Daily Reminder Alerts")
    st.sidebar.toggle("Weekly Progress Report")

    st.sidebar.markdown("<div class='sidebar-divider'></div>", unsafe_allow_html=True)

    # ================= SYSTEM STATUS =================
    st.sidebar.markdown("### ⚙ System Status")
    st.sidebar.success("Server: Online")
    st.sidebar.info("Last Sync: Today")
    st.sidebar.warning("2 Modules Pending")

    # ================= MAIN CONTENT =================
    if menu == "🏠 Overview":
        overview_ui()
    elif menu == "📘 DSA Tracker":
        dsa_ui()
    elif menu == "🧮 Aptitude Tracker":
        aptitude_ui()
    elif menu == "📚 Core Subjects":
        core_subjects_ui()
    elif menu == "🛠 Projects & Research":
        project_tracker_ui()
    elif menu == "🏆 Coding Contests":
        coding_contests_ui()
    elif menu == "🏢 Service-Based Companies":
        company = st.selectbox(
            "Choose Company",
            ["All", "TCS", "Infosys", "Wipro", "Accenture", "SAP", "Deloitte"]
        )
        if company == "TCS":
            tcs_ui()
        elif company == "Infosys":
            infosys_ui()
        elif company == "Wipro":
            wipro_ui()
        elif company == "Accenture":
            accenture_ui()
        elif company == "SAP":
            sap_ui()
        elif company == "Deloitte":
            deloitte_ui()
        else:
            service_based_ui()
    elif menu == "🚀 Product-Based Companies":
        product_based_ui()
    elif menu == "⌛ All Companies":
        all_companies_ui()
    elif menu == "📄 Resume Manager":
        resume_upload_ui()
    elif menu == "🎤 HR Interview":
        hr_ui()
    elif menu == "🤖 Mock Interview":
        mock_interview_ui()
    elif menu == "💼 Internships":
        internships_ui()
    elif menu == "🌐 Off-Campus Jobs":
        offcampus_ui()
    elif menu == "👤 My Profile":
        profile_ui()
    elif menu == "🚪 Logout":
        logout_ui()
