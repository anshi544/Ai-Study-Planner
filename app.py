import streamlit as st
from planner import generate_plan

st.title("📚 AI Study Planner")

subjects = []

num = st.number_input("Number of subjects", 1, 5)

for i in range(num):
    st.subheader(f"Subject {i+1}")
    name = st.text_input(f"Name {i}", key=f"name{i}")
    deadline = st.date_input(f"Deadline {i}", key=f"date{i}")
    difficulty = st.selectbox(f"Difficulty {i}", ["Easy", "Medium", "Hard"], key=f"diff{i}")

    subjects.append({
        "name": name,
        "deadline": str(deadline),
        "difficulty": difficulty
    })

if st.button("Generate Plan"):
    plan = generate_plan(subjects)

    st.subheader("📅 Your Study Plan")
    for p in plan:
        st.write(f"{p['subject']} → {p['hours']} hrs/day")