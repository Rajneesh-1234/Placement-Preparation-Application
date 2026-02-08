import streamlit as st


def offcampus_ui():
    st.title("🌐 Off-Campus Job Preparation")
    st.caption(
        "Everything you need for off-campus placements & referrals"
    )

    st.divider()

    # =================================================
    # JOB TYPE
    # =================================================
    job_type = st.selectbox(
        "Select Job Type",
        ["Fresher", "Experienced", "Intern-to-Full-Time"]
    )

    st.divider()

    # =================================================
    # OFF-CAMPUS COMPANIES
    # =================================================
    st.subheader("🏢 Companies Hiring Off-Campus")

    companies = [
        "Google", "Microsoft", "Amazon", "SAP", "IBM",
        "TCS Ninja", "Infosys", "Wipro", "Capgemini",
        "Cognizant", "Accenture", "Deloitte"
    ]

    st.multiselect(
        "Target Companies",
        companies
    )

    st.divider()

    # =================================================
    # APPLICATION PLATFORMS
    # =================================================
    st.subheader("📌 Job Application Platforms")

    platforms = [
        "LinkedIn Jobs",
        "Naukri",
        "Indeed",
        "Glassdoor",
        "Company Career Pages",
        "Employee Referrals"
    ]

    for p in platforms:
        st.markdown(f"🔗 {p}")

    st.divider()

    # =================================================
    # OFF-CAMPUS STRATEGY
    # =================================================
    st.subheader("🧭 Off-Campus Strategy")

    strategy = [
        "Daily apply to 5-10 jobs",
        "Optimize resume for ATS",
        "Use LinkedIn referrals",
        "Practice DSA + Aptitude daily",
        "Prepare HR answers",
        "Track applications in Excel"
    ]

    for s in strategy:
        st.markdown(f"✅ {s}")

    st.divider()

    # =================================================
    # DOCUMENT CHECKLIST
    # =================================================
    st.subheader("📄 Required Documents")

    st.checkbox("Updated Resume (ATS Friendly)")
    st.checkbox("GitHub / Portfolio Link")
    st.checkbox("Degree / Provisional Certificate")
    st.checkbox("Identity Proof")
    st.checkbox("Internship Certificates")

    st.divider()

    st.success(
        "🎯 Tip: Off-campus success depends on consistency, referrals & skill depth."
    )
