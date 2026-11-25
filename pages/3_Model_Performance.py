import streamlit as st
from ui import apply_style, detail_card, footer
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Model Performance", layout="wide")
apply_style()
st.markdown('<div class="section-label">03 / EVALUATION DASHBOARD</div>', unsafe_allow_html=True)
st.title("Model Performance")
st.markdown('<div class="page-intro">Compare experimental results and understand the trade-offs.</div>', unsafe_allow_html=True)
st.write("Selected model: XGBoost without resampling. Decision threshold: 0.05.")

a, b, c = st.columns(3)
a.metric("Accuracy", "77.89%")
b.metric("Recall", "80%")
c.metric("Precision", "15.63%")
a,b = st.columns(2)
a.metric("F1-score", "0.2614")
b.metric("ROC-AUC", "0.8469")
st.info("Model selection: highest validation ROC-AUC. Threshold selection: recall-focused validation rule.")

st.subheader("Validation comparison at default threshold")
results = pd.DataFrame({
    "Model": ["Random Forest", "XGBoost", "RF + SMOTE", "XGB + SMOTE", "XGB + SMOTENC"],
    "Recall": [0, .04, .04, .24, .54],
    "F1": [0, .0769, .0563, .1860, .2318],
    "ROC-AUC": [.7959, .8503, .7877, .8082, .7990]
})
st.dataframe(results, hide_index=True)
metric = st.selectbox("Choose a comparison metric", ["ROC-AUC", "Recall", "F1"])
st.bar_chart(results.set_index("Model")[[metric]], color="#0f766e")

st.subheader("Test confusion matrix")
st.table(pd.DataFrame([[756, 216], [10, 40]], index=["Actual no stroke", "Actual stroke"], columns=["Predicted no stroke", "Predicted stroke"]))
a,b,c,d = st.columns(4)
a.metric("True positives", 40)
b.metric("False negatives", 10)
c.metric("True negatives", 756)
d.metric("False positives", 216)
st.write("40 of 50 stroke-positive test records were detected. 216 non-stroke records were incorrectly classified as positive.")

assets = Path(__file__).resolve().parents[1] / "assets"
for name in ["confusion_matrix.png", "roc_curve.png", "threshold_analysis.png"]:
    if (assets / name).exists():
        st.image(str(assets / name))

st.subheader("Milestone 2 vs final")
st.table(pd.DataFrame({"Metric": ["Accuracy", "Recall", "Precision", "F1", "ROC-AUC"], "Milestone 2": [.7573, .72, .1333, .2250, .8122], "Final": [.7789, .80, .1563, .2614, .8469]}))
st.warning("The test split was previously examined. Results are not independent external validation, and precision remains low.")

with st.expander("What do these metrics mean?"):
    st.markdown("**Recall:** fraction of actual positive records detected.\n\n**Precision:** fraction of positive predictions that are actually positive.\n\n**ROC-AUC:** ranking ability across thresholds.\n\n**F1:** harmonic mean of precision and recall.")

footer()
