from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from service.liste_favoris_service import ListeFavorisService


class IngredientsVue(VueAbstraite):
    """
    Vue pour les préférences ingrédients d'un utilisateur connecté.
    """

    def __init__(self, message, utilisateur):
        super().__init__(message)
        self.utilisateur = utilisateur

    def choisir_menu(self):
        print("\n" + "-" * 50 + "\nConsultation des préférences ingrédients\n" + "-" * 50 + "\n")

        # Choix des actions à réaliser
        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Consulter tous les ingrédients",
                "Consulter les ingrédients favoris",
                "Consulter les ingrédients non-désirés",
                "Retour",
            ],
        ).execute()

        match choix:
            case "Consulter tous les ingrédients":
                from view.ingredient.menu_ingredient import MenuIngredient

                return MenuIngredient(message=self.message, utilisateur=self.utilisateur)

            case "Consulter les ingrédients favoris":
                ListeFavorisService().consulter_preference_ingredient_favori(
                    utilisateur=self.utilisateur
                )
                return IngredientsVue(message=self.message, utilisateur=self.utilisateur)

            case "Consulter les ingrédients non-désirés":
                ListeFavorisService().consulter_preference_ingredient_non_desire(
                    utilisateur=self.utilisateur
                )
                return IngredientsVue(message=self.message, utilisateur=self.utilisateur)

            case "Retour":
                from view.users.menu_user_vue import MenuUserVue

                return MenuUserVue(message=self.message, utilisateur=self.utilisateur)
