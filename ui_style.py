import streamlit as st

def apply_custom_style():

    st.set_page_config(
        page_title="AI Vitamin Deficiency Predictor",
        page_icon="🧬",
        layout="centered"
    )

    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #f8fbff, #e6f0fa);
    }

    .main-card {
        background: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 6px 20px rgba(0,0,0,0.1);
    }

    .title {
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        color: #1f4e79;
    }

    .result-box {
        padding: 20px;
        border-radius: 10px;
        font-size: 18px;
        font-weight: bold;
        text-align: center;
    }

    .success-box {
        background-color: #e6f4ea;
        color: #137333;
    }

    .warning-box {
        background-color: #fdecea;
        color: #b3261e;
    }

    .stButton>button {
        background-color: #1f77b4;
        color: white;
        border-radius: 8px;
        height: 45px;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)
