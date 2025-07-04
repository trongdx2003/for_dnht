import streamlit as st
from datetime import date
import time
import fordnht

st.set_page_config(
    page_title="For Do Nguyen Ha Trang",
    layout="centered",
    initial_sidebar_state="collapsed"
)

CORRECT_DATING_DATE = date(2021, 7, 23)

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
if "show_main" not in st.session_state:
    st.session_state["show_main"] = False

st.markdown("""
    <style>
        .main .block-container {
            padding-top: 2rem;
            max-width: 600px;
        }
        h1 {
            color: #FF4B4B;
            font-family: 'Segoe UI', sans-serif;
            white-space: nowrap;      
            overflow: hidden;          
            width: 100%;             
        }
        .stDateInput label {
            font-weight: bold;
            font-size: 16px;
        }
        .stButton button {
            border-radius: 10px;
            font-size: 16px;
            padding: 10px 20px;
            text-align: center;
        }
        .stSuccess {
            background-color: #d4f4dd !important;
            color: green !important;
        }
        .stError {
            background-color: #ffe6e6 !important;
            color: red !important;
        }
    </style>
""", unsafe_allow_html=True)

if st.session_state.authenticated and st.session_state.show_main:
    fordnht.show()

elif not st.session_state.authenticated:
    st.title("This app is for Do Nguyen Ha Trang")

    st.markdown("""
        🌟 Before proceeding, I need to confirm that you're really **Do Nguyen Ha Trang** 😊  
        Please answer this question correctly to continue:
    """)

    travel_date = st.date_input(
        "📅 When did we start dating?",
        min_value=date(2021, 1, 1),
        max_value=date(2025, 12, 31)
    )

    if st.button("Verify 🔐"):
        if travel_date == CORRECT_DATING_DATE:
            st.success("✅ Verified successfully!")
            st.session_state.authenticated = True
            st.session_state.show_main = True
            time.sleep(2)
            st.rerun()
        else:
            st.error("❌ The date you entered is incorrect. Please try again.")
