from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite


class RecettesVue(VueAbstraite):
    """Vue d'accueil de l'application"""

    def choisir_menu(self):
        """
        Vue pour la consultation de recette d'un utilisateur invité.
        """
        print("\n" + "-" * 50 + "\nConsultation des recettes\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Consulter toutes les recettes",
                "Consulter les recettes par ingrédient",
                "Retour",
            ],
        ).execute()

        match choix:
            case "Consulter toutes les recettes":
                from view.recette.menu_recette_inv_sf import MenuRecetteSf

                return MenuRecetteSf()

            case "Consulter les recettes par ingrédient":
                from view.recette.menu_recette_inv_af import MenuRecetteAf

                return MenuRecetteAf()

            case "Retour":
                from view.users.menu_inv_vue import MenuInvVue

                return MenuInvVue()
