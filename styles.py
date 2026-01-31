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

    .title-text {
        font-size: 52px !important;
        font-weight: 800 !important;
        background: linear-gradient(90deg, #00ADEF 0%, #FFFFFF 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 30px !important;
    }

    .step-header {
        color: #00ADEF;
        font-size: 0.9rem;
        font-weight: 700;
        letter-spacing: 2px;
        margin-bottom: 15px;
        text-transform: uppercase;
        border-bottom: 1px solid rgba(0, 173, 239, 0.2);
        padding-bottom: 5px;
    }

    /* Diagnosis Box */
    .aha-box {
        padding: 30px;
        background: rgba(0, 173, 239, 0.08);
        border-left: 8px solid #00ADEF;
        border-radius: 15px;
        margin: 30px 0;
    }

    .phase-card {
        background: rgba(255, 255, 255, 0.03);
        border-left: 5px solid #F02FC2; /* Pink accent for GESHIDO energy */
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 15px;
    }
    
    .target-state {
        color: #00ADEF;
        font-weight: 800;
        background: rgba(0, 173, 239, 0.1);
        padding: 2px 8px;
        border-radius: 4px;
    }
    
    table { width: 100%; border-collapse: collapse; margin: 20px 0; font-size: 14px; }
    th { text-align: left; color: #00ADEF; border-bottom: 2px solid #00ADEF; padding: 10px; }
    td { padding: 10px; border-bottom: 1px solid rgba(255, 255, 255, 0.1); }
    </style>
    """, unsafe_allow_html=True)
