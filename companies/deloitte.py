import streamlit as st

def deloitte_ui():
    st.title("🏢 Deloitte Preparation")
    st.caption("Consulting + Technology hiring")

    st.divider()

    st.subheader("📝 Deloitte Selection Process")

    st.markdown("""
    **Round 1 – Online Test**
    - Aptitude
    - Verbal
    - Logical Reasoning
    - Coding (Optional)

    **Round 2 – Technical Interview**
    - OOPS
    - DBMS
    - Java / Python basics
    - Project explanation

    **Round 3 – Managerial + HR**
    """)

    st.divider()

    st.subheader("📚 Core Preparation Areas")
    st.checkbox("Java / Python fundamentals")
    st.checkbox("SQL Queries")
    st.checkbox("Data Structures")
    st.checkbox("Business communication")
    st.checkbox("Case-study thinking")

    st.success("🎯 Deloitte looks for structured thinking and professionalism.")
