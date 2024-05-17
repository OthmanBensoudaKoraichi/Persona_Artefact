import streamlit as st
from src.utils import config
from st_clickable_images import clickable_images


def set_background_image(image_path, opacity=0):
    """
    Fonction qui permet de configurer l'image de fond sur la page d'accueil
    :param image_path: Le chemin de l'image
    :param opacity: L'opacité allant de 0 (visible) à 1 (transparent)
    """
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: linear-gradient(rgba(255, 255, 255, {opacity}), rgba(255, 255, 255, {opacity})), url("{image_path}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """,
        unsafe_allow_html=True,
    )


def display_logo(logo_path):
    """
    Fonction qui permet d'afficher le logo de BOA en haut à gauche
    :param logo_path: Chemin du logo
    """
    st.markdown(
        """
        <style>
        header .css-1lcbmhc.e1fqkh3o3 {
            display: flex;
            justify-content: center; /* Center the content in the header */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.image(logo_path, width=400)

    return


def display_persona_in_sidebar(persona: str):
    """
    Fonction qui permet d'afficher la persona dans la sidebar
    :param persona: Nom de la persona qu'on affiche
    """
    # On prend le chemin de la persona dans le dictionnaire présent dans le fichier config.py
    persona_image_url = config.persona_images[persona]

    with st.sidebar:
        st.sidebar.markdown(
            f"""
            <style>
            img {{
                display: block;  /* Centers the image */
                margin-left: auto;
                margin-right: auto;
                width: 60%;  /* Adjust the width as needed */
                height: auto;
                border-radius: 50%;  /* Perfect circle */
                box-shadow: 0px 0px 0px rgba(0, 0, 0, 0); /* Soft shadow around the image */
            }}
            .content-box {{
                background-color: #FBFBFB;  /* Stylish light grey background */
                padding: 20px;              /* Padding around the content */
                border-radius: 8px;        /* Rounded corners for the box */
                box-shadow: 0 4px 8px rgba(0,0,0,0.1); /* Subtle shadow for depth */
                margin: 10px 0;             /* Vertical spacing between elements */
            }}
            .big-font, .regular-sidebar-font {{
                font-size: 20px;  /* Consistent font size */
                overflow-y: auto;
                word-wrap: break-word;
                white-space: normal;
                text-align: justify;
            }}
            .big-font {{
                font-size: 25px; /* Larger font size for headers */
                text-align: center;
            }}
            </style>
            <img src="{persona_image_url}">
            """,
            unsafe_allow_html=True,
        )

        # Contenu du header
        header_content = f"""
        <div class="big-font content-box">
            <strong>{config.persona_info[persona]}</strong>
        </div>
        """

        st.markdown(header_content, unsafe_allow_html=True)

        # Contenu de la description, qu'on prend d'un dictionnaire présent dans config.py
        body_content = config.persona_descriptions[persona]
        st.markdown(
            f"<div class='regular-sidebar-font content-box'>{body_content}</div>",
            unsafe_allow_html=True,
        )

    return


def css_landing_page():
    st.markdown(
        """
        <style>
            .responsive-image img {
                display: block;
                margin: auto;
                max-width: 100%;
                height: 500px;  # Set a fixed height for both images
            }
            .image-header {
                text-align: center;
                position: relative;
                top: 0;
                width: 100%;
                font-size: 24px;  /* Large font size */
                font-weight: bold;  /* Bold text */
                color: #1A4376 !important;  /* Color of the text */
            }
            .text-below-image {
                margin-top: 30px;  /* Add more margin between image and text */
                background-color: rgba(230, 242, 255, 1);
                padding: 15px;
                text-align: center;
                border-radius: 10px;
                border: 1px solid #003366;
                color: #003366;
                font-size: 0.8vw;
                margin-left: 0;
                margin-right: auto;
                max-width: fit-content;
            }
            .info-container {
                width: auto;  /* Set width to auto for the info container */
            }
            .stButton>button {
                display: block;
                margin: 20px auto;  # Center button and add margin
            }
              /* Targeting the Streamlit Info component */
            div[role="alert"] {
                width: auto;  /* Adjust width to content */
                max-width: 50%;  /* Set a maximum width; adjust as necessary */
                margin-left: 0;  /* Center align the box */
                margin-right: auto;
            }
            h1.custom-title {
                font-size: 36px !important;
                font-weight: bold !important;
                color: #1A4376 !important;
            }
        </style>
        
    """,
        unsafe_allow_html=True,
    )

    return


def css_tabs():
    """
    Fonction qui permet de configurer le CSS des onglets (ex : Overview, transactions etc..)
    """
    css_tabs = """
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
    """

    return css_tabs

def display_clickable_clusters() :
    """
    Cette fonction affiche des bulles cliquables de nos 5 personae.
    Elle retourne le cluster cliqué.
    """
    cluster_selected = clickable_images(
        [
            config.persona_images["first_persona"],
            config.persona_images["second_persona"],
            config.persona_images["third_persona"],
            config.persona_images["fourth_persona"],
            config.persona_images["fifth_persona"],
        ],
        titles=[f"Image #{str(i)}" for i in range(5)],
        div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
        img_style={
            "margin": "5px",
            "height": "150px",
            "transition": "transform 0.2s",
            "cursor": "pointer",
        },
    )

    # On crée 3 colonnes
    col1, col2, col3 = st.columns([1, 1, 1])

    # with col2:
    # if st.button('Générer une campagne marketing',type = "primary"):
    # switch_page("générateur de créas")

    # On change ce qui s'affiche dans la sidebar selon le cluster sur lequel l'utilisateur a cliqué
    if cluster_selected == 0:
        display_persona_in_sidebar("first_persona")
        # On change les graphiques selon le cluster sur lequel l'utilisateur a cliqué

    if cluster_selected == 1:
        display_persona_in_sidebar("second_persona")

    if cluster_selected == 2:
        display_persona_in_sidebar("third_persona")

    if cluster_selected == 3:
        display_persona_in_sidebar("fourth_persona")

    if cluster_selected == 4:
        display_persona_in_sidebar("fifth_persona")

    return cluster_selected
