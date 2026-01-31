import streamlit as st

def apply_iq_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700;800&display=swap');
    
    /* HIDE SIDEBAR & DEFAULT STREAMLIT ELEMENTS */
    [data-testid="stSidebar"] { display: none !important; }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* THE FOUNDATION: DEEP NAVY RADIAL GRADIENT */
    .stApp {
        background: radial-gradient(circle at top right, #1a1b3a, #050a18) !important;
        color: white !important;
        font-family: 'Outfit', sans-serif !important;
    }

    /* TYPOGRAPHY: PREMIUM IQ GRADIENT */
    .title-text {
        font-size: 64px !important;
        font-weight: 800 !important;
        background: linear-gradient(90deg, #00ADEF 0%, #F02FC2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0px 10px 30px rgba(0, 173, 239, 0.3);
        letter-spacing: -2px;
        margin-bottom: 10px !important;
    }

    .step-header {
        color: #00ADEF;
        font-size: 0.85rem;
        font-weight: 700;
        letter-spacing: 3px;
        margin-bottom: 20px;
        text-transform: uppercase;
        border-bottom: 1px solid rgba(0, 173, 239, 0.2);
        padding-bottom: 8px;
    }

    /* GLASSMORPHISM CARDS */
    .aha-box { 
        padding: 40px; 
        background: rgba(255, 255, 255, 0.03); 
        border: 1px solid rgba(0, 173, 239, 0.3);
        border-left: 8px solid #00ADEF; 
        border-radius: 20px; 
        margin: 30px 0; 
        box-shadow: 0 20px 40px rgba(0,0,0,0.4);
    }
    
    .aha-box h3 {
        color: #FFFFFF !important;
        font-weight: 800;
        letter-spacing: -1px;
        margin-bottom: 15px !important;
    }

    .phase-card { 
        background: rgba(255, 255, 255, 0.02); 
        padding: 25px; 
        border-radius: 15px; 
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-top: 4px solid #F02FC2; 
        margin-bottom: 20px; 
        transition: transform 0.3s ease;
    }
    
    .phase-card:hover {
        transform: translateY(-5px);
        background: rgba(240, 47, 194, 0.05);
    }

    /* REASONING BREADCRUMB */
    .breadcrumb-box {
        background: rgba(0, 173, 239, 0.05) !important;
        border: 1px solid #00ADEF !important;
        padding: 30px !important;
        border-radius: 20px !important;
        margin: 40px 0 !important;
    }

    /* TABLES: BIG 4 CLINICAL STYLE */
    table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 30px;
        background: rgba(255, 255, 255, 0.02);
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }

    th {
        background: rgba(0, 173, 239, 0.1) !important;
        color: #00ADEF !important;
        text-align: left;
        padding: 20px !important;
        text-transform: uppercase;
        font-size: 11px;
        letter-spacing: 1.5px;
    }

    td {
        padding: 20px !important;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        vertical-align: top;
        font-size: 15px;
        color: rgba(255,255,255,0.8);
    }

    .target-state {
        color: #00ADEF;
        font-weight: 700;
        background: rgba(0, 173, 239, 0.1);
        padding: 4px 12px;
        border-radius: 6px;
    }

    /* BUTTONS: THE GESHIDO ACTION */
    div.stButton > button {
        background: rgba(255, 255, 255, 0.05) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
        height: 55px !important;
        transition: all 0.3s ease !important;
        font-weight: 600 !important;
    }

    div.stButton > button:hover {
        border-color: #00ADEF !important;
        background: rgba(0, 173, 239, 0.1) !important;
        transform: translateY(-2px);
    }

    div.stButton > button[kind="primary"] {
        background: linear-gradient(90deg, #00ADEF, #F02FC2) !important;
        border: none !important;
        height: 65px !important;
        border-radius: 32px !important;
        font-size: 18px !important;
        font-weight: 800 !important;
        letter-spacing: 1px !important;
        box-shadow: 0 10px 30px rgba(0, 173, 239, 0.3) !important;
    }

    /* INPUTS & SELECTS */
    .stSelectbox div[data-baseweb="select"], .stTextArea textarea, .stTextInput input {
        background-color: rgba(255, 255, 255, 0.03) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
        color: white !important;
    }
    
    .stTextArea textarea:focus, .stTextInput input:focus {
        border-color: #00ADEF !important;
        box-shadow: 0 0 15px rgba(0, 173, 239, 0.2) !important;
    }

    </style>
    """, unsafe_allow_html=True)
