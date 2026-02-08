import streamlit as st

def sap_ui():
    st.title("🏢 SAP Preparation Dashboard")

    st.markdown("""
### About SAP Placement
SAP looks for candidates with **strong fundamentals** and **clean coding skills**.

### Selection Rounds
1. Online Assessment (Aptitude + Coding)
2. Technical Interview
3. Managerial / HR Interview
""")

    st.subheader("📌 Core Focus Areas")
    st.checkbox("Core Java / OOPs")
    st.checkbox("DBMS & SQL")
    st.checkbox("Data Structures")
    st.checkbox("Problem Solving")

    st.subheader("🛠 Preparation Tips")
    st.markdown("""
- Write clean, readable code  
- Explain logic clearly  
- Be strong in projects  
- Know DBMS concepts deeply  
""")

    st.success("SAP prefers quality over quantity 🚀")
