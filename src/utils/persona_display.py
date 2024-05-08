import streamlit as st
from src.utils import config
def display_persona_in_sidebar(persona: str):
    # Get image url that will be displayed in the sidebar
    persona_image_url = config.persona_images[persona]

    with st.sidebar:
        # Inject custom CSS for glowing border effect using Markdown with unsafe_allow_html
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
            unsafe_allow_html=True
        )

        # Dynamic header content based on persona
        header_content = f"""
        <div class="big-font content-box">
            <strong>{config.persona_info[persona]}</strong>
        </div>
        """

        # Display the header content within a markdown element, enabling HTML
        st.markdown(header_content, unsafe_allow_html=True)

        body_content = config.persona_descriptions[persona]
        # Apply the class to the parent container
        st.markdown(f"<div class='regular-sidebar-font content-box'>{body_content}</div>", unsafe_allow_html=True)

    return