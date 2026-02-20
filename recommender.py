import streamlit as st
import google.generativeai as genai

# 1. PAGE CONFIGURATION (Must be the very first Streamlit command)
st.set_page_config(
    page_title="GreenGuide AI",
    page_icon="🥗",
    layout="centered"
)

# 2. PROFESSIONAL CSS STYLING (Injecting styles in a single file)
st.markdown("""
    <style>
    /* Main background */
    .stApp {
        background-color: #f9fbf9;
    }
    /* Style the main title */
    h1 {
        color: #2e7d32;
        font-family: 'Helvetica Neue', sans-serif;
    }
    /* Custom button styling */
    .stButton>button {
        width: 100%;
        border-radius: 25px;
        height: 3em;
        background-color: #4caf50;
        color: white;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #388e3c;
        transform: translateY(-2px);
        color: white;
    }
    /* Info box styling */
    .stAlert {
        border-radius: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. API SETUP
try:
    # Use the secret key you added to the Streamlit dashboard
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    # Using the 2.0-flash model for speed and availability
    model = genai.GenerativeModel('gemini-2.0-flash')
except Exception as e:
    st.error("🔑 API Key Missing! Please add 'GOOGLE_API_KEY' to your Streamlit Secrets.")
    st.stop()

# 4. SIDEBAR SETTINGS
with st.sidebar:
    st.header("⚙️ Preferences")
    diet_type = st.selectbox("Dietary Preference", ["None", "Vegan", "Vegetarian", "Keto", "Paleo"])
    goal = st.radio("What is your goal?", ["Health & Wellness", "Quick Meals", "Budget Friendly"])
    st.divider()
    st.caption("Powered by Gemini 2.0 Flash")

# 5. MAIN INTERFACE
st.title("🥗 GreenGuide AI")
st.subheader("Your Personal Fruit & Veggie Expert")

user_input = st.text_input(
    "What's in your kitchen or what are you craving?", 
    placeholder="e.g. I have tomatoes and cucumber, give me a light meal idea"
)

# 6. RECOMMENDATION LOGIC
if st.button("✨ Get Expert Recommendations"):
    if user_input:
        with st.spinner("🥬 Consulting the garden..."):
            # High-quality specialized prompt
            prompt = f"""
            You are an expert Nutritionist and Chef.
            User Input: {user_input}
            User Diet: {diet_type}
            User Goal: {goal}
            
            Provide recommendations in this exact format:
            1. 🍎 **Top Picks**: 2 Fruits and 2 Vegetables that fit the request.
            2. 🥙 **The Perfect Meal**: One creative recipe name and 3 simple steps to make it.
            3. 💡 **Nutrition Secret**: One fun health fact about these ingredients.
            
            Keep it professional, concise, and use emojis.
            """
            
            try:
                response = model.generate_content(prompt)
                st.markdown("---")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("⚠️ Please enter a fruit, vegetable, or meal preference first!")

# 7. FOOTER
st.divider()
st.center = st.caption("© 2026 GreenGuide AI | Freshness Delivered via Intelligence")
