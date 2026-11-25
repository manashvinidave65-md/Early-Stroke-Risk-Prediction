import streamlit as st
from ui import apply_style, detail_card, footer
from pathlib import Path

st.set_page_config(page_title="Methodology", layout="wide")
apply_style()
st.markdown('<div class="section-label">04 / RESEARCH WORKFLOW</div>', unsafe_allow_html=True)
st.title("Project Methodology")
st.markdown('<div class="page-intro">From raw data to a deployed classification model.</div>', unsafe_allow_html=True)

st.subheader("Data partition")
st.markdown('<div class="split-bar"><span style="width:60%;background:#0f766e"></span><span style="width:20%;background:#54b5ac"></span><span style="width:20%;background:#a5d8d4"></span></div>', unsafe_allow_html=True)
a,b,c = st.columns(3)
a.metric("Training · 60%", "3,066")
b.metric("Validation · 20%", "1,022")
c.metric("Testing · 20%", "1,022")
st.subheader("Research pipeline")
for title, description in [
    ("1. Dataset split", "60% training, 20% validation and 20% testing."),
    ("2. Preprocessing", "Median imputation, standardization and one-hot encoding. Preprocessing is fitted on training data."),
    ("3. Random Forest", "Combines multiple decision trees for classification."),
    ("4. XGBoost", "Builds trees sequentially to improve predictions."),
    ("5. SMOTE and SMOTENC", "Generate minority-class samples on training data only. SMOTENC handles mixed categorical and numerical features."),
    ("6. Model selection", "Choose the model with the highest validation ROC-AUC."),
    ("7. Threshold selection", "Use validation recall and F1-score to choose an experimental classification cutoff."),
    ("8. Deployment", "Load the saved model and preprocessing files instead of retraining.")
]:
    with st.container(border=True):
        st.markdown("#### " + title)
        st.write(description)

assets = Path(__file__).resolve().parents[1] / "assets"
for name in ["smote_comparison.png", "feature_importance.png"]:
    if (assets / name).exists():
        st.image(str(assets / name))
st.caption("Feature importance does not establish causation.")

st.subheader("Saved model architecture")
st.code("Sample inputs → Preprocessor → XGBoost → Score → Threshold → Class", language=None)
with st.expander("Why was the baseline model selected?"):
    st.write("XGBoost without resampling had the highest validation ROC-AUC. Resampling improved some default-threshold results but did not guarantee the best ranking performance.")

footer()
