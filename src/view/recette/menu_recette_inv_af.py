from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from view.users.menu_inv_vue import MenuInvVue
from service.ingredient_service import IngredientService
from service.recette_service import RecetteService
from view.recettes.recettes_vue_inv import RecettesVue


class MenuRecetteAf(VueAbstraite):
    """
    Vue pour la consultation de toutes les recettes par ingrédient d'un utilisateur non connecté.
    """

    def choisir_menu(self):
        print(
            "\n"
            + "-" * 50
            + "\nConsultation de toutes les recettes par ingrédient\n"
            + "-" * 50
            + "\n"
        )

        # Affichage de tous les ingrédients
        ingredients = IngredientService().lister_tous()
        choix = "-> Page suivante"
        i = 0
        while choix == "-> Page suivante":  # Pour avoir plusieurs pages avec 10 ingrédients
            i += 1
            if abs(10 * (i - 1) - len(ingredients)) > 10:
                liste_ingredients = ingredients[10 * (i - 1) : 10 * i]
            else:
                liste_ingredients = ingredients[10 * (i - 1) :]
                i = 0
            liste_ingredients.append("-> Page suivante")
            # Choix de l'ingrédient
            choix = inquirer.select(
                message="Choisissez un ingrédient : ",
                choices=liste_ingredients,
            ).execute()

        # Affichage des recettes avec l'ingrédient sélectionné
        liste_recette_filtree = RecetteService().trouver_recette_par_ingredient(choix)
        liste_recette_filtree.append("Retour")

        # Choix de la recette
        choix_deux = inquirer.select(
            message="Choisissez une recette : ",
            choices=liste_recette_filtree,
        ).execute()

        if choix_deux == "Retour":
            return RecettesVue()

        else:
            autre_action = "Oui"
            while autre_action == "Oui":  # Pour réaliser plusieurs action à la suite
                choix_bis = inquirer.select(
                    message="Que voulez-vous faire ?",
                    choices=[
                        "Lire la recette",
                        "Voir les notes et les avis",
                    ],
                ).execute()

                match choix_bis:
                    case "Lire la recette":
                        # Appel au service pour afficher la recette
                        RecetteService().lire_recette(choix_deux)

                        # Fin (ou non) de la boucle pour réaliser une autre action
                        autre_action = inquirer.select(
                            message="Réaliser une autre action pour cette recette ?",
                            choices=["Oui", "Non"],
                        ).execute()

                        # Fin (ou non) de la boucle pour consulter une autre recette
                        if autre_action == "Non":
                            choix_bis_bis = inquirer.select(
                                message="Consulter une autre recette ? ",
                                choices=["Oui", "Non"],
                            ).execute()
                            if choix_bis_bis == "Non":
                                return MenuInvVue()

                    case "Voir les notes et les avis":
                        # Appel au service pour afficher la note et les avis de la recette
                        RecetteService().voir_note_avis(choix_deux)

                        # Fin (ou non) de la boucle pour réaliser une autre action
                        autre_action = inquirer.select(
                            message="Réaliser une autre action pour cette recette ?",
                            choices=["Oui", "Non"],
                        ).execute()

                        # Fin (ou non) de la boucle pour consulter une autre recette
                        if autre_action == "Non":
                            choix_bis_bis = inquirer.select(
                                message="Consulter une autre recette ? ",
                                choices=["Oui", "Non"],
                            ).execute()
                            if choix_bis_bis == "Non":
                                return MenuInvVue()

        return RecettesVue()
