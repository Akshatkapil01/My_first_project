# This file will contain the Streamlit application code.
import streamlit as st
import joblib
import pandas as pd
import numpy as np
import google.generativeai as genai
# from google.colab import userdata # Commented out as userdata is not available in Streamlit environment

import streamlit as st
import google.generativeai as genai

# Load CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# App Header
st.markdown("<h1 style='text-align: center; color: #1B5E20; font-size: 3rem;'>🥗 GreenGuide AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #555;'>The smartest way to eat fresh and stay healthy.</p>", unsafe_allow_html=True)
st.markdown("---")

# Layout: 2 Columns for Inputs
col1, col2 = st.columns([2, 1])

with col1:
    user_query = st.text_input("What are you looking for today?", placeholder="e.g. Best summer fruits for energy")

with col2:
    diet_goal = st.selectbox("Your Goal", ["Health", "Weight Loss", "Muscle Gain", "Budget"])

# Action Button
if st.button("✨ Generate My Plan"):
    if user_query:
        with st.spinner("🥬 Harvesting the best advice..."):
            # (Insert your Gemini API Logic Here)
            # example response:
            response_text = "### 🍎 Top Picks\n* **Apples**: High fiber.\n* **Berries**: Antioxidant rich.\n\n### 🥗 Meal Idea\n**Fresh Berry Salad**: Mix greens with blueberries and a citrus dressing."
            
            # This 'div' applies the 'result-card' style from your CSS file
            st.markdown(f'<div class="result-card">{response_text}</div>', unsafe_allow_html=True)
    else:
        st.warning("Please type something first!")


GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"] # For Streamlit Cloud deployment
genai.configure(api_key=GOOGLE_API_KEY)
gemini_model = genai.GenerativeModel('gemini-2.5-flash')

# Load the trained models
models = {
    'A': joblib.load('model_A.joblib'),
    'B12': joblib.load('model_B12.joblib'),
    'B6': joblib.load('model_B6.joblib'),
    'C': joblib.load('model_C.joblib'),
    'D': joblib.load('model_D.joblib'),
    'IRON': joblib.load('model_IRON.joblib')
}

# Define feature columns mapping
feature_cols = {
    'A': 'Vitamin_A',
    'B12': 'Vitamin_B12',
    'B6': 'Vitamin_B6',
    'C': 'Vitamin_C',
    'D': 'Vitamin_D',
    'IRON': 'IRON'
}

# Function to get Gemini recommendation
def get_gemini_recommendation(vitamin_type, is_deficient):
    status_text = "deficient" if is_deficient else "not deficient"
    prompt = f""" Given that a person is {status_text} in {vitamin_type},You are an expert Nutrition Coach and Culinary Assistant. Your  Goal is  to Provide structured recommendations in the following format:

1. 🍎 Fruits (5 specific options commonly available in India)
2. 🥦 Vegetables (5 specific options)
3. 🍛 Complete Indian Meals (Breakfast, Lunch, Dinner examples)
4. 🥜 Nuts/Seeds (if relevant)
5. 💪 Exercises (safe and suitable for this deficiency)
6. ☀️ Lifestyle Advice
7. ⚠️ Foods to Avoid (if applicable)

Guidelines:
- Keep advice practical and affordable
- Mention vegetarian and non-vegetarian options separately if needed
- Avoid medical jargon
- Keep it concise but professional
"""
    try:
        response = gemini_model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Could not retrieve recommendation at this time: {e}"

# Streamlit App UI
st.set_page_config(page_title="Vitamin Deficiency Predictor", layout="centered")
st.title("Vitamin Deficiency Predictor")
st.write("Enter patient details to predict vitamin deficiency and get recommendations.")

# Input widgets
gender_option = st.radio("Select Gender:", ('Male', 'Female'))
gender_encoded = 1 if gender_option == 'Male' else 0

available_vitamins = list(models.keys())
vitamin_type_input = st.selectbox("Select Vitamin Type:", available_vitamins)

vital_level = st.number_input(f"Enter {vitamin_type_input} level:", min_value=0.0, format="%.2f")

if st.button("Predict Deficiency"):
    # Prepare input data for prediction
    input_data_dict = {'gender': gender_encoded}

    # Initialize all vitamin value columns to 0.0
    for vc_name in feature_cols.values():
        input_data_dict[vc_name] = 0.0
    # Set the specific vitamin level
    input_data_dict[feature_cols[vitamin_type_input]] = vital_level

    # Initialize all vitamin type dummy columns to 0
    for vt_key in models.keys():
        input_data_dict[f'vitamin_type_{vt_key}'] = 0
    # Set the specific vitamin type dummy variable to 1
    input_data_dict[f'vitamin_type_{vitamin_type_input}'] = 1

    # Ensure all required columns are present and in correct order for the model
    # The models were trained on X = df[['gender','Vitamin_A','vitamin_type_A']] etc.
    # We need to construct the input_df with only the features relevant to the selected model.
    model_feature_columns = ['gender', feature_cols[vitamin_type_input], f'vitamin_type_{vitamin_type_input}']
    input_df = pd.DataFrame([input_data_dict], columns=model_feature_columns)

    # Make prediction
    selected_model = models[vitamin_type_input]
    prediction = selected_model.predict(input_df)[0]

    # Display prediction result
    if prediction == 1:
        st.error(f"Prediction: Deficient in {vitamin_type_input}")
        is_deficient = True
    else:
        st.success(f"Prediction: Not deficient in {vitamin_type_input}")
        is_deficient = False

    # Get and display Gemini recommendation
    st.markdown("### Recommendation")
    recommendation = get_gemini_recommendation(vitamin_type_input, is_deficient)
    st.info(recommendation)

