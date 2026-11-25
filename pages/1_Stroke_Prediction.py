import streamlit as st
from ui import apply_style
import pandas as pd
import joblib
from pathlib import Path

st.set_page_config(page_title="Stroke Prediction", layout="wide")
apply_style()
st.markdown('<div class="section-label">01 / INTERACTIVE DEMO</div>', unsafe_allow_html=True)
st.title("Stroke Classification Demo")
st.markdown('<div class="page-intro">Explore the trained classifier with a fictional sample record.</div>', unsafe_allow_html=True)
st.warning("Use fictional or sample inputs only. This tool cannot diagnose stroke or estimate your personal future risk.")

# Load the trained model and matching preprocessing
folder = Path(__file__).resolve().parents[1] / "models"

@st.cache_resource
def load_model():
    model = joblib.load(folder / "model.pkl")
    preprocessor = joblib.load(folder / "preprocessor.pkl")
    threshold = joblib.load(folder / "threshold.pkl")
    return model, preprocessor, threshold

with st.form("prediction"):
    left, right = st.columns(2)
    with left:
        st.markdown("#### Demographics & history")
        gender = st.selectbox("Gender", ["Female", "Male", "Other"])
        age = st.number_input("Age (years)", 0.08, 82.0, 65.0)
        hypertension = st.selectbox("Hypertension", [0, 1], format_func=lambda x: "Yes" if x else "No")
        heart_disease = st.selectbox("Heart disease", [0, 1], format_func=lambda x: "Yes" if x else "No")
        married = st.selectbox("Ever married", ["Yes", "No"])
    with right:
        st.markdown("#### Lifestyle & measurements")
        work = st.selectbox("Work type", ["Private", "Self-employed", "Govt_job", "children", "Never_worked"])
        residence = st.selectbox("Residence", ["Urban", "Rural"])
        glucose = st.number_input("Average glucose level", 55.0, 272.0, 180.0)
        bmi = st.number_input("BMI", 10.0, 98.0, 30.0)
        smoking = st.selectbox("Smoking status", ["formerly smoked", "never smoked", "smokes", "Unknown"])
    submitted = st.form_submit_button("Run classification", type="primary", use_container_width=True)

if submitted:
    # Convert the form inputs into a single dataset row
    data = pd.DataFrame([{
        "gender": gender, "age": age, "hypertension": hypertension,
        "heart_disease": heart_disease, "ever_married": married,
        "work_type": work, "Residence_type": residence,
        "avg_glucose_level": glucose, "bmi": bmi, "smoking_status": smoking
    }])

    try:
        model, preprocessor, threshold = load_model()
        processed = preprocessor.transform(data)
        score = float(model.predict_proba(processed)[0][1])

        st.subheader("Model output")
        st.metric("Model score (not clinical risk)", f"{score:.4f}")
        st.write("Decision threshold:", threshold)
        if score >= threshold:
            st.info("Stroke-positive classification")
        else:
            st.info("Non-stroke classification")
        st.caption("A negative classification does not rule out stroke. This demonstration does not provide medical advice.")
    except Exception as error:
        st.error("Model could not be loaded or evaluated. Check the saved files and library versions.")
        st.caption(str(error))
