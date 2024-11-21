from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite


class MenuInvVue(VueAbstraite):
    """
    Vue du menu de l'invité
    """

    def choisir_menu(self):
        """
        Vue de l'utilisateur non connecté.
        """
        print("\n" + "-" * 50 + "\nMenu Invité\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Consulter les recettes",
                "Retour",
            ],
        ).execute()

        match choix:
            case "Retour":
                from view.accueil.accueil_vue import AccueilVue

                return AccueilVue()

            case "Consulter les recettes":
                from view.recette.menu_recette_inv_vue import MenuRecetteInvVue

                return MenuRecetteInvVue()
