from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from src.service.utilisateur_service import UtilisateurService


class IngredientsVue(VueAbstraite):
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
                "Consulter tous les ingrédients"#done
                "Consulter les ingrédients favoris",#done
                "Consulter les ingrédients non-désirés"#done
                "Retour",#done
            ],
        ).execute()

        match choix:
            case "Consulter tous les ingrédients":
                from src.view.ingredient.menu_ingredient import MenuIngredient

                return MenuIngredient()

            case "Consulter les ingrédients favoris":
                
                return voir_ingredients_favoris()

            case "Consulter les ingrédients non-désirés":

                return voir_ingredients_non_desires()

            case "Retour":
                from src.view.users.menu_user_vue import MenuUserVue

                return MenuUserVue()