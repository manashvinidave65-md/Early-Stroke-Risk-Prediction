import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Dataset Insights", layout="wide")
st.title("Dataset and Insights")
st.write("Source: [Kaggle Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)")

a, b, c = st.columns(3)
a.metric("Total records", "5,110")
b.metric("Stroke-positive", "249")
c.metric("Missing BMI", "201")
st.bar_chart({"Records": {"No stroke": 4861, "Stroke": 249}})
st.write("Only 4.87% of records are stroke-positive, making this an imbalanced classification problem.")

assets = Path(__file__).resolve().parents[1] / "assets"
for name, title in [
    ("age_distribution.png", "Age distribution"),
    ("age_by_stroke.png", "Age by stroke status"),
    ("glucose_distribution.png", "Glucose distribution"),
    ("correlation_heatmap.png", "Correlation heatmap"),
    ("stroke_rate1.png", "Stroke rate comparison 1"),
    ("stroke_rate2.png", "Stroke rate comparison 2")
]:
    st.subheader(title)
    if (assets / name).exists():
        st.image(str(assets / name))
    else:
        st.caption("Graph not available in the repository.")
st.caption("Observed associations do not establish causation.")
