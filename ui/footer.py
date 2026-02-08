import streamlit as st

def load_footer():
    st.markdown("""
    <style>
    .main-footer {
        background: #f9fafb;
        padding: 50px 80px;
        border-top: 1px solid #e5e7eb;
        font-family: Inter, sans-serif;
    }

    .footer-grid {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 40px;
    }

    .footer-title {
        font-weight: 600;
        margin-bottom: 12px;
    }

    .footer-text {
        color: #4b5563;
        font-size: 14px;
        margin-bottom: 6px;
    }

    .footer-bottom {
        text-align: center;
        margin-top: 30px;
        font-size: 13px;
        color: #6b7280;
    }
    </style>

    <div class="main-footer">
        <div class="footer-grid">

            <div>
                <div class="footer-title">PlacementPrep</div>
                <div class="footer-text">India’s No.1 Placement Platform</div>
                <div class="footer-text">For B.Tech, M.Tech & MCA</div>
            </div>

            <div>
                <div class="footer-title">Support</div>
                <div class="footer-text">About Us</div>
                <div class="footer-text">Privacy Policy</div>
                <div class="footer-text">Terms & Conditions</div>
            </div>

            <div>
                <div class="footer-title">Companies</div>
                <div class="footer-text">TCS</div>
                <div class="footer-text">Infosys</div>
                <div class="footer-text">SAP</div>
                <div class="footer-text">Accenture</div>
            </div>

            <div>
                <div class="footer-title">Dashboards</div>
                <div class="footer-text">DSA Tracker</div>
                <div class="footer-text">Aptitude</div>
                <div class="footer-text">Mock Interviews</div>
            </div>

            <div>
                <div class="footer-title">Contact</div>
                <div class="footer-text">support@placementprep.com</div>
                <div class="footer-text">+91-XXXXXXXXXX</div>
            </div>
        </div>

        <div class="footer-bottom">
            © 2026 PlacementPrep | Built for Engineers 🚀
        </div>
    </div>
    """, unsafe_allow_html=True)
