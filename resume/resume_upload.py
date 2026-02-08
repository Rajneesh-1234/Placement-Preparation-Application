import streamlit as st

def resume_upload_ui():

    st.title("📄 Resume Manager")
    st.caption("Build • Validate • Optimize your resume for placements")

    st.divider()

    # =====================================================
    # RESUME UPLOAD
    # =====================================================
    st.subheader("⬆ Upload Resume (PDF only)")

    resume_file = st.file_uploader(
        "Upload your resume",
        type=["pdf"],
        help="Only PDF format is recommended for ATS systems"
    )

    if resume_file:
        st.success("✅ Resume uploaded successfully")

    st.divider()

    # =====================================================
    # ATS RESUME CHECKLIST
    # =====================================================
    st.subheader("✅ ATS-Friendly Resume Checklist")

    st.checkbox("One-page resume (mandatory for freshers)")
    st.checkbox("Simple layout (no tables / text boxes)")
    st.checkbox("Standard fonts (Arial, Calibri, Times New Roman)")
    st.checkbox("Font size 10.5–12")
    st.checkbox("No images, icons, emojis")
    st.checkbox("Clear section headings")
    st.checkbox("Consistent formatting")
    st.checkbox("PDF generated from Word (not scanned)")

    st.divider()

    # =====================================================
    # RESUME STRUCTURE (IDEAL)
    # =====================================================
    st.subheader("📌 Ideal Resume Structure (Top → Bottom)")

    st.markdown("""
1. **Name**
2. **Contact Details**  
   (Phone | Email | LinkedIn | GitHub)

3. **Professional Summary / Objective**

4. **Technical Skills**

5. **Projects**

6. **Internship / Experience**

7. **Education**

8. **Certifications / Achievements**
""")

    st.divider()

    # =====================================================
    # SERVICE VS PRODUCT BASED RESUME
    # =====================================================
    st.subheader("🏢 Resume Strategy by Company Type")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
### Service-Based Companies
(TCS, Infosys, Wipro, Capgemini)

✔ Clear basics  
✔ Clean formatting  
✔ Simple projects  
✔ Communication skills  

Focus on:
- OOPS
- DBMS
- Java / Python basics
- Internship experience
""")

    with col2:
        st.markdown("""
### Product-Based Companies
(Amazon, Google, Microsoft)

✔ Strong DSA  
✔ Impactful projects  
✔ Problem-solving depth  
✔ Optimized code  

Focus on:
- DSA keywords
- Algorithms
- System thinking
- Metrics & results
""")

    st.divider()

    # =====================================================
    # PROJECT SECTION (MOST IMPORTANT)
    # =====================================================
    st.subheader("🚀 Project Section – How to Write")

    st.markdown("""
**Use this format for each project:**

• Project Name  
• Tech Stack  
• 3–4 bullet points  

**Bullet Formula (STAR):**
- What you built
- How you built it
- What problem it solved
- Result / impact
""")

    st.info("""
Example:
• Developed an e-commerce platform using Java, JDBC, MySQL  
• Implemented secure login & role-based access  
• Optimized database queries reducing load time by 30%  
""")

    st.divider()

    # =====================================================
    # SKILLS SECTION BEST PRACTICES
    # =====================================================
    st.subheader("🧠 Skills Section Best Practices")

    st.markdown("""
✔ Categorize skills  
✔ Use ATS-friendly names  
✔ Do NOT rate skills (avoid stars / percentages)

**Good Example**
- Languages: Java, Python, SQL  
- Frameworks: Spring Boot, JDBC  
- Tools: Git, Postman, Maven  

❌ Bad Example
- Java ⭐⭐⭐⭐⭐  
- Expert in everything
""")

    st.divider()

    # =====================================================
    # COMMON RESUME REJECTION REASONS
    # =====================================================
    st.subheader("🚫 Common Resume Rejection Reasons")

    st.error("""
❌ Too lengthy (2–3 pages)
❌ Poor formatting
❌ No projects
❌ Generic objective
❌ Missing keywords
❌ Spelling / grammar mistakes
❌ Fake or exaggerated claims
""")

    st.divider()

    # =====================================================
    # ATS RESUME CHECKER LINKS
    # =====================================================
    st.subheader("🔗 ATS Resume Checker (Recommended)")

    st.markdown("""
Use these trusted tools to check ATS score:

• https://www.jobscan.co  
• https://resumeworded.com  
• https://enhancv.com  
• https://resume.io  

👉 Upload resume + job description for best results
""")

    st.divider()

    # =====================================================
    # FINAL SELF-VERIFICATION
    # =====================================================
    st.subheader("🎯 Final Resume Readiness Check")

    ready = True

    ready &= st.checkbox("Resume is one page")
    ready &= st.checkbox("Projects are well explained")
    ready &= st.checkbox("No grammar mistakes")
    ready &= st.checkbox("ATS score above 70%")
    ready &= st.checkbox("Resume customized for company")

    if ready:
        st.success("🚀 Your resume is READY for placements")
    else:
        st.warning("⚠ Improve resume before applying")

    st.divider()

    st.success("""
Final Advice:
- Resume gets you the interview
- Skills get you the job
- Keep updating your resume every month
""")
