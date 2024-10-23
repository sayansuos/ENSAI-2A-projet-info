from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite


class RecettesVue(VueAbstraite):
    """Vue d'accueil de l'application"""

    def choisir_menu(self):
        """Choix du menu suivant

        Return
        ------
        view
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "-" * 50 + "\nAccueil\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Consulter toutes les recettes"
                "Consulter les recettes par ingrédient",
                "Retour",
            ],
        ).execute()

        match choix:
            case "Consulter toutes les recettes":
                from src.view.recette.menu_recette_user_sf import MenuRecetteSf

                return MenuRecetteSf()

            case "Consulter les recettes par ingrédient":
                from src.view.recette.menu_recette_user_af import MenuRecetteAf

                return MenuRecetteAf()
            
            case "Retour":
                from src.view.users.menu_user_vue import MenuUserVue

                return MenuUserVue()