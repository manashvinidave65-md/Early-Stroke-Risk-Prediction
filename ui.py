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
        st.caption("Explore the six pages using the navigation above.")

def detail_card(number, title, description):
    # Static research content, never user-provided HTML
    st.markdown(f'<div class="detail-card"><span class="step-number">{number}</span><h3>{title}</h3><p>{description}</p></div>', unsafe_allow_html=True)

def footer():
    st.markdown('<div class="footer-note">STROKE RESEARCH LAB · Academic demonstration · Not for clinical use</div>', unsafe_allow_html=True)
