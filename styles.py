import streamlit as st

def apply_iq_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700;800&display=swap');
    
    /* 1. GLOBAL OVERRIDES - HIDE STREAMLIT BRANDING */
    [data-testid="stSidebar"] { display: none !important; }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stHeader"] {background: rgba(0,0,0,0) !important;}

    /* 2. THE FOUNDATION: HIGH-IMPACT IQ BACKGROUND */
    /* Targeting multiple layers to ensure the background takes effect */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
        background: radial-gradient(circle at top right, #1a1b3a, #050a18) !important;
        background-attachment: fixed !important;
        color: #FFFFFF !important;
        font-family: 'Outfit', sans-serif !important;
    }

    /* 3. TYPOGRAPHY: THE IQ "DIGITAL INTEGRATOR" GRADIENT */
    .title-text {
        font-size: clamp(40px, 8vw, 64px) !important;
        font-weight: 800 !important;
        background: linear-gradient(90deg, #00ADEF 0%, #F02FC2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0px 10px 30px rgba(0, 173, 239, 0.3);
        letter-spacing: -2px;
        margin-bottom: 5px !important;
        line-height: 1.1 !important;
    }

    .step-header {
        color: #00ADEF;
        font-size: 0.85rem;
        font-weight: 700;
        letter-spacing: 3px;
        margin-bottom: 25px;
        text-transform: uppercase;
        border-bottom: 1px solid rgba(0, 173, 239, 0.3);
        padding-bottom: 10px;
    }

    /* 4. GLASSMORPHISM ARTIFACTS (Cards) */
    .aha-box { 
        padding: 40px; 
        background: rgba(255, 255, 255, 0.03); 
        border: 1px solid rgba(0, 173, 239, 0.4);
        border-left: 8px solid #00ADEF; 
        border-radius: 20px; 
        margin: 30px 0; 
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(10px);
    }
    
    .aha-box h3 {
        color: #FFFFFF !important;
        font-weight: 800;
        letter-spacing: -1px;
        margin-bottom: 20px !important;
        font-size: 28px !important;
    }

    .phase-card { 
        background: rgba(255, 255, 255, 0.02); 
        padding: 30px; 
        border-radius: 18px; 
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-top: 4px solid #F02FC2; 
        margin-bottom: 25px; 
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    
    .phase-card:hover {
        transform: translateY(-8px);
        background: rgba(240, 47, 194, 0.08);
        border-color: rgba(240, 47, 194, 0.3);
        box-shadow: 0 15px 30px rgba(0,0,0,0.3);
    }

    /* 5. BIG 4 CLINICAL TABLES */
    table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 35px;
        background: rgba(255, 255, 255, 0.01);
        border-radius: 15px;
        overflow: hidden;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }

    th {
        background: rgba(0, 173, 239, 0.15) !important;
        color: #00ADEF !important;
        text-align: left;
        padding: 22px !important;
        text-transform: uppercase;
        font-size: 11px;
        letter-spacing: 2px;
        font-weight: 700;
    }

    td {
        padding: 22px !important;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        vertical-align: top;
        font-size: 15px;
        color: rgba(255,255,255,0.85);
        line-height: 1.6;
    }

    .target-state {
        color: #00ADEF;
        font-weight: 800;
        background: rgba(0, 173, 239, 0.15);
        padding: 5px 14px;
        border-radius: 8px;
        border: 1px solid rgba(0, 173, 239, 0.2);
    }

    /* 6. BUTTONS: THE GESHIDO ACTION PUSH */
    div.stButton > button {
        background: rgba(255, 255, 255, 0.04) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        border-radius: 14px !important;
        height: 58px !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        font-weight: 600 !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    div.stButton > button:hover {
        border-color: #00ADEF !important;
        background: rgba(0, 173, 239, 0.15) !important;
        transform: scale(1.02);
        box-shadow: 0 5px 15px rgba(0, 173, 239, 0.2);
    }

    /* PRIMARY BUTTON: THE ORCHESTRATION GRADIENT */
    div.stButton > button[kind="primary"] {
        background: linear-gradient(90deg, #00ADEF, #F02FC2) !important;
        border: none !important;
        height: 70px !important;
        border-radius: 35px !important;
        font-size: 18px !important;
        font-weight: 800 !important;
        letter-spacing: 2px !important;
        box-shadow: 0 15px 35px rgba(0, 173, 239, 0.4) !important;
    }
    
    div.stButton > button[kind="primary"]:hover {
        transform: scale(1.03) translateY(-3px) !important;
        box-shadow: 0 20px 45px rgba(240, 47, 194, 0.4) !important;
    }

    /* 7. WIDGET CUSTOMIZATION */
    .stSelectbox div[data-baseweb="select"], .stTextArea textarea, .stTextInput input {
        background-color: rgba(255, 255, 255, 0.04) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 14px !important;
        color: white !important;
        padding: 12px !important;
    }
    
    .stTextArea textarea:focus, .stTextInput input:focus {
        border-color: #00ADEF !important;
        box-shadow: 0 0 20px rgba(0, 173, 239, 0.3) !important;
    }

    /* Target labels */
    div[data-testid="stWidgetLabel"] p {
        color: rgba(255,255,255,0.7) !important;
        font-weight: 600 !important;
        font-size: 14px !important;
    }

    </style>
    """, unsafe_allow_html=True)
