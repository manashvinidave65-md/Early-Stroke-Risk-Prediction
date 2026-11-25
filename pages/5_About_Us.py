import streamlit as st
from ui import apply_style, detail_card, footer

st.set_page_config(page_title="About the Project", layout="wide")
apply_style()
st.markdown('<div class="section-label">05 / ACADEMIC RESEARCH</div>', unsafe_allow_html=True)
st.title("About the Project")
st.markdown('<div class="page-intro">A student project exploring machine learning for healthcare awareness.</div>', unsafe_allow_html=True)
st.subheader("Early Stroke Risk Prediction Using Machine Learning and Class Rebalancing")
st.write("B.Tech Computer Science and Engineering academic project.")
st.write("SDG 3: Good Health and Well-Being")
st.subheader("Objective")
st.write("Compare classification and class-rebalancing techniques and demonstrate the selected model through a simple web application.")
st.subheader("Limitations")
st.markdown("- Few stroke-positive records\n- Low precision\n- No independent external or clinical validation\n- Model scores are not calibrated future stroke probabilities")
st.warning("Educational use only. Not for diagnosis or medical decisions.")
st.markdown("[View source code on GitHub](https://github.com/manashvinidave65-md/Early-Stroke-Risk-Prediction)")

st.subheader("Research contributions")
a,b,c = st.columns(3)
with a:
    detail_card("01", "Data exploration", "Investigate imbalance, missing values and feature distributions.")
with b:
    detail_card("02", "Model comparison", "Evaluate baseline and class-rebalanced classifiers.")
with c:
    detail_card("03", "Web demonstration", "Connect the saved model to an interactive educational interface.")
st.subheader("Future scope")
st.markdown("- Validate on an independent dataset.\n- Investigate probability calibration and subgroup performance.\n- Explore ways to reduce false positives without sacrificing recall.")
st.subheader("Project resources")
st.link_button("Source code and notebooks", "https://github.com/manashvinidave65-md/Early-Stroke-Risk-Prediction")
st.link_button("Original dataset", "https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset")

footer()
