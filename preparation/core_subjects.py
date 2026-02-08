import streamlit as st
import pandas as pd
import os
from datetime import datetime, timedelta
from pandas.errors import EmptyDataError

# =====================================================
# CONFIG
# =====================================================
DATA_DIR = "data"

PROGRESS_FILE = f"{DATA_DIR}/core_progress.csv"
TOPIC_FILE = f"{DATA_DIR}/core_topics.csv"
NOTES_FILE = f"{DATA_DIR}/core_notes.csv"
REVISION_FILE = f"{DATA_DIR}/core_revision.csv"
STUDY_LOG_FILE = f"{DATA_DIR}/core_study_log.csv"

SUBJECTS = ["DBMS", "OS", "CN", "OOPs"]

TOPICS = {
    "DBMS": [
        "ER Model","Relational Model","Keys",
        "Normalization","Transactions","ACID",
        "Indexing","B Trees","SQL Joins",
        "Subqueries","Views","Triggers",
        "Stored Procedures","Concurrency Control",
        "Deadlock","Recovery","NoSQL","CAP Theorem"
    ],
    "OS": [
        "Process","Thread","CPU Scheduling",
        "Deadlock","Memory Management","Paging",
        "Segmentation","Virtual Memory",
        "File System","Disk Scheduling",
        "Synchronization","Semaphores",
        "Monitors","IPC","Linux Basics"
    ],
    "CN": [
        "OSI Model","TCP/IP","HTTP HTTPS",
        "DNS","SMTP","FTP","UDP vs TCP",
        "Routing Algorithms","ARP","ICMP",
        "Congestion Control","Flow Control",
        "Network Security","Firewalls",
        "Subnetting","NAT"
    ],
    "OOPs": [
        "Class & Object","Encapsulation",
        "Inheritance","Polymorphism",
        "Abstraction","Interfaces",
        "Abstract Class","SOLID Principles",
        "Design Patterns","Factory Pattern",
        "Singleton","Observer Pattern",
        "Dependency Injection","UML",
        "Java OOPs","C++ OOPs"
    ]
}

DIFFICULTY = ["Easy", "Medium", "Hard"]
CONFIDENCE = ["Low", "Medium", "High"]

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
    st.session_state.progress = safe_csv(
        PROGRESS_FILE,
        ["Subject","Completed","Date"]
    )

    st.session_state.topics = safe_csv(
        TOPIC_FILE,
        ["Subject","Topic","Completed","Difficulty","Confidence","Date"]
    )

    st.session_state.notes = safe_csv(
        NOTES_FILE,
        ["Subject","Topic","Note","Date"]
    )

    st.session_state.revision = safe_csv(
        REVISION_FILE,
        ["Subject","Topic","RevisionDate"]
    )

    st.session_state.study_log = safe_csv(
        STUDY_LOG_FILE,
        ["Subject","Topic","Minutes","Date"]
    )

# =====================================================
# HEADER
# =====================================================
def header():
    st.title("📚 Core Subjects Tracker")
    st.caption("DBMS • OS • CN • OOPs – Interview Ready Dashboard 🚀")

# =====================================================
# SUBJECT COMPLETION
# =====================================================
def subject_completion():
    st.subheader("✅ Subject Completion Status")

    for sub in SUBJECTS:
        completed = st.checkbox(f"{sub} Completed", key=f"chk_{sub}")

        if completed:
            row = pd.DataFrame([[sub, True, now()]],
                               columns=st.session_state.progress.columns)
            st.session_state.progress = pd.concat(
                [st.session_state.progress, row], ignore_index=True
            )
            st.session_state.progress.to_csv(PROGRESS_FILE, index=False)

# =====================================================
# TOPIC TRACKER
# =====================================================
def topic_tracker():
    st.subheader("📘 Topic-wise Tracking")

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        subject = st.selectbox("Subject", SUBJECTS)

    with c2:
        topic = st.selectbox("Topic", TOPICS[subject])

    with c3:
        completed = st.checkbox("Completed")

    with c4:
        difficulty = st.selectbox("Difficulty", DIFFICULTY)

    with c5:
        confidence = st.selectbox("Confidence", CONFIDENCE)

    if st.button("💾 Save Topic Progress"):
        row = pd.DataFrame([[ 
            subject, topic, completed, difficulty, confidence, now()
        ]], columns=st.session_state.topics.columns)

        st.session_state.topics = pd.concat(
            [st.session_state.topics, row], ignore_index=True
        )

        st.session_state.topics.to_csv(TOPIC_FILE, index=False)
        st.success("Topic progress saved ✅")

