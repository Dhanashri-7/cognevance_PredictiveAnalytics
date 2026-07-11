import streamlit as st
import requests
import time

# 1. Page Configuration
st.set_page_config(page_title="ChurnAI | Predictive Analytics", page_icon="🔮", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #f4f6f9; }
    .main-header { font-size: 2.5rem; color: #1E3A8A; font-weight: 800; margin-bottom: 0px; }
    .sub-header { font-size: 1.2rem; color: #64748B; margin-bottom: 30px; }
    .persona-card { background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-header">🔮 ChurnAI: Customer Retention Dashboard</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Real-time predictive analytics powered by Logistic Regression</p>', unsafe_allow_html=True)
st.divider()

# 2. Define Customer Personas (Data + Visuals)
personas = {
    "Sarah (The Loyal VIP)": {
        "features": [1, 0, 1, 0, 0.5, 1, 1, 0.6, 0.4, 0.2, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0],
        "details": {"Tenure": "36 Months", "Spend": "$65.00 /mo", "Contract": "Two Year", "Tech Support": "Yes", "Internet": "DSL", "Status": "VIP Subscriber"}
    },
    "John (The Flight Risk)": {
        "features": [0, 1, 0, 0, 0.05, 1, 0, 0.95, 0.1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1],
        "details": {"Tenure": "2 Months", "Spend": "$95.50 /mo", "Contract": "Month-to-Month", "Tech Support": "No", "Internet": "Fiber Optic", "Status": "New / At-Risk"}
    },
    "Alex (The Budget User)": {
        "features": [1, 0, 0, 0, 0.2, 0, 1, 0.3, 0.1, 0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
        "details": {"Tenure": "14 Months", "Spend": "$35.20 /mo", "Contract": "Month-to-Month", "Tech Support": "No", "Internet": "DSL", "Status": "Standard Subscriber"}
    }
}

# 3. Sidebar: Control Panel
with st.sidebar:
    st.header("⚙️ Control Panel")
    st.info("Select a simulated customer profile to send to our FastAPI backend.")
    
    selected_persona = st.selectbox("Select Customer Profile:", list(personas.keys()))
    active_data = personas[selected_persona]

    st.markdown("---")
    analyze_btn = st.button("🚀 Analyze Customer Data", type="primary", use_container_width=True)

# 4. Main Content Area (Split into two columns)
col1, col2 = st.columns([1, 1.5])

# Left Column: Beautiful Customer ID Card
with col1:
    st.subheader("📋 Customer Profile")
    
    with st.container():
        st.markdown(f"### {selected_persona.split(' ')[0]}")
        st.caption(f"Account Status: {active_data['details']['Status']}")
        
        # Display key metrics in a row
        m1, m2 = st.columns(2)
        m1.metric("Customer Tenure", active_data['details']['Tenure'])
        m2.metric("Monthly Charges", active_data['details']['Spend'])
        
        # Display extra services
        st.markdown("**Service Breakdown:**")
        st.write(f"📄 **Contract Type:** {active_data['details']['Contract']}")
        st.write(f"🌐 **Internet Service:** {active_data['details']['Internet']}")
        st.write(f"🛠️ **Tech Support:** {active_data['details']['Tech Support']}")

# Right Column: AI Results
with col2:
    st.subheader("🤖 AI Prediction Engine")
    
    if analyze_btn:
        with st.spinner("Connecting to API & analyzing neural patterns..."):
            time.sleep(1.2) 
            
            api_url = "http://127.0.0.1:8000/predict"
            try:
                response = requests.post(api_url, json={"features": active_data["features"]})
                
                if response.status_code == 200:
                    result = response.json()
                    prediction = result["prediction"]
                    risk = result["churn_risk_percentage"]
                    
                    st.markdown("#### Model Confidence Score")
                    
                    if prediction == "Churn":
                        st.error(f"🚨 **ALERT: High Flight Risk Detected**")
                        st.metric(label="Probability of Churn", value=f"{risk}%", delta="Critical", delta_color="inverse")
                        st.progress(int(risk))
                        st.warning("💡 **AI Recommendation:** Offer a 20% discount on a 1-year contract upgrade and free Tech Support.")
                    else:
                        st.success(f"✅ **SAFE: Customer is Stable**")
                        st.metric(label="Probability of Churn", value=f"{risk}%", delta="Stable", delta_color="normal")
                        st.progress(int(risk))
                        st.info("💡 **AI Recommendation:** Excellent retention probability. Target for premium service upsell.")
                else:
                    st.warning("Received an error from the API.")
            except Exception as e:
                st.error("🚨 Connection Error: Ensure your FastAPI server (Uvicorn) is running!")
    else:
        st.info("👈 Select a profile on the left and click **Analyze Customer Data** to see the AI in action.")