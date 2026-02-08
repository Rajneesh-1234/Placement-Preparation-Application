import streamlit as st
import os
from auth.auth_utils import register_user

UPLOAD_DIR = "uploads/profiles"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def register_ui():
    st.title("📝 Student Registration")
    st.caption("Register first, then login to access the dashboard")

    # ---------------- PERSONAL DETAILS ----------------
    st.subheader("👤 Personal Details")

    name = st.text_input("Full Name *")
    email = st.text_input("Email ID *")
    password = st.text_input("Create Password *", type="password")
    mobile = st.text_input("Mobile Number")

    profile_pic = st.file_uploader(
        "Upload Profile Picture",
        type=["jpg", "jpeg", "png"]
    )

    # ---------------- ACADEMIC DETAILS ----------------
    st.subheader("🎓 Academic Details")

    degree = st.selectbox(
        "Degree *",
        ["B.Tech", "M.Tech", "MCA"]
    )

    branch = st.text_input("Branch / Specialization")
    college = st.text_input("College Name")
    university = st.text_input("University")

    passing_year = st.selectbox(
        "Passing Year",
        list(range(2020, 2031))
    )

    cgpa = st.text_input("CGPA / Percentage")

    # ---------------- SKILLS ----------------
    st.subheader("🧠 Technical Skills")

    skills = st.multiselect(
        "Select Skills",
        [
            "Java", "Python", "C++", "DSA",
            "SQL", "Web Development",
            "Spring Boot", "React",
            "Machine Learning", "AI"
        ]
    )

    # ---------------- REGISTER BUTTON ----------------
    if st.button("Register"):
        if not name or not email or not password:
            st.warning("⚠️ Please fill all mandatory fields (*)")
            return

        # -------- SAVE PROFILE PIC --------
        profile_path = ""
        if profile_pic:
            profile_path = os.path.join(
                UPLOAD_DIR,
                email.replace("@", "_") + ".png"
            )
            with open(profile_path, "wb") as f:
                f.write(profile_pic.getbuffer())

        status = register_user(
            full_name=name,
            email=email,
            password=password,
            mobile=mobile,
            degree=degree,
            branch=branch,
            college=college,
            university=university,
            passing_year=passing_year,
            cgpa=cgpa,
            skills=skills,
            profile_pic_path=profile_path
        )

        if status:
            st.success("✅ Registration successful!")
            st.info("👉 Please go to **Login** from the sidebar")
        else:
            st.error("❌ Email already registered")
