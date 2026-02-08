import streamlit as st
from auth.auth_utils import login_user


def login_ui():

    # =====================================================
    # SESSION INITIALIZATION (MOST IMPORTANT PART)
    # =====================================================
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if "user" not in st.session_state:
        st.session_state.user = None

    # =====================================================
    # IF USER IS ALREADY LOGGED IN → SKIP LOGIN PAGE
    # =====================================================
    if st.session_state.logged_in:
        st.success(f"✅ Logged in as {st.session_state.user}")
        st.info("You will remain logged in until you logout manually.")
        return

    # =====================================================
    # LOGIN UI
    # =====================================================
    st.title("🔐 Student Login")
    st.caption("Login using registered email & password")

    email = st.text_input("📧 Email ID", placeholder="example@gmail.com")
    password = st.text_input("🔑 Password", type="password")

    # Optional (future use)
    remember_me = st.checkbox("Remember me")

    if st.button("Login"):
        if not email or not password:
            st.warning("⚠️ Please enter both email and password")
            return

        user = login_user(email, password)

        if user:
            st.session_state.logged_in = True
            st.session_state.user = email
            st.session_state.remember_me = remember_me

            st.success("✅ Login successful")
            st.info("Session will remain active until logout.")
            st.rerun()
        else:
            st.error("❌ Invalid email or password")
