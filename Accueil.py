from src.utils import style, config, landing_page, session_state


def main():
    # On configure le style de la page
    session_state.set_config()

    # On ajoute l'image de fond
    style.set_background_image(image_path=config.background, opacity=0)

    # On ajoute le logo de BOA en haut à gauche
    style.display_logo(config.logo_boa)

    # Fonction qui affiche la page d'accueil (landing_page.py)
    landing_page.display_landing_page(config.explorator, config.generator)

    return


if __name__ == "__main__":
    main()
