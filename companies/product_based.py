import streamlit as st

def product_based_ui():

    st.title("🚀 Product-Based Companies Preparation Dashboard")
    st.caption("Amazon • Microsoft • Google • SAP • Adobe")

    st.divider()

    # =====================================================
    # PRODUCT-BASED COMPANY MINDSET
    # =====================================================
    st.subheader("🧠 Product-Based Company Mindset")

    st.markdown("""
Product-based companies build **their own products**, platforms, and technologies.
They expect engineers who can:

- Think independently
- Design efficient solutions
- Write clean, optimized code
- Handle ambiguity
- Scale solutions

They focus less on memorization and more on **depth of understanding**.
""")

    st.divider()

    # =====================================================
    # COMPANY SELECTION
    # =====================================================
    company = st.selectbox(
        "Select Product Company",
        ["Amazon", "Microsoft", "Google", "SAP", "Adobe"]
    )

    st.divider()

    # =====================================================
    # COMPANY-WISE HIRING PROCESS
    # =====================================================
    st.subheader(f"🧾 {company} – Hiring Process")

    if company == "Amazon":
        st.markdown("""
**Rounds**
1. Online Assessment  
   - 2 Coding Questions (DSA – Medium)  
   - Logical Reasoning  
   - Work Simulation  

2. Technical Interviews (2–3 Rounds)  
   - Arrays, Strings, Trees, Graphs  
   - Problem-solving & optimization  
   - Time & Space Complexity  
   - Amazon Leadership Principles  

3. Bar Raiser Round  
   - Deep problem solving  
   - Decision-making under pressure  
""")

    elif company == "Microsoft":
        st.markdown("""
**Rounds**
1. Online Coding Test  
   - DSA (Medium–Hard)  

2. Technical Interviews (3–4 Rounds)  
   - Data Structures  
   - Algorithms  
   - OOPS & System Design (experienced)  

3. HR / Managerial  
   - Team fit & culture  
""")

    elif company == "Google":
        st.markdown("""
**Rounds**
1. Online Assessment  
   - DSA (Hard)  

2. Technical Interviews (4–5 Rounds)  
   - Algorithms  
   - Data Structures  
   - Problem solving from scratch  
   - Optimization  

3. Hiring Committee  
""")

    elif company == "SAP":
        st.markdown("""
**Rounds**
1. Online Coding Assessment  
   - DSA (Medium)  

2. Technical Interview  
   - Java / C++ / Python  
   - OOPS  
   - DBMS  
   - System understanding  

3. HR Interview  
""")

    elif company == "Adobe":
        st.markdown("""
**Rounds**
1. Online Coding Test  
   - DSA (Medium–Hard)  

2. Technical Interviews (2–3 Rounds)  
   - Algorithms  
   - Low-level design  
   - Code quality  

3. HR Interview  
""")

    st.divider()

    # =====================================================
    # MANDATORY DSA TOPICS (DEEP)
    # =====================================================
    st.subheader("📚 Mandatory DSA Topics (Must Master)")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
**Core Data Structures**
- Arrays & Strings  
- Linked List  
- Stack & Queue  
- Hashing  

**Trees**
- Binary Tree  
- BST  
- Traversals  
""")

    with col2:
        st.markdown("""
**Advanced Topics**
- Graphs (BFS, DFS)  
- Dynamic Programming  
- Greedy Algorithms  
- Backtracking  
""")

    st.divider()

    # =====================================================
    # SYSTEM DESIGN
    # =====================================================
    st.subheader("🏗 System Design Expectations")

    st.info("""
Freshers:
- Basic design thinking
- Data flow understanding

Experienced:
- Low-level design
- Scalability
- APIs & databases
""")

    st.divider()

    # =====================================================
    # CODING INTERVIEW REALITY
    # =====================================================
    st.subheader("💻 Coding Interview Reality")

    st.markdown("""
Interviewers evaluate:
- How you approach the problem
- How you optimize
- How you explain your logic
- How you handle edge cases

❌ Writing brute-force only is risky  
✅ Optimized + clean solution is expected
""")

    st.divider()

    # =====================================================
    # RESUME & PROJECT EXPECTATIONS
    # =====================================================
    st.subheader("📄 Resume & Projects")

    st.markdown("""
**Projects Matter A LOT**
- 2–3 strong projects
- Real-world relevance
- Proper explanation

**What Interviewers Ask**
- Why this project?
- What challenges?
- How would you improve it?
""")

    st.divider()

    # =====================================================
    # PREPARATION CHECKLIST
    # =====================================================
    st.subheader("✅ Preparation Checklist")

    if "product_checklist" not in st.session_state:
        st.session_state.product_checklist = {
            "Arrays & Strings": False,
            "Trees & Graphs": False,
            "Dynamic Programming": False,
            "System Design": False,
            "OOPS": False,
            "Projects": False,
            "Resume": False
        }

    for item in st.session_state.product_checklist:
        st.session_state.product_checklist[item] = st.checkbox(
            item,
            st.session_state.product_checklist[item]
        )

    done = sum(st.session_state.product_checklist.values())
    total = len(st.session_state.product_checklist)

    st.progress(done / total)
    st.write(f"Completion: {done}/{total}")

    st.divider()

    # =====================================================
    # SELF-ASSESSMENT
    # =====================================================
    st.subheader("📊 Self Assessment")

    dsa = st.slider("DSA Strength", 0, 10, 5)
    coding = st.slider("Coding Speed & Accuracy", 0, 10, 5)
    design = st.slider("System Design", 0, 10, 3)

    readiness = int((dsa * 0.5 + coding * 0.3 + design * 0.2) * 10)

    st.metric("Interview Readiness Score", f"{readiness}%")

    if readiness >= 80:
        st.success("You are READY for product-based interviews 🚀")
    elif readiness >= 60:
        st.warning("You are close, practice more ⚠")
    else:
        st.error("You need deeper preparation ❌")

    st.divider()

    # =====================================================
    # DAILY STRATEGY
    # =====================================================
    st.subheader("🗓 Daily Preparation Strategy")

    st.markdown("""
**Daily Routine**
- 2 DSA problems (Medium)
- 1 Revision topic
- 30 min system design reading
- Explain solutions aloud
""")

    st.divider()

    # =====================================================
    # FINAL TIPS
    # =====================================================
    st.success("""
Final Advice:
- Focus on depth, not quantity
- Solve problems, don’t memorize
- Learn to explain clearly
- Stay consistent
""")
