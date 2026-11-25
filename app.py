import streamlit as st
from ui import apply_style, detail_card, footer

st.set_page_config(page_title="Stroke Risk Prediction", page_icon="🩺", layout="wide")
apply_style()

st.markdown("""
<div class="hero"><div class="hero-grid"><div>
<div class="eyebrow">HEALTHCARE AI / ACADEMIC RESEARCH / SDG 3</div>
<h1>Early Stroke<br>Risk Prediction</h1>
<p>Exploring stroke-associated patterns through machine learning, class rebalancing and data-driven research.</p>
<svg class="pulse" viewBox="0 0 340 54" aria-hidden="true"><path d="M0 28 H80 L94 18 L108 38 L125 5 L145 49 L163 28 H210 L223 20 L237 34 L249 28 H340" fill="none" stroke="#75e4ce" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg></div><svg class="hero-art" viewBox="0 0 260 240" aria-hidden="true"><circle cx="130" cy="120" r="105" fill="#ffffff" opacity=".07"/><circle cx="130" cy="120" r="80" fill="none" stroke="#99e7d6" stroke-width="1" stroke-dasharray="5 8"/><path d="M130 65 C95 25 48 75 70 112 C42 148 88 190 130 164 C172 190 218 148 190 112 C212 75 165 25 130 65Z" fill="#75e4ce" fill-opacity=".15" stroke="#99e7d6" stroke-width="3"/><path d="M130 65 V164 M80 95 L105 115 L130 100 L155 125 L180 95 M105 115 L100 150 M155 125 L165 150" fill="none" stroke="#99e7d6" stroke-width="2"/><g fill="#fff"><circle cx="105" cy="115" r="5"/><circle cx="155" cy="125" r="5"/><circle cx="130" cy="100" r="5"/><circle cx="100" cy="150" r="4"/><circle cx="165" cy="150" r="4"/></g></svg></div></div>
""", unsafe_allow_html=True)

if st.button("Explore prediction demo →", type="primary"):
    st.switch_page("pages/1_Stroke_Prediction.py")

st.markdown('<div class="section-label">RESEARCH AT A GLANCE</div>', unsafe_allow_html=True)
a, b, c = st.columns(3)
a.metric("Dataset records", "5,110")
b.metric("Test recall", "80%")
c.metric("ROC-AUC", "0.8469")

st.subheader("Why this research matters")
a, b, c = st.columns(3)
with a:
    detail_card("01", "The challenge", "Only 4.87% of dataset records are stroke-positive. Accuracy alone can hide missed positive cases.")
with b:
    detail_card("02", "Our approach", "Compare five model configurations, including SMOTE and SMOTENC, and tune the decision threshold.")
with c:
    detail_card("03", "The outcome", "The selected model detected 40 of 50 positive test records, with substantial false positives.")

st.subheader("How the demonstration works")
st.markdown('<div class="flow-grid"><div class="detail-card"><span class="step-number">01</span><h3>Enter sample data</h3><p>Ten demographic and health-related features.</p></div><div class="detail-card"><span class="step-number">02</span><h3>Process and classify</h3><p>Saved preprocessing and XGBoost model.</p></div><div class="detail-card"><span class="step-number">03</span><h3>Understand the result</h3><p>Experimental score, threshold and limitations.</p></div></div>', unsafe_allow_html=True)

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

st.subheader("Frequently asked questions")
with st.expander("Is this a medical risk calculator?"):
    st.write("No. It demonstrates classification on a research dataset. It cannot estimate personal future stroke risk.")
with st.expander("Why use recall instead of accuracy alone?"):
    st.write("Because the positive class is rare, high accuracy can coexist with many missed positive records.")
with st.expander("Does the website train a new model?"):
    st.write("No. It loads the saved XGBoost model and preprocessing pipeline.")

footer()
