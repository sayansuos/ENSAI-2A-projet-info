from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from src.service.ingredient_service import IngredientService
from src.service.recette_service import RecetteService


class MenuRecetteAf(VueAbstraite):
    """Vue qui affiche :
    - toutes les recettes dispo selon l'ingredient choisi
    - les options
    """

    def choisir_menu(self):
        recette_service = RecetteService()
        ingredient_service = IngredientService

        liste_ingredients = ingredient_service.lister_tous()
        choix = inquirer.select(
            message="Choisissez un ingrédient : ",
            choices=liste_ingredients,
        ).execute()

        liste_recette_filtree = recette_service.trouver_recette_par_ingredient(choix)
        liste_recette_filtree.append("Retour")

        choix_deux = inquirer.select(
            message="Choisissez une recette : ",
            choices=liste_recette_filtree,
        ).execute()

        if choix_deux == "Retour":
            from src.view.recettes.recettes_vue_inv import RecettesVue

            return RecettesVue()
        else:
            choix_bis = inquirer.select(
                message="Que voulez-vous faire ?",
                choices=[
                    "Lire la recette",
                    "Voir les notes et les avis",
                ],
            ).execute()

            match choix_bis:
                case "Lire la recette":

                    return recette_service.voir_description(choix_deux)
                
                case "Voir les notes et les avis":

                    return recette_service.voir_note(choix_deux), recette_service.voir_avis(choix_deux)

        return MenuRecetteAf()
