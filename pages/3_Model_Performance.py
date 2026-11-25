import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Model Performance", layout="wide")
st.title("Model Performance")
st.write("Selected model: XGBoost without resampling. Decision threshold: 0.05.")

a, b, c = st.columns(3)
a.metric("Accuracy", "77.89%")
b.metric("Recall", "80%")
c.metric("Precision", "15.63%")
st.write("F1-score: 0.2614 | ROC-AUC: 0.8469")

st.subheader("Validation comparison at default threshold")
results = pd.DataFrame({
    "Model": ["Random Forest", "XGBoost", "RF + SMOTE", "XGB + SMOTE", "XGB + SMOTENC"],
    "Recall": [0, .04, .04, .24, .54],
    "F1": [0, .0769, .0563, .1860, .2318],
    "ROC-AUC": [.7959, .8503, .7877, .8082, .7990]
})
st.dataframe(results, hide_index=True)
st.bar_chart(results.set_index("Model"))

st.subheader("Test confusion matrix")
st.table(pd.DataFrame([[756, 216], [10, 40]], index=["Actual no stroke", "Actual stroke"], columns=["Predicted no stroke", "Predicted stroke"]))
st.write("40 of 50 stroke-positive test records were detected. 216 non-stroke records were incorrectly classified as positive.")

assets = Path(__file__).resolve().parents[1] / "assets"
for name in ["confusion_matrix.png", "roc_curve.png", "threshold_analysis.png"]:
    if (assets / name).exists():
        st.image(str(assets / name))

st.subheader("Milestone 2 vs final")
st.table(pd.DataFrame({"Metric": ["Accuracy", "Recall", "Precision", "F1", "ROC-AUC"], "Milestone 2": [.7573, .72, .1333, .2250, .8122], "Final": [.7789, .80, .1563, .2614, .8469]}))
st.warning("The test split was previously examined. Results are not independent external validation, and precision remains low.")
