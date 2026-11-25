from pathlib import Path
import streamlit as st

def apply_style():
    # Load the same CSS file on every page
    css = (Path(__file__).parent / "style.css").read_text()
    st.markdown("<style>" + css + "</style>", unsafe_allow_html=True)
