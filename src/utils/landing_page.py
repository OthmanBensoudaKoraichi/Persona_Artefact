import streamlit as st
from src.utils import config

def display_landing_page():
    st.title("Générateur de persona & contenu marketing")

    st.write("Bienvenue sur votre plateforme permettant la segmentation de votre audience et la création de persona, couplée à un puissant générateur de campagnes marketing.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Détails des segments")
        st.image(config.explorator)  # Replace 'config.explorator' with the path to your image
        with st.container():
            st.markdown("""
                <style>
                .text-container {
                    background-color: #f0f2f6;
                    border-radius: 10px;
                    padding: 10px;
                    box-shadow: 2px 2px 5px #ccc;
                }
                </style>
                <div class="text-container">
                <p>Découvrez le cœur de votre audience avec le module avancé de segmentation. Découvrez les persona détaillés qui respirent la vie dans votre data, permettant une compréhension profonde et nuancée des clients. Transformez les insights en action et personnalisez votre approche pour atteindre votre public cible de manière plus efficace que jamais.</p>
                </div>
            """, unsafe_allow_html=True)

    with col2:
        st.subheader("Générateur de Créas")
        st.image(config.generator)  # Replace 'config.generator' with the path to your image
        with st.container():
            st.markdown("""
                <style>
                .text-container {
                    background-color: #f0f2f6;
                    border-radius: 10px;
                    padding: 10px;
                    box-shadow: 2px 2px 5px #ccc;
                }
                </style>
                <div class="text-container">
                <p>Lancez des campagnes percutantes avec un outil intuitif de création de campagnes. Le générateur de campagne vous guide selon votre besoin afin de générer le bon format avec des messages pertinents.</p>
                </div>
            """, unsafe_allow_html=True)

    return