import streamlit as st
from styles import apply_iq_styles
from brain import run_strategy_engine

st.set_page_config(page_title="IQ Intelligence Lab", layout="wide")
apply_iq_styles()

st.markdown('<h1 class="title-text">Intelligence Lab</h1>', unsafe_allow_html=True)

# 01: THE TECHNICAL ANCHOR
st.markdown('<p class="step-header">01 / IDENTIFY THE TECHNICAL ANCHOR</p>', unsafe_allow_html=True)
anchor_options = ["Legacy Core Banking (Mainframe)", "Siloed CRM", "Fragmented ERP", "Unstructured Data Lake", "Other (Custom)"]
selected_anchor = st.selectbox("Which system is causing 'Complexity Paralysis'?", anchor_options)

if selected_anchor == "Other (Custom)":
    anchor = st.text_input("Specify the legacy system:", placeholder="e.g., Claims Processing Engine")
else:
    anchor = selected_anchor

# 02: THE CLINICAL DISCOVERY
st.markdown('<p class="step-header">02 / CAPTURE STRATEGIC SYMPTOMS</p>', unsafe_allow_html=True)
st.caption("Probe for: PoC fatigue, CRO roadblocks, data residency fears, or team skepticism.")
friction = st.text_area("Live Discovery Notes (Type CIO's pain here):", 
                        placeholder="e.g., CRO is blocking mainframe access due to POPIA; pilots are failing to reach production...", 
                        height=150)

# ORCHESTRATE
if st.button("⚡ ORCHESTRATE STRATEGIC BLUEPRINT", type="primary", use_container_width=True):
    if not friction:
        st.warning("Clinical Tip: You must capture symptoms before the engine can diagnose maturity.")
    else:
        with st.spinner("Analyzing tensions and diagnosing maturity..."):
            result = run_strategy_engine(friction, anchor)
            st.markdown(result, unsafe_allow_html=True)
            st.toast("Blueprint Orchestrated Successfully")
