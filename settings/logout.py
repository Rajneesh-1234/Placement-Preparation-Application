import streamlit as st
from datetime import datetime
import time
import pandas as pd
import os

# =====================================================
# CONFIG
# =====================================================
DATA_DIR = "data"
LOGOUT_AUDIT_FILE = f"{DATA_DIR}/logout_audit.csv"


def ensure_data_dir():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)


def save_logout_audit(data):
    ensure_data_dir()

    df = pd.DataFrame([data])

    if os.path.exists(LOGOUT_AUDIT_FILE):
        old = pd.read_csv(LOGOUT_AUDIT_FILE)
        df = pd.concat([old, df], ignore_index=True)

    df.to_csv(LOGOUT_AUDIT_FILE, index=False)


def logout_ui():

    st.title("🚪 Logout")
    st.caption("End your session securely")

    st.divider()

    # =====================================================
    # CHECK LOGIN STATE
    # =====================================================
    if not st.session_state.get("logged_in", False):
        st.error("❌ You are already logged out.")
        st.info("Please login again to access the dashboard.")
        return

    # =====================================================
    # SESSION DETAILS
    # =====================================================
    user = st.session_state.get("user", "Unknown User")
    login_time = st.session_state.get("login_time", None)

    current_time = datetime.now()
    current_time_str = current_time.strftime("%d-%m-%Y %H:%M:%S")

    if login_time:
        try:
            login_dt = datetime.strptime(login_time, "%d-%m-%Y %H:%M:%S")
            session_duration = current_time - login_dt
            duration_str = str(session_duration).split(".")[0]
        except:
            duration_str = "Unavailable"
    else:
        duration_str = "Unavailable"

    st.subheader("👤 Session Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.info(f"**User:** {user}")
        st.info(f"**Login Time:** {login_time}")

    with col2:
        st.info(f"**Current Time:** {current_time_str}")
        st.info(f"**Session Duration:** {duration_str}")

    st.divider()

    # =====================================================
    # LOGOUT REASON
    # =====================================================
    st.subheader("📝 Logout Reason")

    reason = st.selectbox(
        "Why are you logging out?",
        [
            "Completed my work",
            "Taking a break",
            "Switching account",
            "Security reasons",
            "System shutdown",
            "Other"
        ]
    )

    custom_reason = ""
    if reason == "Other":
        custom_reason = st.text_input("Please specify reason")

    st.divider()

    # =====================================================
    # FEEDBACK (NEW FEATURE)
    # =====================================================
    st.subheader("⭐ Session Feedback (Optional)")

    rating = st.slider(
        "How was your session experience?",
        1, 5, 3
    )

    feedback = st.text_area(
        "Any feedback or issue faced? (Optional)",
        placeholder="Your feedback helps us improve..."
    )

    st.divider()

    # =====================================================
    # CONFIRMATION
    # =====================================================
    st.subheader("⚠ Confirm Logout")

    st.warning(
        "Once logged out, you will lose access to all dashboard features "
        "until you login again."
    )

    confirm = st.checkbox("Yes, I want to logout")

    col1, col2 = st.columns(2)

    # =====================================================
    # CONFIRM LOGOUT
    # =====================================================
    with col1:
        if st.button("✅ Logout Now", disabled=not confirm):

            audit_data = {
                "user": user,
                "login_time": login_time,
                "logout_time": current_time_str,
                "session_duration": duration_str,
                "logout_reason": custom_reason if reason == "Other" else reason,
                "rating": rating,
                "feedback": feedback
            }

            save_logout_audit(audit_data)

            # Clear session safely
            for key in list(st.session_state.keys()):
                del st.session_state[key]

            st.success("✅ You have been logged out successfully.")
            st.info("Redirecting to login page...")

            with st.spinner("Redirecting..."):
                time.sleep(1.5)

            st.rerun()

    # =====================================================
    # CANCEL LOGOUT
    # =====================================================
    with col2:
        if st.button("❌ Cancel"):
            st.success("Logout cancelled.")
            st.info("Your session is still active.")

    st.divider()

    # =====================================================
    # SECURITY TIPS
    # =====================================================
    st.subheader("🔐 Security Best Practices")

    st.markdown("""
- Always logout from shared systems  
- Never share credentials  
- Avoid public Wi-Fi for login  
- Logout regularly to protect your data  
""")

    st.divider()

    # =====================================================
    # FOOTER
    # =====================================================
    st.caption(
        "Placement Preparation Dashboard • Secure Session & Audit Enabled"
    )
