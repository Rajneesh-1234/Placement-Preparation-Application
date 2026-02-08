import streamlit as st

def service_based_ui():

    st.title("🏢 Service-Based Companies Preparation Dashboard")
    st.caption(
        "TCS • Infosys • Wipro • Cognizant • Capgemini • Accenture"
    )

    st.divider()

    # =====================================================
    # ABOUT SERVICE-BASED COMPANIES
    # =====================================================
    st.subheader("📌 About Service-Based Companies")

    st.markdown("""
Service-based companies primarily work on **client projects**, **enterprise software**,  
**support systems**, and **long-term IT services**.

They do NOT expect:
- Advanced competitive programming
- Research-level algorithms

They DO expect:
- Strong fundamentals
- Clean, readable code
- Good communication
- Problem-solving approach
""")

    st.divider()

    # =====================================================
    # COMPANY SELECTION
    # =====================================================
    company = st.selectbox(
        "Select Company",
        [
            "TCS",
            "Infosys",
            "Wipro",
            "Cognizant",
            "Capgemini",
            "Accenture"
        ]
    )

    st.divider()

    # =====================================================
    # COMPANY-WISE HIRING PATTERN
    # =====================================================
    st.subheader(f"🧾 {company} – Hiring Pattern")

    if company == "TCS":
        st.markdown("""
**Rounds**
1. Online Assessment  
   - Numerical Ability  
   - Verbal Ability  
   - Reasoning Ability  
   - 1–2 Coding Questions  

2. Technical Interview  
   - OOPS concepts  
   - Basic DSA  
   - DBMS & SQL  
   - Project discussion  

3. Managerial / HR Interview  
   - Situation-based questions  
   - Teamwork & adaptability  
""")

    elif company == "Infosys":
        st.markdown("""
**Rounds**
1. Online Test  
   - Quantitative Aptitude  
   - Logical Reasoning  
   - Verbal  
   - Pseudocode / Coding  

2. Technical Interview  
   - Java / Python basics  
   - OOPS & Collections  
   - SQL queries  
   - Resume deep dive  

3. HR Interview  
   - Communication skills  
   - Willingness to relocate  
""")

    elif company == "Wipro":
        st.markdown("""
**Rounds**
1. Online Assessment  
   - Aptitude  
   - Reasoning  
   - Verbal  
   - Coding (easy level)  

2. Technical Interview  
   - DSA basics  
   - OOPS  
   - OS basics  
   - Projects  

3. HR Round  
   - Career goals  
""")

    elif company == "Cognizant":
        st.markdown("""
**Rounds**
1. Online Test  
   - Aptitude  
   - Coding logic  

2. Technical Interview  
   - Arrays & Strings  
   - OOPS  
   - DBMS  
   - Real-time scenarios  

3. HR Interview  
""")

    elif company == "Capgemini":
        st.markdown("""
**Rounds**
1. Online Assessment  
   - Pseudocode  
   - Aptitude  
   - English Communication  

2. Technical Interview  
   - Basic coding  
   - OOPS & DBMS  

3. HR Interview  
""")

    elif company == "Accenture":
        st.markdown("""
**Rounds**
1. Cognitive Assessment  
   - Aptitude  
   - Reasoning  
   - Verbal  

2. Technical Assessment  
   - Coding fundamentals  
   - Pseudocode  

3. Communication Assessment  
4. HR Interview  
""")

    st.divider()

    # =====================================================
    # SYLLABUS BREAKDOWN
    # =====================================================
    st.subheader("📚 Common Syllabus (Must Prepare)")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
**Aptitude**
- Percentages  
- Ratio & Proportion  
- Time & Work  
- Time & Speed  
- Probability  
""")

        st.markdown("""
**Reasoning**
- Seating Arrangement  
- Puzzles  
- Blood Relations  
- Direction Sense  
""")

    with col2:
        st.markdown("""
**Verbal Ability**
- Reading Comprehension  
- Grammar  
- Synonyms & Antonyms  
""")

        st.markdown("""
**Technical**
- Arrays & Strings  
- Basic Recursion  
- OOPS  
- DBMS & SQL  
""")

    st.divider()

    # =====================================================
    # CODING EXPECTATION
    # =====================================================
    st.subheader("💻 Coding Expectations")

    st.info("""
Difficulty Level: **Easy to Medium**  

Focus Areas:
- Correct logic
- Edge case handling
- Clean syntax
- Proper variable naming  

Languages Preferred:
- Java
- Python
- C / C++
""")

    st.divider()

    # =====================================================
    # PROJECT & RESUME GUIDANCE
    # =====================================================
    st.subheader("📄 Resume & Projects")

    st.markdown("""
**Number of Projects**
- 2–3 strong projects are enough  

**Project Type**
- CRUD applications  
- Web applications  
- Database-driven projects  

**Interview Focus**
- Why you built it  
- Challenges faced  
- How you solved problems  
""")

    st.divider()

    # =====================================================
    # PREPARATION CHECKLIST
    # =====================================================
    st.subheader("✅ Preparation Checklist")

    if "service_checklist" not in st.session_state:
        st.session_state.service_checklist = {
            "Aptitude": False,
            "Reasoning": False,
            "Verbal": False,
            "DSA Basics": False,
            "OOPS": False,
            "DBMS": False,
            "Projects": False,
            "Resume": False
        }

    for item in st.session_state.service_checklist:
        st.session_state.service_checklist[item] = st.checkbox(
            item,
            st.session_state.service_checklist[item]
        )

    completed = sum(st.session_state.service_checklist.values())
    total = len(st.session_state.service_checklist)

    st.progress(completed / total)
    st.write(f"Preparation Completed: {completed}/{total}")

    st.divider()

    # =====================================================
    # SELF ASSESSMENT
    # =====================================================
    st.subheader("📊 Self-Assessment")

    aptitude = st.slider("Aptitude Level", 0, 10, 5)
    coding = st.slider("Coding Level", 0, 10, 5)
    communication = st.slider("Communication Level", 0, 10, 5)

    readiness = int((aptitude + coding + communication) / 3 * 10)

    st.metric("Overall Readiness Score", f"{readiness}%")

    if readiness >= 75:
        st.success("You are READY for service-based company interviews 🎯")
    elif readiness >= 50:
        st.warning("You need some more practice ⚠")
    else:
        st.error("Start preparation seriously 🚨")

    st.divider()

    # =====================================================
    # FINAL TIPS
    # =====================================================
    st.success("""
Final Advice:
- Practice daily
- Revise basics repeatedly
- Explain your thinking clearly
- Be confident and honest
""")
