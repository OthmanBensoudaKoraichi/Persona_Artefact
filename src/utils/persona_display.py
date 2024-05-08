import streamlit as st
import src.utils.config as config

def display_persona_in_sidebar(persona : str):

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
                border-radius: 20%;  /* Adjust for desired roundness */
                box-shadow:
                    0 0 10px rgba(150, 150, 150, 0.6),  /* Light grey, smaller spread */
                    0 0 10px rgba(120, 120, 120, 0.5),  /* Medium grey, medium spread */
                    0 0 20px rgba(90, 90, 90, 0.4);     /* Darker grey, larger spread */
            }}
            </style>
            <img src="{persona_image_url}">
            """,
            unsafe_allow_html=True
        )

        # Inject custom CSS for font size, vertical scrolling, and text wrap
        st.markdown(
            """
            <style>
            .big-font {
                font-size: 30px; /* Adjust size as needed */
                overflow-y: auto; /* Enables vertical scrolling */
                word-wrap: break-word; /* Ensures words do not extend outside the container */
                white-space: normal; /* Overrides any other whitespace settings that might prevent wrapping */
                text-align: center;
            }
            .regular-sidebar-font {
                font-size: 20px; /* Smaller font size for regular content */
                overflow-y: auto;
                word-wrap: break-word;
                white-space: normal;
                text-align: justify;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        header_content = """
        <div class="big-font">
            <strong>Sophia, 48 ans</strong><br>
            <strong>Expatriée de Retour</strong><br>
            <strong>Consultant en gestion</strong><br><br>
        </div>
        """
        # Display the header content within a markdown element, enabling HTML
        st.markdown(header_content, unsafe_allow_html=True)

        body_content = config.persona_descriptions[persona]
        # Appliquer la classe au conteneur parent
        st.markdown(f"<div class='regular-sidebar-font'>{body_content}</div>", unsafe_allow_html=True)

    return

