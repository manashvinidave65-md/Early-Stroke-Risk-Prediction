import streamlit as st
from ui import apply_style

st.set_page_config(page_title="Stroke Risk Prediction", page_icon="🩺", layout="wide")
apply_style()

st.markdown("""
<div class="hero">
<div class="eyebrow">HEALTHCARE AI / ACADEMIC RESEARCH / SDG 3</div>
<h1>Early Stroke<br>Risk Prediction</h1>
<p>Exploring stroke-associated patterns through machine learning, class rebalancing and data-driven research.</p>
<svg class="pulse" viewBox="0 0 340 54" aria-hidden="true"><path d="M0 28 H80 L94 18 L108 38 L125 5 L145 49 L163 28 H210 L223 20 L237 34 L249 28 H340" fill="none" stroke="#75e4ce" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>
</div>
""", unsafe_allow_html=True)

if st.button("Explore prediction demo →", type="primary"):
    st.switch_page("pages/1_Stroke_Prediction.py")

st.markdown('<div class="section-label">RESEARCH AT A GLANCE</div>', unsafe_allow_html=True)
a, b, c = st.columns(3)
a.metric("Dataset records", "5,110")
b.metric("Test recall", "80%")
c.metric("ROC-AUC", "0.8469")

st.subheader("Explore the research")
left, right = st.columns(2)
with left:
    with st.container(border=True):
        st.markdown("#### 01 / Dataset insights")
        st.write("Explore demographics, class imbalance and feature distributions.")
        st.page_link("pages/2_Dataset_Insights.py", label="View dataset →")
    with st.container(border=True):
        st.markdown("#### 03 / Methodology")
        st.write("Understand preprocessing, SMOTE, SMOTENC and model selection.")
        st.page_link("pages/4_Methodology.py", label="Explore methodology →")
with right:
    with st.container(border=True):
        st.markdown("#### 02 / Model performance")
        st.write("Compare models, evaluation metrics and classification outcomes.")
        st.page_link("pages/3_Model_Performance.py", label="View results →")
    with st.container(border=True):
        st.markdown("#### 04 / About the project")
        st.write("Discover the academic objective, scope and limitations.")
        st.page_link("pages/5_About_Us.py", label="About the project →")

st.warning("Educational prototype only. Not a medical diagnostic tool. Model scores are not probabilities of future stroke.")
st.caption("Machine Learning Research • B.Tech CSE • SDG 3")
