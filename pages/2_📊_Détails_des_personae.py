from src.utils import style, config, session_state
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd

# Fonction pour que la sidebar s'active automatiquement lorsque l'on arrive sur la page
session_state.manage_sidebar_state()

# Affiche le logo de BOA en haut à gauche
style.display_logo(config.logo_boa)

# Importe le dataset
data = pd.read_excel(
    "/Users/othmanbensouda/PycharmProjects/Persona_Artefact/files/master_table_fictif.xlsx"
)

# Affiche les bulles des personae de cliquer sur les images
cluster_selected = style.display_clickable_clusters()


# On crée les onglets
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["Overview", "Comportement", "Financial Health", "Transactions", "Équipements"]
)

# Graphs de l'onglet overview
with tab1:
    # Calculs et affichage spécifique au cluster
    average_age = data[data["cluster"] == cluster_selected]["age"].mean()
    age_distribution = (
        data[data["cluster"] == cluster_selected]["age"].value_counts().sort_index()
    )
    gender_distribution = data[data["cluster"] == cluster_selected][
        "genre"
    ].value_counts()

    # Affichage des statistiques
    st.subheader("Moyenne d'âge")
    st.write(f"{average_age:.1f} ans")

    st.subheader("Distribution par Âge")
    st.bar_chart(age_distribution)

    st.subheader("Distribution par Genre")
    st.bar_chart(gender_distribution)

# Graphs de l'onglet Comportement
with tab2:
    print("")

# Graphs de l'onglet Financial Health
with tab3:
    print("")

# Graphs de l'onglet transactions
with tab4:
    print("")

# Graphs de l'onglet équipements
with tab5:
    # Affichage spécifique des équipements du cluster
    print("")

# On applique le style des onglets, disponible dans le fichier style.py
st.markdown(style.css_tabs(), unsafe_allow_html=True)
