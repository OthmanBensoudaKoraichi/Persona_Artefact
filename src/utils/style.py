import streamlit as st
import pandas as pd
import numpy as np

def set_bg_image(image_path, opacity=0):  # Adjust opacity as needed
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

def display_logo(logo_path):
    # CSS pour centrer l'image du logo
    st.markdown("""
        <style>
        header .css-1tkidbn.e1fqkh3o3 {
            justify-content: center;  /* Centrer le contenu dans l'en-tête */
        }
        </style>
        """, unsafe_allow_html=True)

    # Remplacer 'url_or_path_to_your_logo.png' par le chemin ou l'URL de votre logo
    st.image(logo_path, width=500)  # Ajustez la largeur selon vos besoins

    return

