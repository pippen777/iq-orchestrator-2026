import streamlit as st
from styles import apply_iq_styles
from brain import run_strategy_engine

st.set_page_config(page_title="IQ Intelligence Lab", layout="wide")
apply_iq_styles()

st.markdown('<h1 class="title-text">Intelligence Lab</h1>', unsafe_allow_html=True)

# Step 1: Maturity Diagnostic
st.subheader("01 / Define Baseline Maturity")
maturity = st.select_slider("", options=["Explorer", "Scaler", "Innovator"])

# Step 2: Strategic Friction
st.subheader("02 / Identify Strategic Friction")
friction = st.text_area("Mirror the 'PoC Zombies' or data silos here...", 
                        placeholder="Example: Data residency fears preventing CRM integration.")

if st.button("ORCHESTRATE BLUEPRINT", type="primary"):
    with st.spinner("Modeling Agentic Strangler Path..."):
        result = run_strategy_engine(maturity, friction)
        st.markdown(result, unsafe_allow_html=True)
