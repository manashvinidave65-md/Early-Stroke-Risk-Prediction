import streamlit as st

st.set_page_config(page_title="About the Project", layout="wide")
st.title("About the Project")
st.subheader("Early Stroke Risk Prediction Using Machine Learning and Class Rebalancing")
st.write("B.Tech Computer Science and Engineering academic project.")
st.write("SDG 3: Good Health and Well-Being")
st.subheader("Objective")
st.write("Compare classification and class-rebalancing techniques and demonstrate the selected model through a simple web application.")
st.subheader("Limitations")
st.markdown("- Few stroke-positive records\n- Low precision\n- No independent external or clinical validation\n- Model scores are not calibrated future stroke probabilities")
st.warning("Educational use only. Not for diagnosis or medical decisions.")
st.markdown("[View source code on GitHub](https://github.com/manashvinidave65-md/Early-Stroke-Risk-Prediction)")
