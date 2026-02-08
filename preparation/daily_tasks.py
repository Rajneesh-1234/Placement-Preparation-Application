import streamlit as st

def daily_tasks_ui():
    st.title("🗓 Daily Task Planner")

    task = st.text_input("Enter today's task")

    if st.button("Add Task"):
        st.success(f"Task added: {task}")

    st.markdown("""
### Sample Daily Routine
- 1 hr DSA
- 1 hr Aptitude
- 1 hr Core Subjects
""")
