import streamlit as st

def technical_ui():
    st.title("💡 Technical Interview Questions")

    questions = [
        "Explain OOPs concepts",
        "Difference between List and Array",
        "What is normalization?",
        "Explain deadlock"
    ]

    for q in questions:
        st.write("❓", q)
