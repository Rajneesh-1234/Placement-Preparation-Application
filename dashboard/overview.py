import streamlit as st

def overview_ui():

    # ==========================================================
    # GLOBAL STYLES
    # ==========================================================
    st.markdown("""
    <style>

    body {
        background-color: #020617;
        color: #e5e7eb;
    }

    .dash-title {
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 6px;
    }

    .dash-subtitle {
        font-size: 18px;
        color: #9ca3af;
        margin-bottom: 30px;
    }

    .section-title {
        font-size: 30px;
        font-weight: 700;
        margin-top: 45px;
        margin-bottom: 18px;
    }

    .card {
        background: linear-gradient(145deg, #0f172a, #020617);
        padding: 30px;
        border-radius: 18px;
        margin-bottom: 22px;
        box-shadow: 0 12px 40px rgba(0,0,0,0.45);
    }

    .card h3 {
        font-size: 24px;
        margin-bottom: 12px;
    }

    .card p, .card li {
        font-size: 18px;
        line-height: 1.8;
        color: #e5e7eb;
    }

    .badge {
        display: inline-block;
        background: #1e293b;
        padding: 8px 16px;
        border-radius: 999px;
        font-size: 14px;
        margin: 6px 6px 0 0;
        color: #10b981;
        border: 1px solid #10b981;
    }

    .highlight {
        background: linear-gradient(90deg, #064e3b, #022c22);
        padding: 20px;
        border-radius: 14px;
        font-size: 19px;
        color: #34d399;
        margin: 30px 0;
    }

    .warning {
        background: #3f1d1d;
        padding: 20px;
        border-radius: 14px;
        font-size: 18px;
        color: #fca5a5;
        margin: 20px 0;
    }

    .footer-note {
        text-align: center;
        margin-top: 70px;
        font-size: 14px;
        color: #9ca3af;
    }

    </style>
    """, unsafe_allow_html=True)

    # ==========================================================
    # HEADER
    # ==========================================================
    st.markdown("<div class='dash-title'>🎓 Placement Master Dashboard</div>", unsafe_allow_html=True)
    st.markdown("<div class='dash-subtitle'>Complete 4-Year roadmap for B.Tech, M.Tech & MCA students</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="highlight">
        🚀 Goal: Crack Service-based + Product-based companies with strong fundamentals
    </div>
    """, unsafe_allow_html=True)

    # ==========================================================
    # YEAR-WISE PLACEMENT ROADMAP
    # ==========================================================
    st.markdown("<div class='section-title'>🗺 4-Year Placement Roadmap</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h3>📘 Year 1 (Foundation Year)</h3>
        <ul>
            <li>Learn one programming language deeply (C / Java / Python)</li>
            <li>Basics of DSA: arrays, strings, loops, recursion</li>
            <li>Strong mathematics & logic building</li>
            <li>Participate in coding clubs & beginner hackathons</li>
        </ul>
        <span class="badge">Programming Basics</span>
        <span class="badge">Logic Building</span>
    </div>

    <div class="card">
        <h3>📗 Year 2 (Skill Development)</h3>
        <ul>
            <li>Intermediate DSA: stacks, queues, linked list, trees</li>
            <li>Core subjects: DBMS, OS, CN (basics)</li>
            <li>Build 2 mini projects (web / Java / Python)</li>
            <li>Start aptitude preparation</li>
        </ul>
        <span class="badge">DSA</span>
        <span class="badge">Core CS</span>
    </div>

    <div class="card">
        <h3>📙 Year 3 (Placement Preparation)</h3>
        <ul>
            <li>Advanced DSA: DP, graphs, greedy</li>
            <li>Company-specific preparation (TCS, Infosys, SAP)</li>
            <li>Major project + internship</li>
            <li>Mock interviews & resume building</li>
        </ul>
        <span class="badge">Placements</span>
        <span class="badge">Internships</span>
    </div>

    <div class="card">
        <h3>📕 Year 4 (Final Execution)</h3>
        <ul>
            <li>Revise DSA + core subjects</li>
            <li>Daily mock tests & HR practice</li>
            <li>Apply to on-campus & off-campus jobs</li>
            <li>Focus on confidence & communication</li>
        </ul>
        <span class="badge">Final Push</span>
        <span class="badge">Interviews</span>
    </div>
    """, unsafe_allow_html=True)

    # ==========================================================
    # IMPORTANT SKILLS FOR PLACEMENT
    # ==========================================================
    st.markdown("<div class='section-title'>🧠 Skills Required for Placement</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h3>💻 Technical Skills</h3>
        <ul>
            <li>Data Structures & Algorithms</li>
            <li>Java / Python / C++</li>
            <li>DBMS, SQL, Operating Systems</li>
            <li>Computer Networks & OOPs</li>
            <li>Basic System Design (for product companies)</li>
        </ul>
    </div>

    <div class="card">
        <h3>📊 Aptitude & Reasoning</h3>
        <ul>
            <li>Quantitative aptitude</li>
            <li>Logical reasoning</li>
            <li>Verbal ability</li>
            <li>Speed & accuracy</li>
        </ul>
    </div>

    <div class="card">
        <h3>🎤 Soft Skills</h3>
        <ul>
            <li>Communication skills</li>
            <li>HR interview answers</li>
            <li>Confidence & clarity</li>
            <li>Professional behavior</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # ==========================================================
    # CERTIFICATIONS
    # ==========================================================
    st.markdown("<div class='section-title'>📜 Recommended Certifications</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <ul>
            <li>NPTEL – Programming, DBMS, OS</li>
            <li>AWS Cloud Practitioner</li>
            <li>Google Data Analytics (optional)</li>
            <li>Coursera / Udemy DSA courses</li>
            <li>Oracle Java Certification</li>
        </ul>
        <span class="badge">Value Added</span>
        <span class="badge">Resume Boost</span>
    </div>
    """, unsafe_allow_html=True)

    # ==========================================================
    # COMMON MISTAKES
    # ==========================================================
    st.markdown("<div class='section-title'>⚠ Common Mistakes to Avoid</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="warning">
        ❌ Only watching tutorials without practice<br>
        ❌ Ignoring aptitude preparation<br>
        ❌ No projects / fake projects<br>
        ❌ Starting placement prep in final year<br>
        ❌ Poor resume & communication
    </div>
    """, unsafe_allow_html=True)

    # ==========================================================
    # FINAL MESSAGE
    # ==========================================================
    st.markdown("""
    <div class="highlight">
        ✅ Consistency + Practice + Smart Planning = Placement Success
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="footer-note">
        © 2026 Placement-Preparation-Dashboard | Designed for Future Engineers 🚀
    </div>
    """, unsafe_allow_html=True)
