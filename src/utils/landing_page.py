import streamlit as st
from src.utils import config

def display_landing_page(explorator_path,generator_path):
    st.title("Générateur de persona & contenu marketing")

    st.write("Bienvenue sur votre plateforme permettant la segmentation de votre audience et la création de persona, couplée à un puissant générateur de campagnes marketing.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Détails des segments")
        st.image(explorator_path)  # Replace with the path to your first image
        st.write("Découvrez le cœur de votre audience avec le module avancé de segmentation. Transformez les insights en action et personnalisez votre approche pour atteindre votre public cible de manière plus efficace que jamais.")

    with col2:
        st.subheader("Générateur de Créas")
        st.image(generator_path)  # Replace with the path to your second image
        st.write("Lancez des campagnes percutantes avec un outil intuitif de création de campagnes. Le générateur de campagne vous guide selon votre besoin afin de générer le bon format avec des messages pertinents.")

    return