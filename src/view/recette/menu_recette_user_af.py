from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from view.users.menu_user_vue import MenuUserVue
from view.recettes.recettes_vue_user import RecettesVue

from service.ingredient_service import IngredientService
from service.recette_service import RecetteService
from service.liste_favoris_service import ListeFavorisService


class MenuRecetteAf(VueAbstraite):
    """Vue qui affiche :
    - toutes les recettes dispo selon l'ingredient choisi
    - les options
    """

    def __init__(self, message, utilisateur):
        super().__init__(message)
        self.utilisateur = utilisateur

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

                    case "Voir les notes et les avis":
                        print(recette_service.voir_note_avis(choix_deux), "\n\n")

                    case "Noter et laisser un commentaire":
                        note = inquirer.select(
                            message="Quelle note attribuez-vous à cette recette ?",
                            choices=[
                                "0/5",
                                "1/5",
                                "2/5",
                                "3/5",
                                "4/5",
                                "5/5",
                            ],
                        ).execute()
                        note = int(note[0])
                        com = inquirer.text(
                            message="Laissez un commentaire ! (pas de ';')\n"
                        ).execute()
                        recette_service.ajouter_note_et_com(recette=choix_deux, note=note, com=com)
                        choix_deux = recette_service.trouver_recette_par_id(choix_deux.id_recette)
                        print("\n\nC'est fait !!!\n\n")

                    case "Ajouter dans les favoris":
                        ListeFavorisService().ajouter_favoris(
                            recette=choix_deux, utilisateur=self.utilisateur
                        )
                        print("\n\nC'est fait !!!\n\n")

                    case "Supprimer des favoris":
                        ListeFavorisService().retirer_favoris(
                            recette=choix_deux, utilisateur=self.utilisateur
                        )
                        print("\n\nC'est fait !!!\n\n")

                    case "Ajouter les ingrédients au panier":
                        ListeFavorisService().ajouter_liste_course(
                            recette=choix_deux, utilisateur=self.utilisateur
                        )
                        print("\n\nC'est fait !!!\n\n")

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
                        return MenuUserVue(message=self.message, utilisateur=self.utilisateur)

        return RecettesVue(message=self.message, utilisateur=self.utilisateur)
