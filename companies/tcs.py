import streamlit as st

def tcs_ui():
    st.title("🏢 TCS Preparation")

    st.markdown("""
### Selection Process
1. Aptitude
2. Coding
3. Technical Interview
4. HR Interview
""")

    st.checkbox("Aptitude prepared")
    st.checkbox("Coding prepared")
    st.checkbox("HR questions prepared")

    st.info("Focus on speed + accuracy")
