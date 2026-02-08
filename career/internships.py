import streamlit as st


def internships_ui():
    st.title("💼 Internships Preparation Hub")
    st.caption(
        "End-to-end internship guidance for B.Tech, M.Tech & MCA students"
    )

    st.divider()

    # =================================================
    # DEGREE SELECTION
    # =================================================
    degree = st.selectbox(
        "Select Your Degree",
        ["B.Tech", "M.Tech", "MCA"]
    )

    year = st.selectbox(
        "Select Academic Year",
        ["1st Year", "2nd Year", "3rd Year", "Final Year"]
    )

    st.divider()

    # =================================================
    # INTERNSHIP ROADMAP
    # =================================================
    st.subheader("🗺 Internship Roadmap")

    if degree == "B.Tech":
        roadmap = [
            "1st Year → Basics of Programming, GitHub, C/Python",
            "2nd Year → DSA + Mini Projects",
            "3rd Year → Core Subjects + Major Internships",
            "Final Year → PPO Conversion & Placement"
        ]
    elif degree == "M.Tech":
        roadmap = [
            "Semester 1 → Advanced Core Subjects",
            "Semester 2 → Research / Industry Projects",
            "Semester 3 → Corporate Internship",
            "Semester 4 → Thesis / PPO"
        ]
    else:  # MCA
        roadmap = [
            "1st Year → Programming + DBMS",
            "2nd Year → Full-Stack / Java / Python",
            "Final Year → Corporate Internship"
        ]

    for step in roadmap:
        st.markdown(f"✅ {step}")

    st.divider()

    # =================================================
    # TOP INTERNSHIP COMPANIES
    # =================================================
    st.subheader("🏢 Top Companies Offering Internships")

    companies = [
        "Google", "Microsoft", "Amazon", "SAP", "Oracle",
        "TCS", "Infosys", "Wipro", "Accenture",
        "Flipkart", "Paytm", "Adobe", "IBM"
    ]

    st.multiselect(
        "Target Companies",
        companies
    )

    # =================================================
    # PLATFORMS
    # =================================================
    st.subheader("🌐 Internship Platforms")

    platforms = [
        "LinkedIn",
        "Internshala",
        "Indeed",
        "Glassdoor",
        "AngelList",
        "Company Career Pages"
    ]

    for p in platforms:
        st.markdown(f"🔗 {p}")

    st.divider()

    # =================================================
    # SKILL CHECKLIST
    # =================================================
    st.subheader("🧠 Skill Readiness Checklist")

    st.checkbox("Strong Programming Fundamentals")
    st.checkbox("DSA Basics")
    st.checkbox("Mini / Major Projects")
    st.checkbox("GitHub Portfolio")
    st.checkbox("Resume Ready")
    st.checkbox("Mock Interviews")

    st.divider()

    st.success(
        "🚀 Tip: Internships are the strongest gateway to PPO & full-time roles."
    )
