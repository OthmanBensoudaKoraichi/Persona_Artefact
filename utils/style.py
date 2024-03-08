import streamlit as st
from utils import config

def set_bg_image(image_path, opacity=0.9):  # Increase opacity for better visibility

    st.markdown(f"""
    <style>
    .stApp {{
        background-image: linear-gradient(rgba(255, 255, 255, {opacity}), rgba(255, 255, 255, {opacity})), url("{image_path}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """, unsafe_allow_html=True)