from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from service.liste_favoris_service import ListeFavorisService


class IngredientsVue(VueAbstraite):
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
                "Consulter tous les ingrédients",  # done
                "Consulter les ingrédients favoris",  # done
                "Consulter les ingrédients non-désirés",  # done
                "Retour",  # done
            ],
        ).execute()

        match choix:
            case "Consulter tous les ingrédients":
                from view.ingredient.menu_ingredient import MenuIngredient

                return MenuIngredient(message=self.message, utilisateur=self.utilisateur)

            case "Consulter les ingrédients favoris":
                print(
                    ListeFavorisService().consulter_preference_ingredient_favori(
                        utilisateur=self.utilisateur
                    )
                )
                return IngredientsVue(message=self.message, utilisateur=self.utilisateur)

            case "Consulter les ingrédients non-désirés":
                print(
                    ListeFavorisService().consulter_preference_ingredient_non_desire(
                        utilisateur=self.utilisateur
                    )
                )
                return IngredientsVue(message=self.message, utilisateur=self.utilisateur)

            case "Retour":
                from view.users.menu_user_vue import MenuUserVue

                return MenuUserVue(message=self.message, utilisateur=self.utilisateur)
