from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from view.users.menu_inv_vue import MenuInvVue
from service.ingredient_service import IngredientService
from service.recette_service import RecetteService
from view.recettes.recettes_vue_inv import RecettesVue


class MenuRecetteAf(VueAbstraite):
    """Vue qui affiche :
    - toutes les recettes dispo selon l'ingredient choisi
    - les options
    """

    def choisir_menu(self):
        recette_service = RecetteService()
        ingredient_service = IngredientService()
        ingredients = ingredient_service.lister_tous()

        choix = "-> Page suivante"
        i = 0

        while choix == "-> Page suivante":
            i += 10
            liste_ingredients = ingredients[i - 10 : i]
            liste_ingredients.append("-> Page suivante")
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
                    print(recette_service.lire_recette(choix_deux), "\n\n")
                    choix_bis_bis = inquirer.select(
                        message="Consulter une autre recette ? ",
                        choices=["Oui", "Non"],
                    ).execute()
                    if choix_bis_bis == "Non":
                        return MenuInvVue()

                case "Voir les notes et les avis":
                    print(recette_service.voir_note_avis(choix_deux), "\n\n")
                    choix_bis_bis = inquirer.select(
                        message="Consulter une autre recette ? ",
                        choices=["Oui", "Non"],
                    ).execute()
                    if choix_bis_bis == "Non":
                        return MenuInvVue()

        return RecettesVue()
