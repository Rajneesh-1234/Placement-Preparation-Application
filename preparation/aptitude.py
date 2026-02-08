# =====================================================
# APTITUDE / REASONING / VERBAL MASTER TRACKER
# =====================================================

import streamlit as st
import pandas as pd
import os
from datetime import datetime
from pandas.errors import EmptyDataError
import matplotlib.pyplot as plt

# =====================================================
# CONFIG
# =====================================================
DATA_DIR = "data"

SCORE_FILE = f"{DATA_DIR}/aptitude_scores.csv"
GOAL_FILE = f"{DATA_DIR}/aptitude_goals.csv"
NOTES_FILE = f"{DATA_DIR}/aptitude_notes.csv"
PRACTICE_FILE = f"{DATA_DIR}/daily_practice.csv"
REVISION_FILE = f"{DATA_DIR}/revision_log.csv"

SECTIONS = [
    "Quantitative Aptitude",
    "Logical Reasoning",
    "Verbal Ability"
]

TOPICS = {
    "Quantitative Aptitude": [
        "Number System","LCM HCF","Percentage","Profit & Loss",
        "Simple Interest","Compound Interest","Ratio & Proportion",
        "Average","Time & Work","Time Speed Distance",
        "Permutation Combination","Probability","Mensuration",
        "Data Interpretation","Simplification"
    ],
    "Logical Reasoning": [
        "Blood Relations","Direction Sense","Seating Arrangement",
        "Coding Decoding","Series","Puzzles","Syllogism",
        "Inequality","Input Output","Clock","Calendar"
    ],
    "Verbal Ability": [
        "Reading Comprehension","Sentence Correction",
        "Error Spotting","Para Jumbles","Synonyms",
        "Antonyms","One Word Substitution","Grammar",
        "Vocabulary","Inference"
    ]
}

# =====================================================
# UTILITIES
# =====================================================
def ensure_data_dir():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def safe_csv(file, columns):
    try:
        if os.path.exists(file) and os.path.getsize(file) > 0:
            df = pd.read_csv(file)

            # Auto-fix missing columns
            for col in columns:
                if col not in df.columns:
                    df[col] = None

            df = df[columns]
            df.to_csv(file, index=False)
            return df

        df = pd.DataFrame(columns=columns)
        df.to_csv(file, index=False)
        return df

    except EmptyDataError:
        df = pd.DataFrame(columns=columns)
        df.to_csv(file, index=False)
        return df

# =====================================================
# SESSION INIT
# =====================================================
def init_session():
    if "user" not in st.session_state:
        st.session_state.user = "Guest"

    st.session_state.scores = safe_csv(
        SCORE_FILE,
        ["User","Section","Topic","Score","TimeTaken","Date"]
    )

    st.session_state.goals = safe_csv(
        GOAL_FILE,
        ["User","Section","TargetScore","Deadline"]
    )

    st.session_state.notes = safe_csv(
        NOTES_FILE,
        ["User","Section","Topic","Note","Date"]
    )

    st.session_state.practice = safe_csv(
        PRACTICE_FILE,
        ["User","Section","Topic","Questions","Correct","Date"]
    )

    st.session_state.revision = safe_csv(
        REVISION_FILE,
        ["User","Section","Topic","RevisionDate"]
    )

# =====================================================
# HEADER
# =====================================================
def header():
    st.title("🧮 Aptitude • Reasoning • Verbal Tracker")
    st.caption("Complete Placement Aptitude Management System 🚀")

def user_section():
    with st.sidebar:
        st.header("👤 User")
        st.session_state.user = st.text_input(
            "Your Name",
            st.session_state.user
        )

# =====================================================
# ADD SCORE
# =====================================================
def add_score():
    st.subheader("➕ Add Test Score")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        section = st.selectbox("Section", SECTIONS)

    with c2:
        topic = st.selectbox("Topic", TOPICS[section])

    with c3:
        score = st.slider("Score (%)", 0, 100)

    with c4:
        time_taken = st.number_input("Time Taken (minutes)", 1, 300)

    if st.button("💾 Save Score"):
        row = {
            "User": st.session_state.user,
            "Section": section,
            "Topic": topic,
            "Score": score,
            "TimeTaken": time_taken,
            "Date": now()
        }

        st.session_state.scores = pd.concat(
            [st.session_state.scores, pd.DataFrame([row])],
            ignore_index=True
        )

        st.session_state.scores.to_csv(SCORE_FILE, index=False)
        st.success("Score saved successfully ✅")

