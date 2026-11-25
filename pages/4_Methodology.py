import streamlit as st
from ui import apply_style
from pathlib import Path

st.set_page_config(page_title="Methodology", layout="wide")
apply_style()
st.markdown('<div class="section-label">04 / RESEARCH WORKFLOW</div>', unsafe_allow_html=True)
st.title("Project Methodology")
st.markdown('<div class="page-intro">From raw data to a deployed classification model.</div>', unsafe_allow_html=True)

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
    st.subheader(title)
    st.write(description)

assets = Path(__file__).resolve().parents[1] / "assets"
for name in ["smote_comparison.png", "feature_importance.png"]:
    if (assets / name).exists():
        st.image(str(assets / name))
st.caption("Feature importance does not establish causation.")
