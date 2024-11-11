from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from view.users.menu_user_vue import MenuUserVue

from service.utilisateur_service import UtilisateurService
from service.ingredient_service import IngredientService
from service.liste_favoris_service import ListeFavorisService
from service.recette_service import RecetteService


class PanierVue(VueAbstraite):
    """Vue qui affiche :
    - le panier de l'utilisateur
    - les options
    """

    def __init__(self, message, utilisateur):
        super().__init__(message)
        self.utilisateur = utilisateur

    def choisir_menu(self):
        ingredients = ListeFavorisService().consulter_liste_course(utilisateur=self.utilisateur)

        if len(ingredients) < 1:
            print("Il n'y a aucun ingrédient dans la liste de courses.")

        else:
            choix = "-> Page suivante"
            i = 0

            while choix == "-> Page suivante":
                i += 1
                if abs(10 * (i - 1) - len(ingredients)) > 10:
                    liste_ingredients_raw = ingredients[10 * (i - 1) : 10 * i]
                else:
                    liste_ingredients_raw = ingredients[10 * (i - 1) :]
                    i = 0

                liste_ingredients = []
                for ing in liste_ingredients_raw:
                    liste_ingredients.append([ing[0].nom_ingredient, f"({ing[1].nom_recette})"])
                liste_ingredients.append("-> Page suivante")
                liste_ingredients.append("Retour")
                choix = inquirer.select(
                    message="Choisissez un ingrédient : ",
                    choices=liste_ingredients,
                ).execute()

            if choix == "Retour":
                return MenuUserVue(message=self.message, utilisateur=self.utilisateur)

            else:
                recette = RecetteService().trouver_recette_par_nom(choix[1][1:-1])
                choix = IngredientService().trouver_par_nom(choix[0])
                choix_bis = inquirer.select(
                    message="Retirer l'ingrédient du panier ? ",
                    choices=[
                        "Oui",
                        "Annuler",
                    ],
                ).execute()

                match choix_bis:

                    case "Annuler":
                        return PanierVue(message=self.message, utilisateur=self.utilisateur)

                    case "Oui":
                        ListeFavorisService().retirer_liste_course(
                            recette=recette, ingredient=choix, utilisateur=self.utilisateur
                        )
                        print("\n\nC'est fait !\n\n")
                        choix_bis_bis = inquirer.select(
                            message="Voir d'autres ingrédients du panier ?", choices=["Oui", "Non"]
                        ).execute()
                        if choix_bis_bis == "Oui":
                            return PanierVue(message=self.message, utilisateur=self.utilisateur)

        return MenuUserVue(message=self.message, utilisateur=self.utilisateur)
