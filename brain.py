import google.generativeai as genai
import streamlit as st
import re

def run_strategy_engine(friction, anchor):
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        model_list = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        selected_model = next((m for m in model_list if 'gemini-1.5-flash' in m), model_list[0])
        model = genai.GenerativeModel(selected_model)
        
        prompt = f"""
        Role: Senior Partner at IQ Business (Biase De Gregorio style).
        Context: Meridian Financial Group Discovery.
        Legacy Anchor: {anchor}
        Discovery Notes: "{friction}"
        
        TASK:
        1. DIAGNOSIS: Based on the Discovery Notes, identify if the client is an EXPLORER, SCALER, or INNOVATOR.
        2. BLUEPRINT: Create a Delta 7/28 roadmap (Value Weekly, Foundations Monthly).
        3. STRANGLER: Explain how we will "wrap" the {anchor} system.

        OUTPUT STRUCTURE (HTML ONLY):
        <div class='aha-box'>
          <h3>Strategic Diagnosis: [INSERT PERSONA]</h3>
          <p><strong>Clinical Pattern:</strong> [1 sentence identifying why they are in this phase based on iqbusiness thought leadership]</p>
        </div>

        <h3>Mobilisation Blueprint: The Agentic Strangler</h3>
        <p>Target: Wrapping {anchor} in an AI brain to drive immediate EBIT impact.</p>
        
        <div class='phase-card'>
          <h4>Phase 1: Surround (7 Days)</h4>
          <p><strong>SUV (Smallest Unit of Value):</strong> [Specific Banking Win for Retail digital channels]</p>
        </div>

        <div class='phase-card'>
          <h4>Phase 2: Synthesize (28 Days)</h4>
          <p><strong>Foundational Gap:</strong> [Identify specific POPIA or Data Readiness gap to close]</p>
        </div>

        <table>
          <thead><tr><th>Metric</th><th>Current</th><th>AI Target</th><th>Human-in-the-Loop Gate</th></tr></thead>
          <tbody>
            <tr><td>Processing Velocity</td><td>Manual/Legacy</td><td><span class='target-state'>Real-time</span></td><td>Policy override check</td></tr>
            <tr><td>Regulatory Confidence</td><td>Risk-averse</td><td><span class='target-state'>Auditable</span></td><td>Final CRO sign-off</td></tr>
          </tbody>
        </table>
        
        STRICT: Clinical, high-stakes language. No markdown code blocks or stars.
        """
        
        response = model.generate_content(prompt)
        return re.sub(r"```[a-z]*\n?|```|\*\*", "", response.text).strip()
    except Exception as e:
        return f"<div style='color:red;'>Engine Error: {str(e)}</div>"
