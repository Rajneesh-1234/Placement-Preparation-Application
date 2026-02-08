import streamlit as st

def accenture_ui():
    st.title("🏢 Accenture Preparation")
    st.caption("Pattern aligned with Accenture hiring process")

    st.divider()

    st.subheader("📝 Accenture Hiring Rounds")

    st.markdown("""
    **Round 1 – Cognitive Assessment**
    - Numerical Ability
    - Logical Reasoning
    - Verbal Ability

    **Round 2 – Technical Assessment**
    - Pseudocode
    - Network Security
    - Cloud Basics
    - Programming MCQs

    **Round 3 – Coding Round**
    - 1–2 Easy/Medium coding problems

    **Round 4 – Communication + HR**
    """)

    st.divider()

    st.subheader("📌 Important Topics")
    st.markdown("""
    - Arrays & Strings
    - Pseudocode logic
    - OOPS concepts
    - SQL queries
    - SDLC & Agile
    """)

    st.divider()

    st.subheader("🎯 Accenture Focus Areas")
    st.checkbox("Clear communication")
    st.checkbox("Problem-solving approach")
    st.checkbox("Basic cloud knowledge (AWS/Azure)")
    st.checkbox("Security fundamentals")

    st.success("💡 Accenture strongly evaluates communication & scenario-based thinking.")
