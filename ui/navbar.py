import streamlit as st

def load_navbar():
    st.markdown("""
    <style>
    .main-navbar {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 70px;
        background: #ffffff;
        border-bottom: 1px solid #e5e7eb;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 40px;
        z-index: 10000;
        font-family: Inter, sans-serif;
    }

    .nav-logo {
        font-size: 24px;
        font-weight: 700;
        color: #10b981;
    }

    .nav-links {
        display: flex;
        gap: 26px;
        font-size: 16px;
        font-weight: 500;
    }

    .nav-right {
        display: flex;
        align-items: center;
        gap: 16px;
    }

    .nav-search {
        width: 260px;
        padding: 8px 16px;
        border-radius: 999px;
        border: 1px solid #d1d5db;
    }

    .nav-btn {
        background: #10b981;
        color: white;
        padding: 10px 18px;
        border-radius: 999px;
        font-weight: 600;
    }

    .block-container {
        padding-top: 100px !important;
        padding-bottom: 120px !important;
    }
    </style>

    <div class="main-navbar">
        <div class="nav-logo">🎓 PlacementPrep</div>

        <div class="nav-links">
            <span>Prepare</span>
            <span>Courses</span>
            <span>Projects</span>
            <span>Skill Courses</span>
            <span>OffCampus</span>
        </div>

        <div class="nav-right">
            <input class="nav-search" placeholder="Search for Placements"/>
            <div class="nav-btn">Get Prime</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
