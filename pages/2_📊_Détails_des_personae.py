from src.utils import style,config,persona_display
import streamlit as st
from st_clickable_images import clickable_images
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
import matplotlib.pyplot as plt


# Import dataset
data = pd.read_excel('/Users/othmanbensouda/PycharmProjects/Persona_Artefact/files/master_table_fictif.xlsx')

# Set page layout
st.set_page_config(layout="wide")


# Make images clickable, so that we can switch pages when we click on them
cluster_selected = clickable_images(
    [
        config.persona_images['first_persona'],
        config.persona_images['second_persona'],
        config.persona_images['third_persona'],
        config.persona_images['fourth_persona'],
        config.persona_images['fifth_persona'],
    ],
    titles=[f"Image #{str(i)}" for i in range(5)],
    div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
    img_style={"margin": "5px", "height": "200px", "transition": "transform 0.2s", "cursor": "pointer"},
)

# Create a single column
col1,col2,col3 = st.columns([1,1,1])

with col2:
    if st.button('Générer une campagne marketing',type = "primary"):
        switch_page("générateur de créas")


if cluster_selected == 0:
    # Change what is displayed in the sidebar

    persona_display.display_persona_in_sidebar('first_persona')
    # Change the numbers displayed in the details

if cluster_selected == 1:

    persona_display.display_persona_in_sidebar('second_persona')

if cluster_selected == 2:
    persona_display.display_persona_in_sidebar('third_persona')


if cluster_selected == 3:
    persona_display.display_persona_in_sidebar('fourth_persona')


if cluster_selected == 4:
    persona_display.display_persona_in_sidebar('fifth_persona')


# Onglets dans l'interface principale
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Overview","Comportement","Financial Health", "Transactions","Équipements"
])

with tab1:
    st.header(f"Overview for Cluster {cluster_selected}")
    # Calculs et affichage spécifique au cluster
    average_age = data[data['cluster'] == cluster_selected]['age'].mean()
    age_distribution = data[data['cluster'] == cluster_selected]['age'].value_counts().sort_index()
    gender_distribution = data[data['cluster'] == cluster_selected]['genre'].value_counts()

    # Affichage des statistiques
    st.subheader('Moyenne d\'âge')
    st.write(f'{average_age:.1f} ans')

    st.subheader('Distribution par Âge')
    st.bar_chart(age_distribution)

    st.subheader('Distribution par Genre')
    st.bar_chart(gender_distribution)

# Vous pouvez personnaliser chaque onglet avec des informations pertinentes par cluster
with tab2:
    st.header(f"Comportement pour Cluster {cluster_selected}")
    # Affichage spécifique du comportement du cluster

with tab3:
    st.header(f"Health financière pour Cluster {cluster_selected}")
    # Affichage spécifique de la santé financière du cluster

with tab4:
    st.header(f"Transactions pour Cluster {cluster_selected}")
    # Affichage spécifique des transactions du cluster

with tab5:
    st.header(f"Équipements pour Cluster {cluster_selected}")
    # Affichage spécifique des équipements du cluster

css_tabs = st.markdown("""
<style>
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;  /* Spacing between tabs */
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;  /* Height of each tab */
        white-space: pre-wrap;  /* Wrap text inside tabs */
        background-color: #F6F6F6;  /* Background color of unselected tabs */
        border-radius: 4px 4px 0 0;  /* Rounded corners on the top of tabs */
        padding-top: 10px;  /* Top padding */
        padding-bottom: 10px;  /* Bottom padding */
        padding-left : 5px;
        padding-right : 5px;
        border: none;  /* Remove borders */
        box-shadow: 0px px 0px 0px rgba(0,0,0,0.1);  /* Subtle shadow under tabs */
        font-size: 40px;  /* Font size */
        color: #656565;  /* Default text color (lighter grey) */
        transition: color 0.3s; /* Smooth transition for color change */
    }
    .stTabs [aria-selected="true"] {
        background-color: #B3E5E5;  /* Background color of the selected tab */
        box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.05);  /* Shadow for selected tab to lift it visually */
        color: #FFFFFF;
    }
    .stTabs [data-baseweb="tab"]:hover,
    .stTabs [data-baseweb="tab"]:focus {
        color: #FFFFFF; /* Text color when tab is hovered or focused (darker grey) */
    }
    .stTabs [data-baseweb="tab"]:hover {
        background-color: #B3E5E5;  /* Background color on hover */
    }
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-weight: 550;
        font-size: 1.5rem;
    }
    .stTabs [data-baseweb="tab-highlight"] {
    background-color:teal;
    }
</style>
""", unsafe_allow_html=True)

st.markdown(css_tabs, unsafe_allow_html=True)