import streamlit as st

def apply_iq_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;700;800&display=swap');
    
    .stApp {
        background: #050A18 !important;
        color: white !important;
        font-family: 'Outfit', sans-serif !important;
    }
    
    /* Modern Gradient Title */
    .title-text {
        font-size: 48px !important;
        font-weight: 800 !important;
        background: linear-gradient(90deg, #00ADEF 0%, #FFFFFF 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 30px !important;
    }

    /* Executive Cards */
    .executive-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(0, 173, 239, 0.3);
        padding: 25px;
        border-radius: 15px;
        margin-bottom: 20px;
    }

    /* Target Impact spans */
    .impact-highlight {
        color: #00ADEF;
        font-weight: 700;
        font-size: 1.1rem;
    }
    </style>
    """, unsafe_allow_html=True)
