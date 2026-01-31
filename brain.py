import google.generativeai as genai
import streamlit as st
import re

def run_strategy_engine(maturity, friction, anchor):
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        
        # RESILIENCE FIX: Automatically find a valid model name
        model_list = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        # Prefer gemini-1.5-flash for speed in live discovery
        selected_model = next((m for m in model_list if 'gemini-1.5-flash' in m), model_list[0])
        
        model = genai.GenerativeModel(selected_model)
        
        prompt = f"""
Role: Senior AI Strategy Partner at IQ Business (Biase De Gregorio style).
Scenario: Meridian Financial Group Discovery.
Input Friction: "{friction}"
Technical Anchor: "{anchor}"

TASK:
1. DIAGNOSIS: Analyze the Friction text. Determine if they are an EXPLORER, SCALER, or INNOVATOR based on iqbusiness personas.
2. MOBILISATION BLUEPRINT: Create a Delta 7/28 roadmap.
3. IMPACT TABLE: Generate 2026 banking EBIT targets.

OUTPUT STRUCTURE (HTML ONLY):
<div class='aha-box'>
  <h3>Strategic Diagnosis: [INSERT PERSONA HERE]</h3>
  <p>Pattern Recognized: [1 clinical sentence on why they are that persona]</p>
</div>
        
        OUTPUT STRUCTURE (HTML ONLY):
        1. <div class='executive-brief'>
           <h3>Mobilisation Blueprint</h3>
           <p><strong>Agentic Strangler Target:</strong> Using AI to wrap {anchor} without disruption.</p>
           </div>
           
        2. <div class='phase-card'>
           <h4>Phase 1: Surround (7 Days)</h4>
           <p>Deliver visible 'Reason to Believe' win: [Generate specific banking win]</p>
           </div>
           
        3. <div class='phase-card'>
           <h4>Phase 2: Synthesize (28 Days)</h4>
           <p>Close foundational gap: [Generate specific POPIA/Data Sovereignty win]</p>
           </div>

        4. <table>
           <thead><tr><th>Metric</th><th>Current</th><th>AI Target</th><th>Human-in-the-Loop Gate</th></tr></thead>
           <tbody>
             <tr><td>Onboarding Speed</td><td>Days</td><td><span class='target-state'>Minutes</span></td><td>Final KYC approval</td></tr>
             <tr><td>Regulatory Risk</td><td>High</td><td><span class='target-state'>Auditable</span></td><td>Policy override review</td></tr>
           </tbody>
           </table>
        
        STRICT: Use clinical, high-stakes language. No markdown stars (**). No code blocks (```).
        """
        
        response = model.generate_content(prompt)
        # Surgical cleanup of markdown artifacts to protect the UI
        return re.sub(r"```[a-z]*\n?|```|\*\*", "", response.text).strip()
    except Exception as e:
        return f"<div style='color:red;'>Strategic Engine Error: {str(e)}</div>"
