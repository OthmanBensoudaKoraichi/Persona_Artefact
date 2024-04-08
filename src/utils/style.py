import streamlit as st
import pandas as pd
import numpy as np

def set_bg_image(image_path, opacity=0.1):  # Adjust opacity as needed
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

def create_interface():
    print('')
