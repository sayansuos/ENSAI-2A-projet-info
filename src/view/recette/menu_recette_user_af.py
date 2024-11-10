from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from view.users.menu_user_vue import MenuUserVue
from view.recettes.recettes_vue_user import RecettesVue

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
            autre_action = "Oui"
            while autre_action == "Oui":

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
                        print(recette_service.lire_recette(choix_deux), "\n\n")
                        autre_action = inquirer.select(
                            message="Réaliser une autre action pour cette recette ?",
                            choices=["Oui", "Non"],
                        ).execute()
                        if autre_action == "Non":
                            choix_bis_bis = inquirer.select(
                                message="Consulter une autre recette ? ",
                                choices=["Oui", "Non"],
                            ).execute()
                            if choix_bis_bis == "Non":
                                return MenuUserVue()

                    case "Voir les notes et les avis":
                        print(recette_service.voir_note_avis(choix_deux), "\n\n")
                        autre_action = inquirer.select(
                            message="Réaliser une autre action pour cette recette ?",
                            choices=["Oui", "Non"],
                        ).execute()
                        if autre_action == "Non":
                            choix_bis_bis = inquirer.select(
                                message="Consulter une autre recette ? ",
                                choices=["Oui", "Non"],
                            ).execute()
                            if choix_bis_bis == "Non":
                                return MenuUserVue()

                    case "Noter et laisser un commentaire":
                        pass

                    case "Ajouter dans les favoris":
                        return lfs.ajouter_favoris(choix_deux)

                    case "Supprimer des favoris":
                        return lfs.supprimer_favoris(choix_deux)

                    case "Ajouter les ingredients au panier":
                        ingr = recette_service.ingredients_recette(choix_deux)

                        return lfs.ajouter_liste_course(ingr)

        return RecettesVue()
