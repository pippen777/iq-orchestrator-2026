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
                        placeholder="e.g., CRO is blocking mainframe access due to POPIA...", 
                        height=150)

# PRIMARY ORCHESTRATION BUTTON
# Added a unique key "main_btn" to prevent duplication errors
if st.button("⚡ ORCHESTRATE STRATEGIC BLUEPRINT", type="primary", use_container_width=True, key="main_btn"):
    if not friction:
        st.warning("Clinical Tip: You must capture symptoms before the engine can diagnose maturity.")
    else:
        with st.spinner("Analyzing tensions and diagnosing maturity..."):
            st.session_state.result = run_strategy_engine(friction, anchor)
            st.toast("Blueprint Orchestrated Successfully")

# RENDER OUTPUT & PIVOT BOX
if "result" in st.session_state:
    st.markdown(st.session_state.result, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown('<p class="step-header">STRATEGY PIVOT: CHALLENGE THE ENGINE</p>', unsafe_allow_html=True)
    pivot_input = st.text_input("If the CIO disagrees, type the shift here:", key="pivot_text")
    
    # Added a unique key "pivot_btn" to prevent duplication errors
    if st.button("RE-ORCHESTRATE STRATEGY", key="pivot_btn"):
        with st.spinner("Adapting Logic..."):
            st.session_state.result = run_strategy_engine(friction, anchor, pivot=pivot_input)
            st.rerun()
