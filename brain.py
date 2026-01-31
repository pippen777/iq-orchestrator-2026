import google.generativeai as genai
import streamlit as st
import re

def run_strategy_engine(maturity, friction, scenario="Meridian Financial"):
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    prompt = f"""
    Context: {scenario} | Maturity: {maturity} | Friction: {friction}
    Role: Senior Partner at IQ Business (Biase De Gregorio style).
    
    Structure your response using HTML for a beautiful dashboard:
    1. A 'Mobilisation Blueprint' div with 3 Phase Cards.
    2. An 'Impact Table' (EBIT, Risk, Capacity).
    3. The 'Agentic Strangler' candidate identified.
    
    Use clinical, high-stakes executive language.
    """
    
    response = model.generate_content(prompt)
    return re.sub(r"```[a-z]*\n?|```|\*\*", "", response.text).strip()
