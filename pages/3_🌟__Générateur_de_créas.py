from src.utils import style, config, prompt_template, session_state
import streamlit as st
from st_clickable_images import clickable_images

# Fonction pour que la sidebar s'active automatiquement lorsque l'on arrive sur la page
session_state.manage_sidebar_state()

# Affiche le logo de BOA en haut à gauche
style.display_logo(config.logo_boa)

# Affiche les bulles des personae de cliquer sur les images
cluster_selected = style.display_clickable_clusters()


# Set tabs
# Onglets dans l'interface principale
tab1, tab2 = st.tabs(["Média Payant", "Média Direct"])

with tab1:
    # On crée 3 colonnes sous notre premier onglet
    col1, col2, col3 = st.columns(3)

    # Selectbox du canal
    with col1:
        canal = st.selectbox(
            "Canal digital", ["Facebook", "Instagram", "Twitter"]
        )

    # Selectbox des services
    with col2:
        service = st.selectbox("Services", ["Crédit Conso", "Autre"])

    # Selectbox de l'objectif
    with col3:
        objective = st.selectbox("Objectif", ["Conversion", "Notoriété"])

    # Text input de l'utilisateur (prompt de spécification)
    prompt_de_specification = st.text_input(
        "Prompt de spécification",
        placeholder="Merci d'ajouter au besoin votre prompt pour cette campagne",
    )



    # Crée un container
    with st.container(border=True):

        # On ajoute du texte à ce container
        st.write(
            "Pour les critères de conversion spécifiques à Facebook, il est généralement recommandé de faire un mix de vidéos et statiques de format carré (1080x1080) en 3 créas: 2 format avec des messages orientés vers l'incitation à l'ouverture de compte et/ou l'incitative propre au digital."
        )
    if st.button("Générer une créa", key="crea_generation"):
        if cluster_selected == -1:
            st.error("Aucun segment n'a été choisi. Veuillez choisir un segment avant de générer une créa.")
        else:
            with st.container(border=True):
                st.write(prompt_template.generate_crea(segment = config.cluster_names[cluster_selected],caracs_segments= config.caracs_segments[cluster_selected] ,canal = canal,prompt_de_specification = prompt_de_specification))

# Vous pouvez personnaliser chaque onglet avec des informations pertinentes par cluster
with tab2:
    # Affichage spécifique du comportement du cluster
    print("")

st.markdown(style.css_tabs(), unsafe_allow_html=True)
