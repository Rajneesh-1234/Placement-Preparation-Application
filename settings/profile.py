import streamlit as st
from auth.auth_utils import get_user_details


def profile_ui():
    st.title("👤 My Profile")
    st.caption("View and manage your personal & academic details")

    # ---------------- SESSION CHECK ----------------
    if "user" not in st.session_state:
        st.error("❌ User session expired. Please login again.")
        return

    email = st.session_state.user
    user = get_user_details(email)

    if not user:
        st.error("❌ Unable to fetch profile data.")
        return

    (
        user_id,
        full_name,
        email,
        password,
        mobile,
        degree,
        branch,
        college,
        university,
        passing_year,
        cgpa,
        skills,
        profile_pic,
        created_at
    ) = user

    # ---------------- PROFILE HEADER ----------------
    col1, col2 = st.columns([1, 3])

    with col1:
        if profile_pic:
            st.image(profile_pic, width=150)
        else:
            st.image(
                "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
                width=150
            )

    with col2:
        st.subheader(full_name)
        st.markdown(f"📧 **Email:** {email}")
        st.markdown(f"🎓 **Degree:** {degree}")
        st.markdown(f"🏫 **College:** {college}")

    st.divider()

    # ---------------- PERSONAL DETAILS ----------------
    st.subheader("📋 Personal Details")

    col1, col2 = st.columns(2)
    with col1:
        st.text_input("Full Name", full_name, disabled=True)
        st.text_input("Email", email, disabled=True)
        st.text_input("Mobile", mobile, disabled=True)

    with col2:
        st.text_input("Degree", degree, disabled=True)
        st.text_input("Branch", branch, disabled=True)
        st.text_input("Passing Year", passing_year, disabled=True)

    # ---------------- ACADEMIC DETAILS ----------------
    st.subheader("🎓 Academic Details")

    col1, col2 = st.columns(2)
    with col1:
        st.text_input("University", university, disabled=True)

    with col2:
        st.text_input("CGPA / Percentage", cgpa, disabled=True)

    # ---------------- SKILLS ----------------
    st.subheader("🧠 Technical Skills")

    if skills:
        for skill in skills.split(","):
            st.markdown(f"✅ {skill}")
    else:
        st.info("No skills added yet.")

    # ---------------- META ----------------
    st.divider()
    st.caption(f"🕒 Account Created On: {created_at}")

    st.info(
        "✏️ Profile editing feature can be enabled in future updates."
    )
