import streamlit as st
import pandas as pd
import os
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from pandas.errors import EmptyDataError

# =====================================================
# CONFIG
# =====================================================
DATA_DIR = "data"
PROGRESS_FILE = f"{DATA_DIR}/dsa_progress.csv"
GOAL_FILE = f"{DATA_DIR}/dsa_goals.csv"
NOTES_FILE = f"{DATA_DIR}/dsa_notes.csv"

TOPICS = [
    "Arrays", "Strings", "Linked List", "Stack", "Queue",
    "Tree", "Graph", "DP", "Greedy", "Recursion", "Backtracking"
]

DIFFICULTIES = ["Easy", "Medium", "Hard"]

# =====================================================
# FILE & DATA UTILITIES (SAFE)
# =====================================================
def ensure_data_dir():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def load_csv(file, columns):
    """
    Safe CSV loader:
    - Handles missing files
    - Handles empty files
    - Handles corrupted headers
    """
    try:
        if os.path.exists(file) and os.path.getsize(file) > 0:
            return pd.read_csv(file)

        # File missing OR empty
        df = pd.DataFrame(columns=columns)
        df.to_csv(file, index=False)
        return df

    except EmptyDataError:
        df = pd.DataFrame(columns=columns)
        df.to_csv(file, index=False)
        return df

def save_csv(df, file):
    df.to_csv(file, index=False)

def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# =====================================================
# SESSION INIT
# =====================================================
def init_session():
    if "user" not in st.session_state:
        st.session_state.user = "Guest"

    st.session_state.progress = load_csv(
        PROGRESS_FILE,
        ["User", "Topic", "Solved", "Difficulty", "Date"]
    )

    st.session_state.goals = load_csv(
        GOAL_FILE,
        ["User", "Topic", "Target", "Deadline"]
    )

    st.session_state.notes = load_csv(
        NOTES_FILE,
        ["User", "Topic", "Note", "Date"]
    )

# =====================================================
# HEADER & USER
# =====================================================
def header():
    st.title("📘 DSA Tracker")
    st.caption("Complete DSA preparation dashboard – company standard 🚀")

def user_section():
    with st.sidebar:
        st.header("👤 User")
        st.session_state.user = st.text_input(
            "Your Name", st.session_state.user
        )

# =====================================================
# ADD PROGRESS
# =====================================================
def add_progress():
    st.subheader("➕ Add DSA Progress")

    c1, c2, c3 = st.columns(3)

    with c1:
        topic = st.selectbox("Topic", TOPICS)

    with c2:
        solved = st.number_input("Problems Solved", 1, 1000)

    with c3:
        diff = st.selectbox("Difficulty", DIFFICULTIES)

    if st.button("💾 Save Progress"):
        row = pd.DataFrame([[ 
            st.session_state.user, topic, solved, diff, now()
        ]], columns=st.session_state.progress.columns)

        st.session_state.progress = pd.concat(
            [st.session_state.progress, row], ignore_index=True
        )

        save_csv(st.session_state.progress, PROGRESS_FILE)
        st.success("Progress saved ✅")

# =====================================================
# GOALS
# =====================================================
def set_goals():
    st.subheader("🎯 Set DSA Goals")

    c1, c2, c3 = st.columns(3)

    with c1:
        topic = st.selectbox("Goal Topic", TOPICS, key="goal_topic")

    with c2:
        target = st.number_input("Target Problems", 10, 2000)

    with c3:
        deadline = st.date_input("Deadline")

    if st.button("📌 Save Goal"):
        row = pd.DataFrame([[
            st.session_state.user, topic, target, deadline
        ]], columns=st.session_state.goals.columns)

        st.session_state.goals = pd.concat(
            [st.session_state.goals, row], ignore_index=True
        )

        save_csv(st.session_state.goals, GOAL_FILE)
        st.success("Goal added 🎯")

