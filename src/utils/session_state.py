import streamlit as st
from src.utils import config


def initialize_sidebar():
    """
    Fonction qui permet d'initialiser l'état de la sidebar
    """
    if "sidebar_state" not in st.session_state:
        st.session_state.sidebar_state = "collapsed"
    else:
        st.session_state.sidebar_state = "expanded"

    return


def set_config():
    """
    Fonction qui permet de configurer nos pages, dont l'affichage (étroit ou large)
    """
    initialize_sidebar()

    # Streamlit set_page_config method has a 'initial_sidebar_state' argument that controls sidebar state.
    st.set_page_config(
        layout="wide",
        initial_sidebar_state=st.session_state.sidebar_state,
        page_icon=config.favicon,
    )

    return


def manage_sidebar_state():
    """
    Fonction qui permet de forcer l'affichage de la sidebar sur les pages qui la nécessitent
    """
    if "sidebar_state" not in st.session_state:
        st.session_state.sidebar_state = "collapsed"
    else:
        st.session_state.sidebar_state = "expanded"
        set_config()

    return
