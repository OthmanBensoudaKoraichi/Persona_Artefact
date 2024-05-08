from src.utils import style,config
import streamlit as st
from st_clickable_images import clickable_images
from streamlit_extras.switch_page_button import switch_page

def main():
    # Set style
    st.set_page_config(layout="wide")
    style.set_bg_image(config.background)


    clicked = clickable_images(
        [
            config.explorator,
            config.generator,
        ],
        div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
        img_style={
            "margin": "50px",
            "height": "400px",
            "transition": "transform 0.2s, box-shadow 0.2s",
            "cursor": "pointer",
        },
    )

    st.markdown(f"Image #{clicked} clicked" if clicked > -1 else "No image clicked")

    if clicked == 0:
        switch_page("détails des personae")

    if clicked == 1:
        switch_page("générateur de créas")


    style.create_interface()



if __name__ == "__main__":
    main()