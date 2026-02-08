import streamlit as st

def github_links_ui():
    st.title("🔗 GitHub Project Links")

    link = st.text_input("GitHub Repo URL")

    if st.button("Save Link"):
        st.success("Link saved")
