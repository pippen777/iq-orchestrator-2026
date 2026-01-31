import streamlit as st
from styles import apply_iq_styles
from brain import run_strategy_engine

# Setup
st.set_page_config(page_title="IQ Intelligence Lab", layout="wide")
apply_iq_styles()

# app.py update
st.markdown('<h1 class="title-text">Intelligence Lab</h1>', unsafe_allow_html=True)

# 01: LEGACY ANCHOR (Start with the 'Where')
st.markdown('<p class="step-header">01 / IDENTIFY THE TECHNICAL ANCHOR</p>', unsafe_allow_html=True)
anchor = st.selectbox("Which system is causing 'Complexity Paralysis'?", 
                      ["Legacy Core Banking", "Siloed CRM", "Fragmented ERP", "Other (Custom)"])

# 02: CLINICAL DISCOVERY (The 'Why')
st.markdown('<p class="step-header">02 / CAPTURE STRATEGIC SYMPTOMS</p>', unsafe_allow_html=True)
st.caption("Ask the CIO about PoC fatigue, data silos, or governance roadblocks.")
friction = st.text_area("Live Discovery Notes:", placeholder="Type exactly what the CIO says here...", height=200)

if st.button("⚡ ORCHESTRATE STRATEGIC BLUEPRINT", type="primary", use_container_width=True):
    with st.spinner("Analyzing tensions and diagnosing maturity..."):
        # The engine now handles the diagnosis based on the text
        result = run_strategy_engine("Unknown", friction, anchor) 
        st.markdown(result, unsafe_allow_html=True)

# Symptom Grid
col1, col2 = st.columns(2)
s1 = col1.checkbox("Struggling with 'PoC fatigue' / Pilot Limbo", help="88% of pilots fail here.")
s2 = col1.checkbox("Legacy Mainframe/ERP is a 'Data Anchor'", help="Complexity paralysis.")
s3 = col2.checkbox("CRO/Risk blocking data access (POPIA fear)", help="Governance is a roadblock.")
s4 = col2.checkbox("AI is seen as an 'IT project', not board strategy", help="Fragmented vision.")

# Logic to determine Persona
if s1 and s2:
    st.session_state.mat = "Scaler"
    st.warning("DIAGNOSIS: SCALER. Trapped in the 'Trough of Despair'.")
elif s4:
    st.session_state.mat = "Explorer"
    st.info("DIAGNOSIS: EXPLORER. Navigating hype vs. substance.")
elif s1 and s3:
    st.session_state.mat = "Scaler"
    st.warning("DIAGNOSIS: SCALER. Operational headwinds identified.")
else:
    st.session_state.mat = "Innovator" # Default for advanced users
    st.success("DIAGNOSIS: INNOVATOR. Ready for Agentic Orchestration.")

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
