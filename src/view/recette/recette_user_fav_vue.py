from InquirerPy import inquirer

from view.session import Session
from view.vue_abstraite import VueAbstraite
from view.users.menu_user_vue import MenuUserVue

from service.recette_service import RecetteService
from service.liste_favoris_service import ListeFavorisService


class RecetteUserFavVue(VueAbstraite):
    """
    Vue qui affiche les recettes favorites d'un utilisateur connecté et les actions associées.
    """

    def __init__(self, message, utilisateur):
        super().__init__(message)
        self.utilisateur = utilisateur

    def choisir_menu(self):
        print("\n" + "-" * 50 + "\nConsultation des recettes favorites\n" + "-" * 50 + "\n")

        # Affichage de toutes les recettes favorites
        recettes = ListeFavorisService().consulter_favoris(utilisateur=self.utilisateur)

        # Si la liste des suggestions est vide :
        if recettes == []:
            print("\n\nThere is no favourite recipe registered...")
            print("Maybe you should try to add some!\n\n")
            inquirer.select(message="", choices=["Ok"]).execute()
            return MenuUserVue(message=self.message, utilisateur=self.utilisateur)

        # Sinon
        else:
            choix = "-> Page suivante"
            i = 0
            while choix == "-> Page suivante":  # Pour avoir plusieurs pages avec 10 recettes
                i += 1
                if abs(10 * (i - 1) - len(recettes)) > 10:
                    liste_recettes = recettes[10 * (i - 1) : 10 * i]
                else:
                    liste_recettes = recettes[10 * (i - 1) :]
                    i = 0
                liste_recettes.append("-> Page suivante")
                liste_recettes.append("Retour")
                # Choix de la recette
                choix = inquirer.select(
                    message="Choisissez une recette : ",
                    choices=liste_recettes,
                ).execute()

            # Pour pouvoir revenir au début de la liste s'il souhaite consulter une autre recette après
            i = 0

            if choix == "Retour":
                return MenuUserVue(message=self.message, utilisateur=self.utilisateur)

            else:
                # Pour pouvoir modifier la liste chargée dans Session ensuite
                for recette_raw in Session().liste_recettes:
                    if recette_raw.id_recette == choix.id_recette:
                        choix = recette_raw

                autre_action = "Oui"
                while autre_action == "Oui":  # Pour réaliser plusieurs actions à la suite
                    # Sélection de l'action
                    choix_bis = inquirer.select(
                        message="Que voulez-vous faire ?",
                        choices=[
                            "Lire la recette",
                            "Voir les notes et les avis",
                            "Noter et laisser un commentaire",
                            "Supprimer des favoris",
                            "Ajouter les ingrédients au panier",
                        ],
                    ).execute()

                    match choix_bis:
                        case "Lire la recette":
                            # Appel au service pour lire une recette
                            RecetteService().lire_recette(choix)

                        case "Voir les notes et les avis":
                            # Appel au service pour lire les notes et avis
                            RecetteService().voir_note_avis(choix)

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
                            RecetteService().ajouter_note_et_com(recette=choix, note=note, com=com)
                            # Suppression dans la liste chargée et ajout de la recette avec avis et com
                            Session().liste_recettes.remove(choix)
                            choix = RecetteService().trouver_recette_par_id(choix.id_recette)
                            Session().liste_recettes.append(choix)
                            print("\n\nLa note et le commentaire ont bien été pris en compte !")

                        case "Supprimer des favoris":
                            # Appel au service pour retirer la recette des favoris
                            ListeFavorisService().retirer_favoris(
                                recette=choix, utilisateur=self.utilisateur
                            )
                            print("\n\nLa recette a bien été retirée des favoris !\n\n")

                        case "Ajouter les ingredients au panier":
                            # Appel au service pour ajouter les ingrédients au panier
                            ListeFavorisService().ajouter_liste_course(
                                recette=choix, utilisateur=self.utilisateur
                            )
                            print("\n\nLes ingrédients ont bien été ajoutés au panier !\n\n")

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

        return RecetteUserFavVue(message=self.message, utilisateur=self.utilisateur)
