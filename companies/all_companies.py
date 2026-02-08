import streamlit as st

def all_companies_ui():
    st.title("🏢 All Companies Overview")
    st.caption("Compare preparation strategy across companies")

    st.divider()

    data = {
        "Company Type": ["Service-Based", "Product-Based"],
        "DSA Level": ["Easy–Medium", "Medium–Hard"],
        "Aptitude": ["High Importance", "Low Importance"],
        "Projects": ["Moderate", "Very Important"],
        "Communication": ["Very Important", "Important"]
    }

    st.table(data)

    st.success("📊 Use this comparison to plan your preparation smartly.")
