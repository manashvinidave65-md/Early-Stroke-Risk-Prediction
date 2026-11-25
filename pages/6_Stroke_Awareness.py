import streamlit as st
from ui import apply_style, detail_card, footer

st.set_page_config(page_title="Stroke Awareness", layout="wide")
apply_style()
st.title("Understand stroke")
st.write("Learn the basics, recognize warning signs and explore how our research relates to healthcare awareness.")
st.error("Sudden stroke symptoms are an emergency. Call local emergency services immediately. Do not use the prediction demo to decide whether to seek help.")

basics, signs, quiz = st.tabs(["What is stroke?", "Recognize warning signs", "Knowledge quiz"])
with basics:
    st.write("A stroke occurs when blood flow to part of the brain is blocked or when a blood vessel in the brain ruptures.")
    a,b = st.columns(2)
    with a:
        detail_card("01", "Ischemic stroke", "A blockage interrupts blood flow to part of the brain.")
    with b:
        detail_card("02", "Hemorrhagic stroke", "Bleeding occurs in or around the brain.")
    st.write("High blood pressure, smoking and certain heart conditions are among known risk factors. Discuss prevention with a healthcare professional.")
with signs:
    st.subheader("Remember FAST")
    for letter, title, description in [
        ("F", "Face", "Sudden facial drooping"),
        ("A", "Arms", "Sudden arm weakness"),
        ("S", "Speech", "Sudden speech difficulty"),
        ("T", "Time", "Call emergency services immediately")
    ]:
        detail_card(letter, title, description)
    st.caption("Other sudden symptoms can include vision changes, severe headache or difficulty walking. FAST is not exhaustive.")
with quiz:
    st.subheader("Test your understanding")
    with st.form("awareness_quiz"):
        q1 = st.radio("What should you do if someone develops sudden facial drooping and speech difficulty?", ["Choose an answer", "Wait and see", "Call emergency services immediately"])
        q2 = st.radio("Can this research model diagnose a stroke?", ["Choose an answer", "Yes", "No"])
        check = st.form_submit_button("Check answers", type="primary")
    if check:
        if "Choose an answer" in [q1,q2]:
            st.info("Please answer both questions.")
        else:
            score = int(q1 == "Call emergency services immediately") + int(q2 == "No")
            st.metric("Quiz score", f"{score}/2")
            st.write("Correct answers: call emergency services immediately; the model cannot diagnose stroke.")
st.link_button("Learn more from WHO", "https://www.who.int/news-room/fact-sheets/detail/stroke")
st.page_link("pages/1_Stroke_Prediction.py", label="Explore the fictional sample demo")
footer()
