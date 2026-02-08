import streamlit as st
import pandas as pd
import os
from datetime import datetime, timedelta
from pandas.errors import EmptyDataError

# =====================================================
# CONFIG
# =====================================================
DATA_DIR = "data"
PROJECT_FILE = f"{DATA_DIR}/projects.csv"
TASK_FILE = f"{DATA_DIR}/project_tasks.csv"
NOTES_FILE = f"{DATA_DIR}/project_notes.csv"
TIME_FILE = f"{DATA_DIR}/project_time.csv"

STATUS = ["Planned", "In Progress", "Completed"]
DIFFICULTY = ["Easy", "Medium", "Hard"]
PROJECT_TYPE = ["Mini Project", "Major Project", "Internship Project", "Freelance Project"]

# =====================================================
# FILE SAFETY
# =====================================================
def ensure_data_dir():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def safe_csv(file, columns):
    try:
        if os.path.exists(file) and os.path.getsize(file) > 0:
            return pd.read_csv(file)
        df = pd.DataFrame(columns=columns)
        df.to_csv(file, index=False)
        return df
    except EmptyDataError:
        df = pd.DataFrame(columns=columns)
        df.to_csv(file, index=False)
        return df

def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# =====================================================
# SESSION INIT
# =====================================================
def init_session():
    st.session_state.projects = safe_csv(
        PROJECT_FILE,
        ["ProjectName","TechStack","Status","Type","Difficulty",
         "StartDate","EndDate","Description","GitHub","Demo","Created"]
    )

    st.session_state.tasks = safe_csv(
        TASK_FILE,
        ["ProjectName","Task","Completed","Date"]
    )

    st.session_state.notes = safe_csv(
        NOTES_FILE,
        ["ProjectName","Note","Date"]
    )

    st.session_state.time = safe_csv(
        TIME_FILE,
        ["ProjectName","Hours","Date"]
    )

# =====================================================
# HEADER
# =====================================================
def header():
    st.title("💻 Project Tracker")
    st.caption("Industry-level Project Management & Resume Builder 🚀")

# =====================================================
# ADD PROJECT
# =====================================================
def add_project():
    st.subheader("➕ Add New Project")

    c1, c2 = st.columns(2)

    with c1:
        pname = st.text_input("Project Name")
        tech = st.text_input("Tech Stack (comma separated)")
        ptype = st.selectbox("Project Type", PROJECT_TYPE)
        diff = st.selectbox("Difficulty", DIFFICULTY)

    with c2:
        status = st.selectbox("Status", STATUS)
        start = st.date_input("Start Date")
        end = st.date_input("End Date")
        github = st.text_input("GitHub Link")
        demo = st.text_input("Demo / Live Link")

    desc = st.text_area("Project Description")

    if st.button("💾 Save Project"):
        if pname.strip() == "":
            st.warning("Project name is required")
            return

        row = pd.DataFrame([[ 
            pname, tech, status, ptype, diff,
            start, end, desc, github, demo, now()
        ]], columns=st.session_state.projects.columns)

        st.session_state.projects = pd.concat(
            [st.session_state.projects, row], ignore_index=True
        )

        st.session_state.projects.to_csv(PROJECT_FILE, index=False)
        st.success("Project added successfully ✅")

# =====================================================
# PROJECT LIST
# =====================================================
def project_list():
    st.subheader("📂 All Projects")

    if st.session_state.projects.empty:
        st.info("No projects added yet")
        return

    st.dataframe(st.session_state.projects, use_container_width=True)

# =====================================================
# TASK MANAGEMENT
# =====================================================
def task_manager():
    st.subheader("🧩 Project Tasks")

    if st.session_state.projects.empty:
        st.info("Add a project first")
        return

    project = st.selectbox(
        "Select Project",
        st.session_state.projects["ProjectName"].unique()
    )

    task = st.text_input("Task / Feature")

    completed = st.checkbox("Completed")

    if st.button("➕ Add Task"):
        row = pd.DataFrame([[ 
            project, task, completed, now()
        ]], columns=st.session_state.tasks.columns)

        st.session_state.tasks = pd.concat(
            [st.session_state.tasks, row], ignore_index=True
        )

        st.session_state.tasks.to_csv(TASK_FILE, index=False)
        st.success("Task added")

    tasks = st.session_state.tasks[
        st.session_state.tasks["ProjectName"] == project
    ]

    if not tasks.empty:
        st.dataframe(tasks, use_container_width=True)

# =====================================================
# TIME TRACKING
# =====================================================
def time_tracker():
    st.subheader("⏱ Time Tracking")

    if st.session_state.projects.empty:
        return

    project = st.selectbox(
        "Project",
        st.session_state.projects["ProjectName"].unique(),
        key="time_proj"
    )

    hours = st.number_input("Hours Spent", 0.5, 24.0, step=0.5)

    if st.button("🕒 Log Time"):
        row = pd.DataFrame([[ 
            project, hours, now()
        ]], columns=st.session_state.time.columns)

        st.session_state.time = pd.concat(
            [st.session_state.time, row], ignore_index=True
        )

        st.session_state.time.to_csv(TIME_FILE, index=False)
        st.success("Time logged")

# =====================================================
# NOTES
# =====================================================
def project_notes():
    st.subheader("📝 Project Notes & Learnings")

    if st.session_state.projects.empty:
        return

    project = st.selectbox(
        "Project",
        st.session_state.projects["ProjectName"].unique(),
        key="note_proj"
    )

    note = st.text_area("Learning / Challenge / Improvement")

    if st.button("💾 Save Note"):
        row = pd.DataFrame([[ 
            project, note, now()
        ]], columns=st.session_state.notes.columns)

        st.session_state.notes = pd.concat(
            [st.session_state.notes, row], ignore_index=True
        )

        st.session_state.notes.to_csv(NOTES_FILE, index=False)
        st.success("Note saved")

# =====================================================
# ANALYTICS
# =====================================================
def analytics():
    st.subheader("📊 Project Analytics")

    df = st.session_state.projects
    if df.empty:
        return

    c1, c2, c3 = st.columns(3)
    c1.metric("Total Projects", len(df))
    c2.metric("Completed", len(df[df["Status"] == "Completed"]))
    c3.metric("In Progress", len(df[df["Status"] == "In Progress"]))

# =====================================================
# EXPORT
# =====================================================
def export_data():
    st.subheader("⬇ Export Project Data")

    csv = st.session_state.projects.to_csv(index=False).encode()
    st.download_button(
        "Download Projects CSV",
        csv,
        "projects.csv",
        "text/csv"
    )

# =====================================================
# RESET
# =====================================================
def reset_data():
    st.subheader("🗑 Danger Zone")

    if st.button("Delete ALL Project Data"):
        for f in [PROJECT_FILE, TASK_FILE, NOTES_FILE, TIME_FILE]:
            if os.path.exists(f):
                os.remove(f)
        init_session()
        st.success("All project data deleted")

# =====================================================
# MAIN UI FUNCTION
# =====================================================
def project_tracker_ui():
    ensure_data_dir()
    init_session()
    header()

    st.divider()
    add_project()

    st.divider()
    project_list()

    st.divider()
    task_manager()

    st.divider()
    time_tracker()

    st.divider()
    project_notes()

    st.divider()
    analytics()

    st.divider()
    export_data()

    st.divider()
    reset_data()
