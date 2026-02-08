import streamlit as st

def resume_builder_ui():
    st.title("📝 Resume Builder")

    name = st.text_input("Name")
    skills = st.text_area("Skills")
    projects = st.text_area("Projects")

    if st.button("Generate Resume"):
        st.success("Resume generated (demo)")
