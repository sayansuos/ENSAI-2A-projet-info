from InquirerPy import inquirer

from view.session import Session
from view.vue_abstraite import VueAbstraite
from view.users.menu_user_vue import MenuUserVue
from view.recette.menu_recette_user_vue import MenuRecetteUserVue

from service.ingredient_service import IngredientService
from service.recette_service import RecetteService
from service.liste_favoris_service import ListeFavorisService


class RecetteUserAfVue(VueAbstraite):
    """
    Vue qui affiche toutes les recettes par ingrédient sélectionné pour l'utilisateur connecté et
    les actions associées.
    """

    def __init__(self, message, utilisateur):
        super().__init__(message)
        self.utilisateur = utilisateur

    def choisir_menu(self):
        print("\n" + "-" * 50 + "\nConsultation des recettes par ingrédients\n" + "-" * 50 + "\n")

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

        # Pour pouvoir revenir au début de la liste s'il souhaite consulter une autre recette après
        i = 0

        # Affichage de toutes les recettes avec l'ingrédient sélectionné
        liste_recette_filtree = RecetteService().trouver_recette_par_ingredient(choix)
        liste_recette_filtree.append("Retour")

        # Choix de la recette
        choix_deux = inquirer.select(
            message="Choisissez une recette : ",
            choices=liste_recette_filtree,
        ).execute()

        if choix_deux == "Retour":
            return MenuRecetteUserVue()

        else:

            # Pour pouvoir modifier la liste chargée dans Session ensuite
            for recette_raw in Session().liste_recettes:
                if recette_raw.id_recette == choix_deux.id_recette:
                    choix_deux = recette_raw

            autre_action = "Oui"
            while autre_action == "Oui":  # Pour réaliser plusieurs actions à la suite
                # Sélection de l'action
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
                        # Appel au service pour lire une recette
                        RecetteService().lire_recette(choix_deux)

                    case "Voir les notes et les avis":
                        # Appel au service pour lire les notes et avis
                        RecetteService().voir_note_avis(choix_deux)

                    case "Noter et laisser un commentaire":
                        # Note à attribuer
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
                        # Commentaire à attribuer
                        com = inquirer.text(
                            message="Laissez un commentaire ! (pas de ';')\n"
                        ).execute()
                        # Appel au service pour pour ajouter une note et un avis
                        RecetteService().ajouter_note_et_com(recette=choix_deux, note=note, com=com)
                        # Suppression dans la liste chargée et ajout de la recette avec avis et com
                        Session().liste_recettes.remove(choix_deux)
                        choix_deux = RecetteService().trouver_recette_par_id(choix_deux.id_recette)
                        Session().liste_recettes.append(choix_deux)
                        print("\n\nLa note et le commentaire ont bien été pris en compte !")

                    case "Ajouter dans les favoris":
                        # Appel au service pour ajouter la recette aux favoris
                        ListeFavorisService().ajouter_favoris(
                            recette=choix_deux, utilisateur=self.utilisateur
                        )
                        print("\n\nLa recette a bien été ajoutée aux favoris !\n\n")

                    case "Supprimer des favoris":
                        # Appel au service pour retirer la recette des favoris
                        ListeFavorisService().retirer_favoris(
                            recette=choix_deux, utilisateur=self.utilisateur
                        )
                        print("\n\nLa recette a bien été retirée des favoris !\n\n")

                    case "Ajouter les ingrédients au panier":
                        # Appel au service pour ajouter les ingrédients au panier
                        ListeFavorisService().ajouter_liste_course(
                            recette=choix_deux, utilisateur=self.utilisateur
                        )
                        print("\n\nLes ingrédients ont bien été ajoutés au panier !.\n\n")

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
                        return MenuUserVue(message=self.message, utilisateur=self.utilisateur)

        return MenuRecetteUserVue(message=self.message, utilisateur=self.utilisateur)
