import streamlit as st
from styles import apply_iq_styles
from brain import run_strategy_engine

# Setup
st.set_page_config(page_title="IQ Intelligence Lab", layout="wide")
apply_iq_styles()

st.markdown('<h1 class="title-text">Intelligence Lab</h1>', unsafe_allow_html=True)

# 01: MATURITY
st.markdown('<p class="step-header">01 / DIAGNOSE MATURITY</p>', unsafe_allow_html=True)
if "mat" not in st.session_state: st.session_state.mat = "Explorer"
m_cols = st.columns(3)
if m_cols[0].button("EXPLORER", use_container_width=True): st.session_state.mat = "Explorer"
if m_cols[1].button("SCALER", use_container_width=True): st.session_state.mat = "Scaler"
if m_cols[2].button("INNOVATOR", use_container_width=True): st.session_state.mat = "Innovator"
st.caption(f"Currently Modeling: **{st.session_state.mat}**")

# 02: LEGACY ANCHOR
st.markdown('<p class="step-header">02 / SELECT LEGACY ANCHOR</p>', unsafe_allow_html=True)
anchor_options = ["Legacy Core Banking", "Siloed CRM", "Fragmented ERP", "Other (Custom)"]
selected_anchor = st.selectbox("Which system is currently causing 'Complexity Paralysis'?", anchor_options)

if selected_anchor == "Other (Custom)":
    anchor = st.text_input("Specify system:", placeholder="e.g., Claims Engine")
else:
    anchor = selected_anchor

# 03: FRICTION
st.markdown('<p class="step-header">03 / IDENTIFY STRATEGIC FRICTION</p>', unsafe_allow_html=True)
friction = st.text_area("Live Capture of CIO Tensions:", 
                        placeholder="Type exactly what the CIO says here...", height=100)

# ORCHESTRATE
if st.button("⚡ ORCHESTRATE BLUEPRINT", type="primary", use_container_width=True):
    with st.spinner("Analyzing tensions..."):
        result = run_strategy_engine(st.session_state.mat, friction, anchor)
        st.markdown(result, unsafe_allow_html=True)
