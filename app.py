import streamlit as st
from styles import apply_iq_styles
from brain import run_strategy_engine

st.set_page_config(page_title="IQ Intelligence Lab", layout="wide")
apply_iq_styles()

st.markdown('<h1 class="title-text">Intelligence Lab</h1>', unsafe_allow_html=True)

# 01: MATURITY (Button Toggle instead of Slider)
st.markdown('<p class="step-header">01 / DIAGNOSE MATURITY</p>', unsafe_allow_html=True)
m_cols = st.columns(3)
if "mat" not in st.session_state: st.session_state.mat = "Explorer"

if m_cols[0].button("EXPLORER", use_container_width=True): st.session_state.mat = "Explorer"
if m_cols[1].button("SCALER", use_container_width=True): st.session_state.mat = "Scaler"
if m_cols[2].button("INNOVATOR", use_container_width=True): st.session_state.mat = "Innovator"

st.caption(f"Current Baseline: **{st.session_state.mat}**")

# 02: THE STRANGLER TARGET
st.markdown('<p class="step-header">02 / SELECT LEGACY ANCHOR</p>', unsafe_allow_html=True)
anchor = st.selectbox("Which system is currently causing 'Complexity Paralysis'?", 
                      ["Legacy Core Banking (Mainframe)", "Siloed CRM", "Fragmented ERP", "Unstructured Data Lake"])

# 03: STRATEGIC FRICTION
st.markdown('<p class="step-header">03 / IDENTIFY STRATEGIC FRICTION</p>', unsafe_allow_html=True)
st.info("Clinical Tip: Identify the 'PoC Zombie' or regulatory barrier holding back ROI.")
friction = st.text_area("Live Capture of CIO Tensions:", 
                        placeholder="e.g., CRO refuses to share customer churn data due to POPIA fears.")

if st.button("ORCHESTRATE BLUEPRINT", type="primary", use_container_width=True):
    with st.spinner(f"Modeling Agentic Strangler for {anchor}..."):
        result = run_strategy_engine(st.session_state.mat, friction, anchor)
        st.markdown(result, unsafe_allow_html=True)
