from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite

# import view.ingredients.menu

from service.ingredient_service import IngredientService
from service.liste_favoris_service import ListeFavorisService

lfs = ListeFavorisService()


class MenuIngredient(VueAbstraite):
    """
    Vue qui affiche :
    - tous les ingrédients dans un premier temps
    - puis les options relatives aux ingrédients pour l'utilisateur
    """

    def __init__(self, message, utilisateur):
        super().__init__(message)
        self.utilisateur = utilisateur

    def choisir_menu(self):
        ingredient_service = IngredientService()
        ingredients = ingredient_service.lister_tous()

        choix = "-> Page suivante"
        i = 0
        ingredient_service = IngredientService()

        while choix == "-> Page suivante":
            i += 10
            liste_ingredients = ingredients[i - 10 : i]
            liste_ingredients.append("-> Page suivante")
            liste_ingredients.append("Retour")
            choix = inquirer.select(
                message="Choisissez un ingrédient : ",
                choices=liste_ingredients,
            ).execute()

        if choix == "Retour":
            from view.ingredients.ingredients_vue import IngredientsVue

            return IngredientsVue(utilisateur=self.utilisateur)

        else:
            choix_bis = inquirer.select(
                message="Que voulez-vous faire ? : ",
                choices=[
                    "Ajouter l'ingrédient aux favoris",  # done
                    "Retirer l'ingrédient des favoris",  # done
                    "Ajouter l'ingrédient aux non-désirés",  # done
                    "Retirer l'ingrédient des non-désirés",  # done
                ],
            ).execute()

            match choix_bis:
                case "Ajouter l'ingrédient aux favoris":

                    lfs.modifier_preference_ingredient(
                        ingredient=choix, utilisateur=self.utilisateur, modif="F"
                    )

                case "Retirer l'ingrédient des favoris":

                    lfs.modifier_preference_ingredient(
                        ingredient=choix, utilisateur=self.utilisateur, modif=None
                    )

                case "Ajouter l'ingredient aux non-désirés":

                    lfs.modifier_preference_ingredient(
                        ingredient=choix, utilisateur=self.utilisateur, modif="ND"
                    )

                case "Retirer l'ingredient des non-désirés":

                    lfs.modifier_preference_ingredient(
                        ingredient=choix, utilisateur=self.utilisateur, modif=None
                    )

        from view.ingredients.ingredients_vue import IngredientsVue

        message = "C'est fait !\n\n"

        return IngredientsVue(message=message, utilisateur=self.utilisateur)
