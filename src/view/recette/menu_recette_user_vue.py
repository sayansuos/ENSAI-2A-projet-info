from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite


class MenuRecetteUserVue(VueAbstraite):
    """
    Vue pour la consultation des recettes d'un utilisateur connecté.
    """

    def __init__(self, message, utilisateur):
        super().__init__(message)
        self.utilisateur = utilisateur

    def choisir_menu(self):
        print("\n" + "-" * 50 + "\nConsultation des recettes\n" + "-" * 50 + "\n")

        # Choix du filtre pour la consultation de recettes
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
                from view.recette.recette_user_sf_vue import RecetteUserSfVue

                return RecetteUserSfVue(message=self.message, utilisateur=self.utilisateur)

            case "Consulter les recettes par ingrédient":
                from view.recette.recette_user_af_vue import RecetteUserAfVue

                return RecetteUserAfVue(message=self.message, utilisateur=self.utilisateur)

            case "Retour":
                from view.users.menu_user_vue import MenuUserVue

                return MenuUserVue(message=self.message, utilisateur=self.utilisateur)