# =====================================================
# STUDY LOG
# =====================================================
def study_log():
    st.subheader("⏱ Daily Study Log")

    c1, c2, c3 = st.columns(3)

    with c1:
        subject = st.selectbox("Study Subject", SUBJECTS, key="sl_sub")

    with c2:
        topic = st.selectbox("Study Topic", TOPICS[subject], key="sl_top")

    with c3:
        minutes = st.number_input("Minutes Studied", 10, 600)

    if st.button("📌 Save Study Log"):
        row = pd.DataFrame([[ 
            subject, topic, minutes, now()
        ]], columns=st.session_state.study_log.columns)

        st.session_state.study_log = pd.concat(
            [st.session_state.study_log, row], ignore_index=True
        )

        st.session_state.study_log.to_csv(STUDY_LOG_FILE, index=False)
        st.success("Study log saved ⏱")

# =====================================================
# REVISION
# =====================================================
def revision_tracker():
    st.subheader("🔁 Revision Tracker")

    subject = st.selectbox("Revision Subject", SUBJECTS, key="rv_sub")
    topic = st.selectbox("Revision Topic", TOPICS[subject], key="rv_top")

    if st.button("🔄 Mark Revised"):
        row = pd.DataFrame([[ 
            subject, topic, now()
        ]], columns=st.session_state.revision.columns)

        st.session_state.revision = pd.concat(
            [st.session_state.revision, row], ignore_index=True
        )

        st.session_state.revision.to_csv(REVISION_FILE, index=False)
        st.success("Revision recorded 🔁")

# =====================================================
# NOTES
# =====================================================
def notes_section():
    st.subheader("📝 Notes / Interview Points")

    subject = st.selectbox("Note Subject", SUBJECTS, key="n_sub")
    topic = st.selectbox("Note Topic", TOPICS[subject], key="n_top")
    note = st.text_area("Write explanation / interview points")

    if st.button("💾 Save Note"):
        row = pd.DataFrame([[ 
            subject, topic, note, now()
        ]], columns=st.session_state.notes.columns)

        st.session_state.notes = pd.concat(
            [st.session_state.notes, row], ignore_index=True
        )

        st.session_state.notes.to_csv(NOTES_FILE, index=False)
        st.success("Note saved 📝")

    if not st.session_state.notes.empty:
        st.dataframe(st.session_state.notes, use_container_width=True)

# =====================================================
# ANALYTICS
# =====================================================
def analytics():
    st.subheader("📊 Core Subject Analytics")

    if st.session_state.topics.empty:
        st.info("No topic data yet")
        return

    completed = st.session_state.topics[
        st.session_state.topics["Completed"] == True
    ]

    st.metric("Topics Completed", len(completed))
    st.metric("Total Topics", len(st.session_state.topics))

# =====================================================
# EXPORT
# =====================================================
def export_data():
    st.subheader("⬇ Export Core Subjects Data")

    if not st.session_state.topics.empty:
        csv = st.session_state.topics.to_csv(index=False).encode()
        st.download_button(
            "Download Topic Progress",
            csv,
            "core_subjects_topics.csv",
            "text/csv"
        )

# =====================================================
# RESET
# =====================================================
def reset_data():
    st.subheader("🗑 Danger Zone")

    if st.button("Delete ALL Core Subject Data"):
        for f in [
            PROGRESS_FILE, TOPIC_FILE, NOTES_FILE,
            REVISION_FILE, STUDY_LOG_FILE
        ]:
            if os.path.exists(f):
                os.remove(f)

        init_session()
        st.success("All core subject data cleared")

# =====================================================
# MAIN UI
# =====================================================
def core_subjects_ui():
    ensure_data_dir()
    init_session()
    header()

    st.divider()
    subject_completion()

    st.divider()
    topic_tracker()

    st.divider()
    study_log()

    st.divider()
    revision_tracker()

    st.divider()
    notes_section()

    st.divider()
    analytics()

    st.divider()
    export_data()

    st.divider()
    reset_data()
