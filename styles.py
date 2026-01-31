import streamlit as st

def apply_iq_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;700;800&display=swap');
    
    .stApp {
        background: radial-gradient(circle at top right, #0b101b, #050a18) !important;
        color: white !important;
        font-family: 'Outfit', sans-serif !important;
    }
    
    /* Step Headers */
    .step-header {
        color: #00ADEF;
        font-size: 0.9rem;
        font-weight: 700;
        letter-spacing: 2px;
        margin-bottom: 10px;
        text-transform: uppercase;
    }

    /* Selected Button Glow */
    div[data-testid="stButton"] button:active, div[data-testid="stButton"] button:focus {
        border-color: #00ADEF !important;
        box-shadow: 0 0 15px rgba(0, 173, 239, 0.4) !important;
        background: rgba(0, 173, 239, 0.1) !important;
    }

    /* Target state highlights in tables */
    .target-state {
        color: #00ADEF;
        font-weight: 800;
        background: rgba(0, 173, 239, 0.1);
        padding: 2px 6px;
        border-radius: 4px;
    }
    </style>
    """, unsafe_allow_html=True)
