import streamlit as st
from ui import apply_style, detail_card, footer
from pathlib import Path

st.set_page_config(page_title="Dataset Insights", layout="wide")
apply_style()
st.markdown('<div class="section-label">02 / EXPLORATORY DATA ANALYSIS</div>', unsafe_allow_html=True)
st.title("Dataset and Insights")
st.markdown('<div class="page-intro">Understand the dataset behind the machine learning models.</div>', unsafe_allow_html=True)
st.write("Source: [Kaggle Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)")

a, b, c = st.columns(3)
a.metric("Total records", "5,110")
b.metric("Stroke-positive", "249")
c.metric("Missing BMI", "201")
st.subheader("Class balance")
st.markdown('<div class="split-bar"><span style="width:95.13%;background:#0f766e"></span><span style="width:4.87%;background:#e5a45c"></span></div>', unsafe_allow_html=True)
a,b = st.columns(2)
a.caption("● No stroke: 4,861 (95.13%)")
b.caption("● Stroke: 249 (4.87%)")
st.write("Only 4.87% of records are stroke-positive, making this an imbalanced classification problem.")

assets = Path(__file__).resolve().parents[1] / "assets"
def show_graph(name, title, explanation):
    st.subheader(title)
    if (assets / name).exists():
        st.image(str(assets / name))
    else:
        st.caption("Graph not available in the repository.")
    st.caption(explanation)

demographics, measurements, relationships, dictionary = st.tabs(["Demographics", "Measurements", "Relationships", "Data dictionary"])
with demographics:
    a,b = st.columns(2)
    with a:
        show_graph("age_distribution.png", "Age distribution", "Distribution of ages in the dataset.")
    with b:
        show_graph("age_by_stroke.png", "Age by stroke status", "Compare age distributions across the two target classes.")
with measurements:
    show_graph("glucose_distribution.png", "Glucose distribution", "Glucose values are right-skewed.")
with relationships:
    show_graph("correlation_heatmap.png", "Correlation heatmap", "Linear associations between numerical variables.")
    a,b = st.columns(2)
    with a:
        show_graph("stroke_rate1.png", "Stroke rate comparison 1", "Observed group-level proportions.")
    with b:
        show_graph("stroke_rate2.png", "Stroke rate comparison 2", "Observed group-level proportions.")
with dictionary:
    st.table({"Feature group": ["Numerical", "Categorical", "Target", "Excluded"], "Fields": ["age, avg_glucose_level, bmi", "gender, hypertension, heart_disease, ever_married, work_type, Residence_type, smoking_status", "stroke", "id"]})
st.caption("Observed associations do not establish causation.")

footer()
