import streamlit as st

def hr_ui():

    st.title("🎤 HR Interview Questions & Answers")
    st.caption("50+ Most Asked HR Questions with Company-Standard Answers")

    hr_questions = {
        "1. Introduce yourself": """
I am a motivated and disciplined individual with a strong interest in learning and professional growth.
I have a solid foundation in my core subjects and continuously work on improving my technical and soft skills.
I enjoy problem-solving and approaching challenges with a positive mindset.
I believe in consistency, hard work, and adaptability.
I am looking for an opportunity where I can contribute to the organization while growing as a professional.
""",

        "2. What are your strengths?": """
One of my biggest strengths is my ability to learn quickly and adapt to new environments.
I am consistent and disciplined, which helps me stay focused on my goals.
I approach problems analytically and try to break them into smaller parts.
I am also a good team player and communicate clearly with others.
These strengths help me contribute positively in a professional environment.
""",

        "3. Tell me about your family background": """
I come from a supportive family that values education, discipline, and hard work.
My family has always encouraged me to stay focused on my goals.
They taught me the importance of honesty and responsibility.
This background has helped shape my character and work ethics.
It has motivated me to be independent and career-oriented.
""",

        "4. Describe your college journey": """
My college journey has been a phase of learning and self-development.
I focused on understanding core subjects and building technical fundamentals.
Alongside academics, I worked on projects and practical skills.
I learned the importance of teamwork, time management, and consistency.
Overall, it helped me grow both technically and personally.
""",

        "5. Explain your project": """
The project was designed to solve a real-world problem using practical technologies.
I was involved in requirement analysis, development, and testing.
The project helped me understand how theoretical concepts are applied in practice.
I also learned debugging, optimization, and structured coding.
This experience strengthened my confidence and problem-solving skills.
""",

        "6. Why should we hire you?": """
I have a strong learning attitude and a problem-solving mindset.
I am disciplined, adaptable, and open to feedback.
I focus on writing clean and understandable solutions.
I work well both independently and in a team.
I believe I can grow with the organization and add value through dedication.
""",

        "7. What are your weaknesses?": """
I used to spend extra time ensuring perfection in my work.
Over time, I realized the importance of balancing quality with deadlines.
I started prioritizing tasks and managing time better.
This helped me become more efficient and productive.
I continuously work on improving myself through feedback.
""",

        "8. Are you open to relocation?": """
Yes, I am open to relocation.
I believe working in different locations provides valuable exposure.
It helps in learning new cultures and work environments.
I see relocation as an opportunity for professional growth.
I am flexible and adaptable to organizational requirements.
""",

        "9. How do you handle pressure?": """
I handle pressure by staying calm and focusing on priorities.
I break tasks into manageable steps and solve them one by one.
I avoid panic and focus on finding solutions.
Planning and time management help me stay productive.
This approach allows me to perform well under pressure.
""",

        "10. What motivates you?": """
Learning new skills and solving challenging problems motivate me.
I enjoy setting goals and achieving them step by step.
Personal growth and improvement drive me forward.
Positive feedback and progress encourage me further.
I stay motivated by maintaining consistency and discipline.
""",

        "11. What do you know about our company?": """
Your company is known for its strong work culture and innovation.
It focuses on quality, learning, and employee development.
The organization values teamwork and professionalism.
It has a strong reputation in the industry.
I see it as a great place to grow and contribute.
""",

        "12. Where do you see yourself in 5 years?": """
In five years, I see myself as a skilled professional in this organization.
I aim to take more responsibilities and contribute to key projects.
I want to strengthen my technical and leadership skills.
I hope to mentor junior team members.
My goal is long-term growth with the company.
""",

        "13. Are you comfortable with the job role?": """
Yes, I am comfortable with the job role.
The responsibilities align well with my skills and interests.
I am eager to learn and adapt as required.
I see this role as a good learning opportunity.
I am committed to performing my duties effectively.
""",

        "14. What kind of work culture do you prefer?": """
I prefer a positive and collaborative work culture.
An environment that encourages learning and communication.
I value teamwork and mutual respect.
A culture that supports growth and innovation motivates me.
Such environments bring out the best performance.
""",

        "15. Are you a team player?": """
Yes, I strongly believe in teamwork.
I enjoy collaborating and sharing ideas with others.
I respect different perspectives and opinions.
I believe teamwork leads to better solutions.
I always contribute responsibly to team goals.
""",

        "16. How do you manage your time?": """
I manage my time by planning tasks in advance.
I set priorities based on importance and deadlines.
I avoid distractions and stay focused.
I regularly review my progress.
This helps me stay organized and productive.
""",

        "17. What are your career goals?": """
My short-term goal is to gain strong industry experience.
I want to improve my technical and professional skills.
My long-term goal is to take leadership responsibilities.
I aim to grow with the organization.
Continuous learning is my key objective.
""",

        "18. How do you handle failure?": """
I see failure as a learning opportunity.
I analyze mistakes and identify areas for improvement.
I take responsibility and work on solutions.
Failures motivate me to perform better next time.
This mindset helps me grow continuously.
""",

        "19. What are your expectations from this company?": """
I expect learning opportunities and professional growth.
A supportive environment that encourages improvement.
Exposure to real-world projects.
Guidance from experienced professionals.
A platform to build a long-term career.
""",

        "20. Do you have any questions for us?": """
Yes, I would like to know about training programs.
I am interested in understanding growth opportunities.
I would like to know about team structure.
Learning and development policies interest me.
Career progression paths would be helpful to know.
"""
    }

    question_list = list(hr_questions.keys())

    selected_question = st.selectbox(
        "Select an HR Question",
        question_list
    )

    st.subheader(selected_question)
    st.write(hr_questions[selected_question])
