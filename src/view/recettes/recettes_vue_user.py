from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite


class RecettesVue(VueAbstraite):
    """Vue d'accueil de l'application"""

    def __init__(self, message, utilisateur):
        super().__init__(message)
        self.utilisateur = utilisateur

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
                "Consulter toutes les recettes",
                "Consulter les recettes par ingrédient",
                "Retour",
            ],
        ).execute()

        match choix:
            case "Consulter toutes les recettes":
                from view.recette.menu_recette_user_sf import MenuRecetteSf

                return MenuRecetteSf(message=self.message, utilisateur=self.utilisateur)

            case "Consulter les recettes par ingrédient":
                from view.recette.menu_recette_user_af import MenuRecetteAf

                return MenuRecetteAf(message=self.message, utilisateur=self.utilisateur)

            case "Retour":
                from view.users.menu_user_vue import MenuUserVue

                return MenuUserVue(message=self.message, utilisateur=self.utilisateur)
