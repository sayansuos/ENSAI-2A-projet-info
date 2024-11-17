from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite

from service.ingredient_service import IngredientService
from service.liste_favoris_service import ListeFavorisService


class MenuIngredient(VueAbstraite):
    """
    Vue qui affiche tous les ingrédients pour un utilisateur connecté.
    """

    def __init__(self, message, utilisateur):
        super().__init__(message)
        self.utilisateur = utilisateur

    def choisir_menu(self):
        print("\n" + "-" * 50 + "\nListe de tous les ingrédients\n" + "-" * 50 + "\n")

        # Affichage de tous les ingrédients
        ingredients = IngredientService().lister_tous()
        choix = "-> Page suivante"
        i = 0
        while choix == "-> Page suivante":  # Pour avoir plusieurs pages avec 10 ingrédients
            i += 1
            if abs(10 * i - len(ingredients)) > 10:
                liste_ingredients = ingredients[10 * (i - 1) : 10 * i]
            else:
                liste_ingredients = ingredients[10 * (i - 1) :]
                i = 0
            liste_ingredients.append("-> Page suivante")
            liste_ingredients.append("Retour")

            # Choix de l'ingrédient
            choix = inquirer.select(
                message="Choisissez un ingrédient : ",
                choices=liste_ingredients,
            ).execute()

        if choix == "Retour":
            from view.ingredients.ingredients_vue import IngredientsVue

            return IngredientsVue(utilisateur=self.utilisateur)

        else:
            # Choix de l'action à réaliser
            choix_bis = inquirer.select(
                message="Que voulez-vous faire ? : ",
                choices=[
                    "Ajouter l'ingrédient aux favoris",
                    "Retirer l'ingrédient des favoris",
                    "Ajouter l'ingrédient aux non-désirés",
                    "Retirer l'ingrédient des non-désirés",
                ],
            ).execute()

            match choix_bis:
                case "Ajouter l'ingrédient aux favoris":
                    # Appel au service pour ajouter un ingrédient aux favoris
                    ListeFavorisService().modifier_preference_ingredient(
                        ingredient=choix, utilisateur=self.utilisateur, modif="F"
                    )
                    print("\n\nL'ingrédient a bien été ajouté aux favoris !\n\n")

                case "Retirer l'ingrédient des favoris":
                    # Appel au service pour retirer un ingrédient des préférences
                    ListeFavorisService().modifier_preference_ingredient(
                        ingredient=choix, utilisateur=self.utilisateur, modif=None
                    )
                    print("\n\nL'ingrédient a bien été retiré des favoris !\n\n")

                case "Ajouter l'ingrédient aux non-désirés":
                    # Appel au service pour ajouter un ingrédient aux non-désirés
                    ListeFavorisService().modifier_preference_ingredient(
                        ingredient=choix, utilisateur=self.utilisateur, modif="ND"
                    )
                    print("\n\nL'ingrédient a bien été ajouté aux non-désirés !\n\n")

                case "Retirer l'ingrédient des non-désirés":
                    # Appel au service pour retirer un ingrédient des préférences
                    ListeFavorisService().modifier_preference_ingredient(
                        ingredient=choix, utilisateur=self.utilisateur, modif=None
                    )
                    print("\n\nL'ingrédient a bien été retiré des non-désirés !\n\n")

        from view.ingredients.ingredients_vue import IngredientsVue

        return IngredientsVue(message=self.message, utilisateur=self.utilisateur)
