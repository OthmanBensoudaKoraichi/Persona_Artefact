from src.utils import style, session_state
import streamlit as st
from streamlit_extras.switch_page_button import switch_page


def display_landing_page(explorator_image_path, generator_image_path):
    """
    :param explorator_image_path: Le chemin de l'image "Détails des segments"
    :param generator_image_path: Le chemin de l'image "Générateur de créas"
    :return: Cette fonction affiche la landing page
    """
    # Initialisation de la session state de la sidebar
    session_state.initialize_sidebar()

    # Fonction regroupant le CSS qui sera injecté à la page
    style.css_landing_page()

    # Titre de la page. Le style de h1 est déterminé dans le fichier style.py
    st.markdown(
        '<h1 class="custom-title">Générateur de Persona et Contenu Marketing</h1>',
        unsafe_allow_html=True,
    )

    # Message d'introduction. Le style de st.info est déterminé dans le fichier style.py
    st.info(
        "Bienvenue sur votre plateforme permettant la segmentation de votre audience et la création de persona, couplée à un puissant générateur de campagnes marketing."
    )

    # On crée 2 colonnes
    col1, col2 = st.columns(2)

    # On affiche le générateur de créas dans la première colonne pour qu'il soit à gauche
    with col1:
        # Titre en haut de l'image. Style déterminé dans le fichier style.py.
        st.markdown(
            '<div class="image-header"><b>Générateur de Créas</b></div>',
            unsafe_allow_html=True,
        )
        # Image. Style déterminé dans le fichier style.py.
        st.markdown(
            f'<div class="responsive-image"><img src="{generator_image_path}"></div>',
            unsafe_allow_html=True,
        )
        # Texte en dessous de l'image. Style déterminé dans le fichier style.py.
        st.markdown(
            '<div class="text-below-image">Lancez des campagnes percutantes avec un outil intuitif de création de campagnes. Le générateur de campagne vous guide selon votre besoin afin de générer le bon format avec des messages pertinents.</div>',
            unsafe_allow_html=True,
        )

        # Bouton du générateur de créas
        if st.button("Utiliser le générateur", key="generator"):
            # On switch à la page "Générateur de créas"
            switch_page("générateur de créas")

    # On affiche le détail des segments dans la deuxième colonne pour qu'il soit à gauche
    with col2:
        # Titre en haut de l'image. Style déterminé dans le fichier style.py.
        st.markdown(
            '<div class="image-header"><b>Détails des segments</b></div>',
            unsafe_allow_html=True,
        )
        # Image. Style déterminé dans le fichier style.py.
        st.markdown(
            f'<div class="responsive-image"><img src="{explorator_image_path}"></div>',
            unsafe_allow_html=True,
        )
        # Texte en dessous de l'image. Style déterminé dans le fichier style.py.
        st.markdown(
            '<div class="text-below-image">Découvrez le cœur de votre audience grâce à notre module avancé de segmentation. Explorez les personas détaillés issus de vos données pour une meilleure compréhension de vos clients, et adaptez votre approche marketing avec précision.</div>',
            unsafe_allow_html=True,
        )

        # Bouton du détail des segments
        if st.button("Explorer les segments", key="explorator"):
            # On switch à la page "détails des personae"
            switch_page("détails des personae")

    return
