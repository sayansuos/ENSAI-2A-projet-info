from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from service.ingredient_service import IngredientService
from service.recette_service import RecetteService
from service.liste_favoris_service import ListeFavorisService
lfs = ListeFavorisService()


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
            from view.recettes.recettes_vue_user import RecettesVue

            return RecettesVue()
        else:
            choix_bis = inquirer.select(
                message="Que voulez-vous faire ?",
                choices=[
                    "Lire la recette",
                    "Voir les notes et les avis",
                    "Noter et laisser un commentaire",
                    "Ajouter dans les favoris",
                    "Supprimer des favoris",
                    "Ajouter les ingrédients au panier",
                ],
            ).execute()

            match choix_bis:
                case "Lire la recette":

                    return recette_service.voir_recette(choix_deux)
                
                case "Voir les notes et les avis":

                    return recette_service.voir_note_avis(choix_deux)
                
                case "Noter et laisser un commentaire":

                    pass

                case "Ajouter dans les favoris":

                    return lfs.ajouter_favoris(choix_deux)
                
                case "Supprimer des favoris":

                    return lfs.supprimer_favoris(choix_deux)
                
                case "Ajouter les ingredients au panier":
                    ingr = recette_service.ingredients_recette(choix_deux)

                    return lfs.ajouter_liste_course(ingr)
        return MenuRecetteAf()
