import streamlit as st
import pandas as pd


def mock_interview_ui():
    st.title("🎤 Mock Interview Evaluation")
    st.caption(
        "Simulated interview assessment based on real company evaluation criteria"
    )

    st.divider()

    # =================================================
    # INTERVIEW TYPE
    # =================================================
    interview_type = st.selectbox(
        "Select Interview Type",
        [
            "Technical Interview",
            "HR Interview",
            "Managerial Interview",
            "Final Round Interview"
        ]
    )

    st.divider()

    # =================================================
    # INTERVIEW SUMMARY
    # =================================================
    st.subheader("🧾 Interview Summary")

    summary = st.text_area(
        "Overall Interview Summary (Interviewer Notes)",
        placeholder="Write feedback like an interviewer..."
    )

    st.divider()

    # =================================================
    # SCORING TABLE (COMPANY STANDARD)
    # =================================================
    st.subheader("📊 Interview Evaluation Scorecard")

    scorecard = pd.DataFrame({
        "Evaluation Parameter": [
            "Technical Knowledge",
            "Problem Solving Ability",
            "Communication Skills",
            "Body Language & Confidence",
            "Resume Knowledge",
            "Project Explanation",
            "Attitude & Professionalism"
        ],
        "Max Marks": [10, 10, 10, 10, 10, 10, 10],
        "Marks Obtained": [0, 0, 0, 0, 0, 0, 0]
    })

    edited_table = st.data_editor(
        scorecard,
        use_container_width=True,
        num_rows="fixed"
    )

    total_score = edited_table["Marks Obtained"].sum()
    max_score = edited_table["Max Marks"].sum()

    st.metric(
        label="Total Interview Score",
        value=f"{total_score} / {max_score}"
    )

    st.divider()

    # =================================================
    # BODY LANGUAGE & COMMUNICATION
    # =================================================
    st.subheader("🧍 Body Language & Communication Review")

    st.checkbox("Maintained eye contact")
    st.checkbox("Confident posture")
    st.checkbox("Clear and structured answers")
    st.checkbox("Avoided filler words (uh, um)")
    st.checkbox("Active listening")

    st.divider()

    # =================================================
    # RESUME ATS CHECKER (MANUAL)
    # =================================================
    st.subheader("📄 Resume ATS Readiness Check")

    st.checkbox("ATS-friendly format (single column)")
    st.checkbox("Relevant keywords added")
    st.checkbox("Quantified achievements")
    st.checkbox("No grammar/spelling errors")
    st.checkbox("Projects aligned with job role")

    st.info(
        "💡 Tip: Most companies use ATS before interviews. "
        "Poor ATS score = rejection before interview."
    )

    st.divider()

    # =================================================
    # DRESSING & ETIQUETTE
    # =================================================
    st.subheader("👔 Dress Code & Interview Etiquette")

    dress = st.selectbox(
        "Dress Code Evaluation",
        [
            "Excellent (Formal & Professional)",
            "Good (Minor improvements needed)",
            "Average (Needs improvement)",
            "Poor (Unprofessional)"
        ]
    )

    st.checkbox("Formal attire worn")
    st.checkbox("Clean & neat appearance")
    st.checkbox("Proper grooming")
    st.checkbox("Professional body language")

    st.divider()

    # =================================================
    # FINAL DECISION
    # =================================================
    st.subheader("✅ Final Interview Decision")

    decision = st.radio(
        "Interview Outcome",
        [
            "Strong Hire",
            "Hire",
            "Hold",
            "Reject"
        ]
    )

    st.divider()

    # =================================================
    # IMPROVEMENT SUGGESTIONS
    # =================================================
    st.subheader("🛠 Improvement Suggestions")

    st.text_area(
        "Areas to Improve",
        placeholder="""
Example:
- Improve DSA problem solving
- Practice HR questions
- Work on confidence
- Improve resume content
"""
    )

    st.success(
        "🎯 Mock Interview Completed! Use this feedback to improve before real interviews."
    )