# =====================================================
# NOTES
# =====================================================
def notes_section():
    st.subheader("📝 DSA Notes")

    topic = st.selectbox("Note Topic", TOPICS, key="note_topic")
    note = st.text_area("Approach / Mistake / Insight")

    if st.button("💾 Save Note"):
        row = pd.DataFrame([[
            st.session_state.user, topic, note, now()
        ]], columns=st.session_state.notes.columns)

        st.session_state.notes = pd.concat(
            [st.session_state.notes, row], ignore_index=True
        )

        save_csv(st.session_state.notes, NOTES_FILE)
        st.success("Note saved 📝")

    if not st.session_state.notes.empty:
        st.dataframe(st.session_state.notes, use_container_width=True)

# =====================================================
# ANALYTICS
# =====================================================
def analytics():
    st.subheader("📊 Analytics")

    df = st.session_state.progress
    if df.empty:
        st.info("No progress data yet")
        return

    c1, c2, c3 = st.columns(3)
    c1.metric("Total Problems Solved", int(df["Solved"].sum()))
    c2.metric("Topics Covered", df["Topic"].nunique())
    c3.metric("Total Entries", len(df))

# =====================================================
# STREAK TRACKER
# =====================================================
def streak_tracker():
    st.subheader("🔥 Streak Tracker")

    df = st.session_state.progress
    if df.empty:
        st.info("No streak data")
        return

    df["Date"] = pd.to_datetime(df["Date"]).dt.date
    days = sorted(df["Date"].unique())

    streak = 1
    max_streak = 1

    for i in range(1, len(days)):
        if days[i] == days[i-1] + timedelta(days=1):
            streak += 1
            max_streak = max(max_streak, streak)
        else:
            streak = 1

    st.metric("🔥 Longest Streak (Days)", max_streak)

# =====================================================
# WEAK TOPICS
# =====================================================
def weak_topics():
    st.subheader("⚠ Weak Topics")

    df = st.session_state.progress
    if df.empty:
        return

    weak = df.groupby("Topic")["Solved"].sum().sort_values().head(3)
    st.table(weak)

# =====================================================
# CHARTS
# =====================================================
def charts():
    st.subheader("📈 Visual Insights")

    df = st.session_state.progress
    if df.empty:
        return

    col1, col2 = st.columns(2)

    with col1:
        topic_chart = df.groupby("Topic")["Solved"].sum()
        fig, ax = plt.subplots()
        topic_chart.plot(kind="bar", ax=ax)
        st.pyplot(fig)

    with col2:
        diff_chart = df.groupby("Difficulty")["Solved"].sum()
        fig, ax = plt.subplots()
        diff_chart.plot(kind="pie", autopct="%1.1f%%", ax=ax)
        st.pyplot(fig)

# =====================================================
# EXPORT
# =====================================================
def export_data():
    st.subheader("⬇ Export Data")

    if not st.session_state.progress.empty:
        csv = st.session_state.progress.to_csv(index=False).encode()
        st.download_button(
            "Download Progress CSV",
            csv,
            "dsa_progress.csv",
            "text/csv"
        )

# =====================================================
# RESET
# =====================================================
def reset_data():
    st.subheader("🗑 Danger Zone")

    if st.button("Delete ALL DSA Data"):
        for f in [PROGRESS_FILE, GOAL_FILE, NOTES_FILE]:
            if os.path.exists(f):
                os.remove(f)

        init_session()
        st.success("All data deleted successfully")

# =====================================================
# MAIN UI FUNCTION (IMPORT SAFE)
# =====================================================
def dsa_ui():
    ensure_data_dir()
    init_session()
    header()
    user_section()

    st.divider()
    add_progress()

    st.divider()
    set_goals()

    st.divider()
    notes_section()

    st.divider()
    analytics()

    st.divider()
    streak_tracker()

    st.divider()
    weak_topics()

    st.divider()
    charts()

    st.divider()
    export_data()

    st.divider()
    reset_data()