# =====================================================
# DAILY PRACTICE
# =====================================================
def daily_practice():
    st.subheader("📅 Daily Practice Log")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        section = st.selectbox("Section", SECTIONS, key="p_sec")

    with c2:
        topic = st.selectbox("Topic", TOPICS[section], key="p_top")

    with c3:
        questions = st.number_input("Questions Attempted", 1, 200)

    with c4:
        correct = st.number_input("Correct Answers", 0, questions)

    if st.button("📌 Save Practice"):
        row = {
            "User": st.session_state.user,
            "Section": section,
            "Topic": topic,
            "Questions": questions,
            "Correct": correct,
            "Date": now()
        }

        st.session_state.practice = pd.concat(
            [st.session_state.practice, pd.DataFrame([row])],
            ignore_index=True
        )

        st.session_state.practice.to_csv(PRACTICE_FILE, index=False)
        st.success("Practice saved 📘")

# =====================================================
# ANALYTICS
# =====================================================
def analytics():
    st.subheader("📊 Performance Analytics")

    df = st.session_state.scores
    if df.empty:
        st.info("No data available yet")
        return

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Attempts", len(df))
    c2.metric("Average Score", f"{df['Score'].mean():.1f}%")
    c3.metric("Best Score", f"{df['Score'].max()}%")
    c4.metric("Lowest Score", f"{df['Score'].min()}%")

# =====================================================
# STRENGTH / WEAKNESS
# =====================================================
def strength_analysis():
    st.subheader("💪 Strength & Weakness Analysis")

    df = st.session_state.scores
    if df.empty:
        return

    avg = df.groupby("Topic")["Score"].mean()

    st.markdown("### ✅ Strong Topics (≥70%)")
    st.table(avg[avg >= 70].sort_values(ascending=False))

    st.markdown("### ⚠ Weak Topics (<40%)")
    st.table(avg[avg < 40].sort_values())

# =====================================================
# REVISION
# =====================================================
def revision_tracker():
    st.subheader("🔁 Revision Tracker")

    section = st.selectbox("Section", SECTIONS, key="r_sec")
    topic = st.selectbox("Topic", TOPICS[section], key="r_top")

    if st.button("🔄 Mark Revised"):
        row = {
            "User": st.session_state.user,
            "Section": section,
            "Topic": topic,
            "RevisionDate": now()
        }

        st.session_state.revision = pd.concat(
            [st.session_state.revision, pd.DataFrame([row])],
            ignore_index=True
        )

        st.session_state.revision.to_csv(REVISION_FILE, index=False)
        st.success("Revision marked ✅")

# =====================================================
# NOTES
# =====================================================
def notes_section():
    st.subheader("📝 Learning & Mistake Notes")

    section = st.selectbox("Section", SECTIONS, key="n_sec")
    topic = st.selectbox("Topic", TOPICS[section], key="n_top")
    note = st.text_area("Write your note")

    if st.button("💾 Save Note"):
        row = {
            "User": st.session_state.user,
            "Section": section,
            "Topic": topic,
            "Note": note,
            "Date": now()
        }

        st.session_state.notes = pd.concat(
            [st.session_state.notes, pd.DataFrame([row])],
            ignore_index=True
        )

        st.session_state.notes.to_csv(NOTES_FILE, index=False)
        st.success("Note saved 📝")

    if not st.session_state.notes.empty:
        st.dataframe(st.session_state.notes, use_container_width=True)

# =====================================================
# MAIN UI
# =====================================================
def aptitude_ui():
    ensure_data_dir()
    init_session()

    header()
    user_section()

    st.divider()
    add_score()

    st.divider()
    daily_practice()

    st.divider()
    analytics()

    st.divider()
    strength_analysis()

    st.divider()
    revision_tracker()

    st.divider()
    notes_section()
