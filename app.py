import streamlit as st

st.set_page_config(page_title="Stroke Risk Prediction", page_icon="🩺", layout="wide")

st.title("Early Stroke Risk Prediction")
st.markdown("### Machine learning for healthcare awareness")
st.info("Academic prototype • SDG 3: Good Health and Well-Being")

st.write("Explore how machine learning identifies stroke-associated patterns in an imbalanced healthcare dataset.")

a, b, c = st.columns(3)
a.metric("Dataset records", "5,110")
b.metric("Test recall", "80%")
c.metric("ROC-AUC", "0.8469")

st.subheader("Explore the project")
st.page_link("pages/1_Stroke_Prediction.py", label="Try the educational prediction tool", icon="🩺")
st.page_link("pages/2_Dataset_Insights.py", label="Explore dataset insights", icon="📊")
st.page_link("pages/3_Model_Performance.py", label="View model performance", icon="📈")
st.page_link("pages/4_Methodology.py", label="Understand the methodology", icon="📚")
st.page_link("pages/5_About_Us.py", label="About the project", icon="ℹ️")

st.warning("Not a medical diagnostic tool. Model scores are not probabilities of future stroke.")
