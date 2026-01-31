import google.generativeai as genai
import streamlit as st
import re

def run_strategy_engine(friction, anchor, pivot=None):
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        model_list = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        selected_model = next((m for m in model_list if 'gemini-1.5-flash' in m), model_list[0])
        model = genai.GenerativeModel(selected_model)
        
        prompt = f"""
        Role: Senior AI Strategy Lead at IQ Business.
        Framework: Use the Explorer/Scaler/Innovator maturity model.
        Context: Meridian Financial Group Discovery.
        Legacy Anchor: {anchor}
        Discovery Notes: "{friction}"
        {"Strategic Pivot Requested: " + pivot if pivot else ""}
        
        REQUIRED OUTPUT (HTML ONLY):
        1. <div class='aha-box'>
           <h3>Strategic Diagnosis: [INSERT PERSONA - Explorer, Scaler, or Innovator]</h3>
           <p><strong>Clinical Pattern:</strong> [Provide a direct, 1-sentence business observation linking their friction to their maturity level. Avoid academic jargon.]</p>
           </div>

        2. <h3>Mobilisation Blueprint: The Agentic Strangler</h3>
        <p><strong>Target:</strong> Wrapping {anchor} to drive immediate EBIT impact without technical debt.</p>
        <div class='phase-card'><h4>Phase 1: Surround (7 Days)</h4><p>[Describe a Smallest Unit of Value (SUV) win that builds board belief]</p></div>
        <div class='phase-card'><h4>Phase 2: Synthesize (28 Days)</h4><p>[Describe a foundational gap closure, e.g., Data Sovereignty or Risk framework]</p></div>

        3. <h3>90-Day Outcome & ROI Projection</h3>
        <table>
          <thead><tr><th>Metric</th><th>Current</th><th>AI Target</th><th>Logic Path</th></tr></thead>
          <tbody>
            <tr><td>Revenue Velocity</td><td>Legacy</td><td><span class='target-state'>Accelerated</span></td><td>[1 sentence on how AI removes the specific anchor bottleneck]</td></tr>
            <tr><td>Trust/Risk Score</td><td>Manual</td><td><span class='target-state'>Auditable</span></td><td>[1 sentence on integrated governance/POPIA compliance]</td></tr>
          </tbody>
        </table>

        4. <div style='background: rgba(255,255,255,0.05); padding: 20px; border-radius: 10px; border: 1px solid #00ADEF;'>
           <h4>Strategic Reasoning (The 'Breadcrumb')</h4>
           <p>[Provide a professional justification for these targets. Use the 'Directionally Accurate' framing. DO NOT use the name Biase or Senior Partner in the text.]</p>
           </div>
        
        STRICT: Use professional, crisp executive language. No markdown code blocks. No bold stars (**). No mention of 'AI' or 'Senior Partner' in headers.
        """
        
        response = model.generate_content(prompt)
        return re.sub(r"```[a-z]*\n?|```|\*\*", "", response.text).strip()
    except Exception as e:
        return f"<div style='color:red;'>Engine Error: {str(e)}</div>"
