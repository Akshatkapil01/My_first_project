import streamlit as st

def show_recommendation(fruits, vegetables, meals, exercises):

    st.markdown("""
    <style>
    .rec-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
        margin-bottom: 15px;
    }

    .rec-title {
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="rec-card">', unsafe_allow_html=True)
        st.markdown('<div class="rec-title">🍎 Fruits</div>', unsafe_allow_html=True)
        for item in fruits:
            st.write("•", item)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="rec-card">', unsafe_allow_html=True)
        st.markdown('<div class="rec-title">🥦 Vegetables</div>', unsafe_allow_html=True)
        for item in vegetables:
            st.write("•", item)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="rec-card">', unsafe_allow_html=True)
        st.markdown('<div class="rec-title">🍛 Meals</div>', unsafe_allow_html=True)
        for item in meals:
            st.write("•", item)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="rec-card">', unsafe_allow_html=True)
        st.markdown('<div class="rec-title">💪 Exercises</div>', unsafe_allow_html=True)
        for item in exercises:
            st.write("•", item)
        st.markdown('</div>', unsafe_allow_html=True)
