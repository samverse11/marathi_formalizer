import streamlit as st
import sys
import os

# --- Add src folder to Python path so we can import train_model ---
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from train_model import formalize_sentence  # updated function that retrieves formal sentence

# --- Set Streamlit page config (must be first Streamlit command) ---
st.set_page_config(
    page_title="Marathi Formalizer",
    page_icon="📘",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- Custom CSS for modern look ---
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 15px;
    }
    .stTextArea textarea {
        border-radius: 10px !important;
        border: 2px solid #a47cf3 !important;
        font-size: 18px !important;
    }
    .stButton button {
        background-color: #7b2ff7 !important;
        color: white !important;
        font-weight: 600;
        border-radius: 8px;
        height: 45px;
        width: 200px;
        font-size: 16px;
    }
    .stButton button:hover {
        background-color: #9d5df7 !important;
        transition: 0.3s;
    }
    .title {
        text-align: center;
        color: #4B0082;
        font-size: 40px;
        font-weight: 800;
        margin-top: 10px;
        margin-bottom: 5px;
    }
    .subtitle {
        text-align: center;
        color: #666;
        font-size: 18px;
        margin-bottom: 30px;
    }
    .output-box {
        background: linear-gradient(135deg, #e5d9f2, #f9f8fd);
        border-radius: 12px;
        padding: 15px 20px;
        color: #2c2c54;
        font-size: 20px;
        font-weight: 500;
        box-shadow: 0 4px 10px rgba(0,0,0,0.08);
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- App Title ---
st.markdown("<div class='title'>मराठी वाक्य औपचारिक करणारा ✨</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Convert informal Marathi sentences into formal language</div>", unsafe_allow_html=True)

# --- User Input ---
user_input = st.text_area("अनौपचारिक वाक्य टाका:", height=80, key="input_box")

# --- Button and Output ---
if st.button("Formalize Sentence 🚀"):
    if user_input.strip():
        try:
            formal_sentence = formalize_sentence(user_input)  # ← updated function
            st.markdown(f"<div class='output-box'><b>औपचारिक वाक्य:</b><br>{formal_sentence}</div>", unsafe_allow_html=True)
        except Exception as e:
            st.error(f"त्रुटी आली आहे: {str(e)}")
    else:
        st.warning("कृपया वाक्य टाका.")
