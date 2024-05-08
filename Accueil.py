from src.utils import style,config, landing_page
import streamlit as st
from st_clickable_images import clickable_images
from streamlit_extras.switch_page_button import switch_page

def main():
    # Set style
    st.set_page_config(layout="wide",initial_sidebar_state="collapsed",page_icon = config.favicon)

    style.set_bg_image(config.background)
    style.display_logo(config.logo_boa)

    landing_page.display_landing_page()

if __name__ == "__main__":
    main()