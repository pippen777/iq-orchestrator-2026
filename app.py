# 02: THE STRANGLER TARGET
st.markdown('<p class="step-header">02 / SELECT LEGACY ANCHOR</p>', unsafe_allow_html=True)

# Added "Other (Custom Target)" to the list
anchor_options = [
    "Legacy Core Banking (Mainframe)", 
    "Siloed CRM", 
    "Fragmented ERP", 
    "Unstructured Data Lake",
    "Other (Custom Target)"
]

selected_anchor = st.selectbox("Which system is currently causing 'Complexity Paralysis'?", anchor_options)

# Show a text box only if "Other" is selected
if selected_anchor == "Other (Custom Target)":
    anchor = st.text_input("Specify the legacy system:", placeholder="e.g., On-premise Claims Engine")
else:
    anchor = selected_anchor
