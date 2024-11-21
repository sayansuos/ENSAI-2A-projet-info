from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from view.users.menu_user_vue import MenuUserVue

from service.ingredient_service import IngredientService
from service.liste_favoris_service import ListeFavorisService
from service.recette_service import RecetteService


class ListeIngredientVue(VueAbstraite):
    """
    Vue pour le panier d'un utilisateur connecté.
    """

    def __init__(self, message, utilisateur):
        super().__init__(message)
        self.utilisateur = utilisateur

    def choisir_menu(self):
        print("\n" + "-" * 50 + "\nConsultation des ingrédients du panier\n" + "-" * 50 + "\n")

        # Affichage des ingrédients de la liste de course
        ingredients = ListeFavorisService().consulter_liste_course(utilisateur=self.utilisateur)

        if len(ingredients) < 1:  # Si pas d'ingrédient
            print("The grocery list is empty.")

        else:
            choix = "-> Page suivante"
            i = 0
            while choix == "-> Page suivante":  # Pour avoir plusieurs pages avec 10 ingrédients
                i += 1
                if abs(10 * (i - 1) - len(ingredients)) > 10:
                    liste_ingredients_raw = ingredients[10 * (i - 1) : 10 * i]
                else:
                    liste_ingredients_raw = ingredients[10 * (i - 1) :]
                    i = 0

                # Liste avec le nom de l'ingrédient et la recette associée
                liste_ingredients = []
                for ing in liste_ingredients_raw:
                    liste_ingredients.append([ing[0].nom_ingredient, f"({ing[1].nom_recette})"])
                liste_ingredients.append("-> Page suivante")
                liste_ingredients.append("Retour")

                # Choix de l'ingrédient
                choix = inquirer.select(
                    message="Choisissez un ingrédient : ",
                    choices=liste_ingredients,
                ).execute()

            if choix == "Retour":
                return MenuUserVue(message=self.message, utilisateur=self.utilisateur)

            else:
                # Création de l'ingrédient et de la recette à partir de leur nom
                recette = RecetteService().trouver_recette_par_nom(choix[1][1:-1])
                choix = IngredientService().trouver_par_nom(choix[0])

                # Retirer ou non l'ingrédient
                choix_bis = inquirer.select(
                    message="Retirer l'ingrédient du panier ? ",
                    choices=[
                        "Oui",
                        "Annuler",
                    ],
                ).execute()

                match choix_bis:

                    case "Annuler":
                        return ListeIngredientVue(
                            message=self.message, utilisateur=self.utilisateur
                        )

                    case "Oui":
                        ListeFavorisService().retirer_liste_course(
                            recette=recette, ingredient=choix, utilisateur=self.utilisateur
                        )
                        print("\n\nL'ingrédient a bien été retiré du panier !\n\n")

                        # Fin (ou non) de la boucle pour voir un autre ingrédient
                        choix_bis_bis = inquirer.select(
                            message="Voir d'autres ingrédients du panier ?", choices=["Oui", "Non"]
                        ).execute()
                        if choix_bis_bis == "Oui":
                            return ListeIngredientVue(
                                message=self.message, utilisateur=self.utilisateur
                            )

        return MenuUserVue(message=self.message, utilisateur=self.utilisateur)
