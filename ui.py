from pathlib import Path
import streamlit as st

def apply_style():
    # Load the same CSS file on every page
    css = (Path(__file__).parent / "style.css").read_text()
    st.markdown("<style>" + css + "</style>", unsafe_allow_html=True)

    with st.sidebar:
        st.markdown("### Stroke Research Lab")
        st.caption("ML • Healthcare • Academic prototype")
        st.divider()
        st.caption("Explore the website using the navigation above.")

    # Visible navigation on every page, including mobile layouts
    links = [("app.py", "Home"), ("pages/6_Stroke_Awareness.py", "Learn"), ("pages/1_Stroke_Prediction.py", "Try demo"), ("pages/2_Dataset_Insights.py", "Data"), ("pages/3_Model_Performance.py", "Results"), ("pages/4_Methodology.py", "Method"), ("pages/5_About_Us.py", "About")]
    for column, (path, label) in zip(st.columns(len(links)), links):
        with column:
            st.page_link(path, label=label)
    st.divider()

def detail_card(number, title, description):
    # Static research content, never user-provided HTML
    st.markdown(f'<div class="detail-card"><span class="step-number">{number}</span><h3>{title}</h3><p>{description}</p></div>', unsafe_allow_html=True)

def footer():
    st.markdown('<div class="footer-note">STROKE RESEARCH LAB · Academic demonstration · Not for clinical use</div>', unsafe_allow_html=True)
