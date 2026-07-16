# ==========================================
# Loan Prediction System
# ==========================================

import streamlit as st
import pickle

st.set_page_config(
    page_title="Loan Prediction System",
    page_icon="🏦",
    layout="wide"
)

with open("loan_model.pkl", "rb") as file:
    loan_model = pickle.load(file)
with open("education_encoder.pkl", "rb") as file:
    education_encoder = pickle.load(file)
with open("gender_encoder.pkl", "rb") as file:
    gender_encoder = pickle.load(file)
with open("home_encoder.pkl", "rb") as file:
    home_encoder = pickle.load(file)
with open("loan_intent_encoder.pkl", "rb") as file:
    loan_intent_encoder = pickle.load(file)
with open("previous_loan_encoder.pkl", "rb") as file:
    previous_loan_encoder = pickle.load(file)

st.markdown("""
<style>

/* Main App Background */
.stApp {
    background: linear-gradient(to right, #eef2f7, #d9e7ff);
}

/* Main Title */
h1 {
    color: #003366;
    text-align: center;
    font-size: 42px;
}

/* Subheader */
h3 {
    color: #1b4f72;
}

/* Buttons */
div.stButton > button {
    background-color: #0056b3;
    color: white;
    border-radius: 12px;
    height: 55px;
    width: 100%;
    font-size: 18px;
    font-weight: bold;
    border: none;
}

div.stButton > button:hover {
    background-color: #003d80;
    color: white;
}

/* Input Boxes */
.stNumberInput,
.stSelectBox {
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("AI Loan Predictor")

    st.success("🤖 Powered by Machine Learning")

    st.markdown("---")

    st.info("""
**Machine Learning Project**

✅ Random Forest

✅ Streamlit

✅ Python

✅ Scikit-learn
""")

    st.markdown("---")

    st.caption("Version 1.0")

st.markdown("""
<div style='background:linear-gradient(90deg,#004e92,#000428);
padding:25px;
border-radius:15px;
text-align:center;
color:white;
box-shadow:0px 4px 15px rgba(0,0,0,0.3);'>

<h1>🏦 AI Loan Approval Prediction System</h1>

<p style="font-size:20px;">
Predict whether a loan application will be approved using Machine Learning.
</p>

</div>
""", unsafe_allow_html=True)

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="🎯 Accuracy",
        value="98.2%"
    )

with col2:
    st.metric(
        label="🤖 Model",
        value="Random Forest"
    )

with col3:
    st.metric(
        label="⚡ Prediction",
        value="< 1 sec"
    )

st.divider()

with st.container(border=True):
    st.markdown("""
    ## 👤 Applicant Information

    Please enter the applicant's financial details below.
    """)

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("🎂 Age", min_value=18, max_value=100, value=25)

    with col2:
        gender = st.selectbox("👤 Gender", ["male", "female"])

    col1, col2 = st.columns(2)

    with col1:
        education = st.selectbox(
            "🎓 Education",
            ["High School", "Bachelor", "Master", "Associate"]
        )

    with col2:
        person_income = st.number_input(
            "💰 Annual Income",
            min_value=0.0,
            max_value=10000000.0
        )

    col1, col2 = st.columns(2)

    with col1:
        employee_experience = st.number_input(
            "💼 Work Experience",
            min_value=0.0,
            max_value=60.0
        )

    with col2:
        home_onwership = st.selectbox(
            "🏠 Home Ownership",
            ["RENT", "OWN", "MORTGAGE"]
        )

    col1, col2 = st.columns(2)

    with col1:
        loan_amount = st.number_input(
            "💵 Loan Amount"
        )

    with col2:
        loan_intent = st.selectbox(
            "🎯 Loan Intent",
            [
                "PERSONAL",
                "EDUCATION",
                "MEDICAL",
                "VENTURE",
                "HOMEIMPROVEMENT",
                "DEBTCONSOLIDATION"
            ]
        )

    col1, col2 = st.columns(2)

    with col1:
        loan_interest_rate = st.number_input(
            "📈 Interest Rate"
        )

    with col2:
        loan_percentage = st.number_input(
            "📊 Loan Percentage",
            min_value=0.0,
            max_value=100.0
        )

    col1, col2 = st.columns(2)

    with col1:
        credit_history = st.number_input(
            "📅 Credit History"
        )

    with col2:
        credit_score = st.number_input(
            "⭐ Credit Score",
            min_value=300,
            max_value=850
        )

    previous_loan = st.selectbox(
        "📜 Previous Loan",
        ["Yes", "No"]
    )

# Input Validation
if person_income <= 0:
    st.error("Annual income must be greater than 0.")
    st.stop()

if loan_amount <= 0:
    st.error("Loan amount must be greater than 0.")
    st.stop()

if employee_experience > age:
    st.error("Work experience cannot be greater than age.")
    st.stop()

if loan_interest_rate <= 0:
    st.error("Interest rate must be greater than 0.")
    st.stop()

if credit_history < 0:
    st.error("Credit history cannot be negative.")
    st.stop()

col1, col2 = st.columns(2)

with col1:
    predict = st.button("🔍 Predict Loan", use_container_width=True)

with col2:
    reset = st.button("🔄 Reset", use_container_width=True)

if reset:
    st.rerun()

if predict:
    education_text = education
    gender_text = gender
    home_text = home_onwership
    loan_intent_text = loan_intent
    previous_loan_text = previous_loan
    # Encode categorical features
    gender = gender_encoder.transform([gender])[0]
    education = education_encoder.transform([education])[0]
    home_onwership = home_encoder.transform([home_onwership])[0]
    loan_intent = loan_intent_encoder.transform([loan_intent])[0]
    previous_loan = previous_loan_encoder.transform([previous_loan])[0]

    # Create input data
    input_data = [[
        age,
        gender,
        education,
        person_income,
        employee_experience,
        home_onwership,
        loan_amount,
        loan_intent,
        loan_interest_rate,
        loan_percentage,
        credit_history,
        credit_score,
        previous_loan
    ]]

    prediction = loan_model.predict(input_data)
    prediction_proba = loan_model.predict_proba(input_data)

    if prediction[0] == 1:
        confidence = prediction_proba[0][1] * 100
    else:
        confidence = prediction_proba[0][0] * 100

    if prediction[0] == 1:

        st.markdown(f"""
        <div style="
        background: linear-gradient(135deg,#eafaf1,#d5f5e3);
        padding:12px 18px;
        border-radius:16px;
        border-left:2px solid #28a745;
        box-shadow:0px 4px 10px rgba(0,0,0,0.15);
        ">

        <h3 style="
        color:#198754;
        margin:0;
        ">
        ✅ Loan Approved
        </h3>

        <p style="
        margin:8px 0 12px 0;
        font-size:17px;
        color:#444;
        ">
        Congratulations! Your loan is likely to be approved.
        </p>

        <div style="
        background:white;
        padding:4px 2px;
        border-radius:10px;
        text-align:center;
        ">

        <div style="
        font-size:16px;
        color:gray;
        margin-bottom:3px;
        ">
        🎯 Confidence Score
        </div>
        
        <div style="
        font-size:18px;
        font-weight:bold;
        color:#198754;
        ">
        {confidence:.2f}%
        </div>
        </div>
        
        </div>
        
        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown(f"""
        <div style="
        background: linear-gradient(135deg,#fdeaea,#fadbd8);
        padding:12px 18px;
        border-radius:16px;
        border-left:2px solid #dc3545;
        box-shadow:0px 4px 10px rgba(0,0,0,0.15);
        ">

        <h3 style="
        color:#dc3545;
        margin:0;
        ">
        ❌ Loan Rejected
        </h3>

        <p style="
        margin:8px 0 12px 0;
        font-size:18px;
        color:#444;
        ">
        Unfortunately, your loan is likely to be rejected.
        </p>

        <div style="
        background:white;
        padding:4px 2px;
        border-radius:10px;
        text-align:center;
        ">

        <div style="
        font-size:14px;
        color:gray;
        ">
        🎯 Confidence Score
        </div>
        
        <div style="
        font-size:18px;
        font-weight:bold;
        color:#dc3545;
        ">
        {confidence:.2f}%
        </div> 
        
        </div>

        </div>
        """, unsafe_allow_html=True
        )


    st.divider()

    st.markdown("## 📋 Applicant Summary")

    summary_col1, summary_col2 = st.columns(2)

    with summary_col1:
        st.write(f"**👤 Age:** {age}")
        st.write(f"**🎓 Education:** {education_text}")
        st.write(f"**💰 Annual Income:** {person_income}")
        st.write(f"**🏠 Home Ownership:** {home_text}")

    with summary_col2:
        st.write(f"**💵 Loan Amount:** {loan_amount}")
        st.write(f"**⭐ Credit Score:** {credit_score}")
        st.write(f"**📈 Interest Rate:** {loan_interest_rate}")
        st.write(f"**📅 Credit History:** {credit_history}")

    st.markdown("---")

    st.markdown(
        """
    <div style="
    text-align:center;
    color:gray;
    font-size:16px;
    ">
    🏦 AI Loan Approval Prediction System
    <br>Developed by <b>Syeda Faiza Adil</b><br>
    Python • Streamlit • Scikit-learn • Random Forest
    </div>
    """, unsafe_allow_html=True
    )
