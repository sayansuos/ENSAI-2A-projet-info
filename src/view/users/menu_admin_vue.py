from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from view.session import Session

from business_object.recette import Recette

from service.utilisateur_service import UtilisateurService
from service.recette_service import RecetteService
from service.ingredient_service import IngredientService


class MenuAdminVue(VueAbstraite):
    """Vue du menu de l'administrateur

    Attributes
    ----------
    message=''
        str

    Returns
    ------
    view
        retourne la prochaine vue, celle qui est choisie par l'administrateur
    """

    def __init__(self, message, utilisateur):
        super().__init__(message)
        self.utilisateur = utilisateur

    def choisir_menu(self):
        """Choix du menu suivant de l'administrateur

        Return
        ------
        vue
            Retourne la vue choisie par l'administrateur dans le terminal
        """

        print("\n" + "-" * 50 + "\nMenu Administrateur\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Consulter les comptes",
                "Consulter les recettes",
                "Supprimer un compte",
                "Modifier un compte",
                "Ajouter une recette",
                "Supprimer une recette",
                "Se déconnecter",
            ],
        ).execute()

        match choix:

            case "Se déconnecter":
                Session().deconnexion()
                from view.accueil.accueil_vue import AccueilVue

                return AccueilVue()

            case "Consulter les comptes":
                print("\n" + "-" * 50 + "\nConsultation des comptes\n" + "-" * 50 + "\n")

                # Affichage de la liste des utilisateurs
                liste_utilisateurs = UtilisateurService().lister_tous()
                autre_utilisateur = "Oui"  # Pour consulter plusieurs utilisateurs à la suite
                while autre_utilisateur == "Oui":
                    utilisateur = inquirer.select(
                        message="Quel utilisateur souhaitez-vous consulter ?",
                        choices=liste_utilisateurs,
                    ).execute()

                    # Affichage des informations de l'utilisateur
                    utilisateur.afficher_info()

                    # Fin (ou non) de la boucle
                    autre_utilisateur = inquirer.select(
                        message="Souhaitez-vous consulter un autre utilisateur ?",
                        choices=["Oui", "Non"],
                    ).execute()

            case "Supprimer un compte":
                print("\n" + "-" * 50 + "\nSuppression d'un compte\n" + "-" * 50 + "\n")

                # Affichage de la liste des utilisateurs
                liste_utilisateurs = UtilisateurService().lister_tous()
                autre_utilisateur = "Oui"  # Pour supprimer plusieurs utilisateurs à la suite
                while autre_utilisateur == "Oui":
                    compte = inquirer.select(
                        message="Quel compte souhaitez-vous supprimer ?",
                        choices=liste_utilisateurs,
                    ).execute()

                    # Suppression de l'utilisateur
                    UtilisateurService().supprimer(compte)
                    print("\n\nLe compte a bien été supprimé !\n\n")

                    # Fin (ou non de la boucle)
                    autre_utilisateur = inquirer.select(
                        message="Souhaitez-vous supprimer un autre compte ?",
                        choices=["Oui", "Non"],
                    ).execute()

            case "Supprimer une recette":
                print("\n" + "-" * 50 + "\nSuppression d'une recette\n" + "-" * 50 + "\n")

                # Affichage de la liste des recettes
                liste_recette = Session().liste_recettes
                autre_recette = "Oui"  # Pour supprimer plusieurs recettes à la suite
                while autre_recette == "Oui":
                    recette = inquirer.select(
                        message="Quelle recette souhaitez-vous supprimer?",
                        choices=liste_recette,
                    ).execute()

                    # Suppression de la recette
                    RecetteService().supprimer_recette(recette)
                    print("\n\nLa recette a bien été supprimée !")
                    print("Veuillez redémarrer l'application pour voir les modifications...\n\n")

                    # Fin ou non de la boucle
                    autre_recette = inquirer.select(
                        message="Souhaitez-vous supprimer une autre recette ?",
                        choices=["Oui", "Non"],
                    ).execute()

            case "Consulter les recettes":
                print("\n" + "-" * 50 + "\nConsultation des recettes\n" + "-" * 50 + "\n")

                # Affichage de la liste des recettes
                recettes = RecetteService().lister_toutes_recettes()
                autre_recette = "Oui"  # Pour consulter plusieurs recettes à la suite
                while autre_recette == "Oui":
                    # Pour avoir plusieurs pages avec 10 recettes
                    i = 0
                    choix = "-> Page suivante"
                    while choix == "-> Page suivante":
                        i += 1
                        if abs(10 * (i - 1) - len(recettes)) > 10:
                            liste_recettes = recettes[10 * (i - 1) : 10 * i]
                        else:
                            liste_recettes = recettes[10 * (i - 1) :]
                            i = 0
                        liste_recettes.append("-> Page suivante")
                        liste_recettes.append("Retour")

                        choix = inquirer.select(
                            message="Choisissez une recette : ",
                            choices=liste_recettes,
                        ).execute()

                    if choix == "Retour":
                        return MenuAdminVue(message=self.message, utilisateur=self.utilisateur)

                    else:
                        autre_action = "Oui"
                        while autre_action == "Oui":  # Pour réaliser différentes actions à la suite
                            choix_bis = inquirer.select(
                                message="Que voulez-vous faire ?",
                                choices=[
                                    "Lire la recette",
                                    "Voir les notes et les avis",
                                ],
                            ).execute()

                            match choix_bis:

                                case "Lire la recette":
                                    RecetteService().lire_recette(choix)
                                    # Fin (ou non) de la boucle action pour la recette
                                    autre_action = inquirer.select(
                                        message="Réaliser une autre action pour cette recette ?",
                                        choices=["Oui", "Non"],
                                    ).execute()
                                    if autre_action == "Non":
                                        # Fin (ou non) de la boucle consulter une recette
                                        autre_recette = inquirer.select(
                                            message="Consulter une autre recette ? ",
                                            choices=["Oui", "Non"],
                                        ).execute()

                                case "Voir les notes et les avis":
                                    RecetteService().voir_note_avis(choix)
                                    # Fin (ou non) de la boucle action pour la recette
                                    autre_action = inquirer.select(
                                        message="Réaliser une autre action pour cette recette ?",
                                        choices=["Oui", "Non"],
                                    ).execute()
                                    if autre_action == "Non":
                                        # Fin (ou non) de la boucle consulter une recette
                                        autre_recette = inquirer.select(
                                            message="Consulter une autre recette ? ",
                                            choices=["Oui", "Non"],
                                        ).execute()

            case "Modifier un compte":
                print("\n" + "-" * 50 + "\nModification d'un compte\n" + "-" * 50 + "\n")

                # Affichage de la liste des utilisateurs
                liste_utilisateurs = UtilisateurService().lister_tous()
                autre_utilisateur = "Oui"  # Pour modifier plusieurs utilisateurs à la suite

                # Choix de l'utilisateur
                while autre_utilisateur == "Oui":
                    user = inquirer.select(
                        message="Quel compte souhaitez-vous modifier?",
                        choices=liste_utilisateurs,
                    ).execute()
                    autre_changement = "Oui"  # Pour faire plusieurs modifications

                    # Choix des modifications
                    while autre_changement == "Oui":
                        modif = inquirer.select(
                            message="Quelle modification souhaitez-vous appliquer ?",
                            choices=[
                                "Pseudo",
                                "Rôle",
                            ],
                        ).execute()
                        if modif == "Pseudo":
                            pseudo = inquirer.text(
                                message="Veuillez saisir le nouveau pseudo : "
                            ).execute()
                            user.pseudo = pseudo
                        if modif == "Rôle":
                            role = inquirer.select(
                                message="Veuillez sélectionner le nouveau rôle :",
                                choices=["admin", "user"],
                            ).execute()
                            user.role = role
                        autre_changement = inquirer.select(
                            message="Souhaitez-vous effectuer une autre modification ?",
                            choices=["Oui", "Non"],
                        ).execute()

                    # Modification de l'utilisateur
                    user.afficher_info()
                    UtilisateurService().modifier(user=user)
                    print(f"\n\nLe compte id{user.id_utilisateur} a bien été modifié !\n\n")

                    # Fin (ou non) de la boucle pour modifier un utilisateur
                    autre_utilisateur = inquirer.select(
                        message="Souhaitez-vous modifier un autre compte ?",
                        choices=["Oui", "Non"],
                    ).execute()

            case "Ajouter une recette":
                print("\n" + "-" * 50 + "\nAjout d'une nouvelle recette\n" + "-" * 50 + "\n")

                autre_recette = "Oui"  # Pour ajouter plusieurs recettes à la suite
                j = 0
                while autre_recette == "Oui":
                    j += 1  # Si on crée plusieurs recette à la suite (cf. id_recette)
                    # Nom de la recette
                    nom = inquirer.text(message="Entrez le nom de la recette : ").execute()
                    # Ingrédients de la recette
                    liste_ing = []
                    autre_ingredient = "Oui"  # Pour ajouter plusieurs ingrédients
                    while autre_ingredient == "Oui":
                        raw_liste_ingredient = IngredientService().lister_tous()
                        ingredient = "-> Page suivante"
                        i = 0
                        while ingredient == "-> Page suivante":
                            i += 1
                            if abs(10 * i - len(raw_liste_ingredient)) > 10:
                                liste_ingredients = raw_liste_ingredient[10 * (i - 1) : 10 * i]
                            else:
                                liste_ingredients = raw_liste_ingredient[10 * (i - 1) :]
                                i = 0
                            liste_ingredients.append("-> Page suivante")
                            liste_ingredients.append("Retour")
                            ingredient = inquirer.select(
                                message="Choisissez un ingrédient : ",
                                choices=liste_ingredients,
                            ).execute()
                        quantite = inquirer.text("Entrez la quantitée associée : ").execute()
                        liste_ing.append([ingredient, quantite])
                        # Fin (ou non) de la boucle pour les ingrédients
                        autre_ingredient = inquirer.select(
                            message="Souhaitez-vous ajouter un autre ingrédient ?",
                            choices=["Oui", "Non"],
                        ).execute()
                    # Description de la recette
                    description = inquirer.text(
                        message="Entrez la description de la recette : "
                    ).execute()
                    # Identifiant de la recette
                    liste_recette = RecetteService().lister_toutes_recettes()
                    id_recette = len(liste_recette) + 54000 + j
                    # Ajout de la recette à la bdd
                    recette = Recette(
                        nom_recette=nom,
                        id_recette=id_recette,
                        liste_ingredient=liste_ing,
                        description_recette=description,
                    )
                    RecetteService().creer_recette(recette=recette)
                    print(f"\n\nLa recette {recette} a bien été créée !")
                    print("Veuillez redémarrer l'application pour voir les modifications...\n\n")
                    # Fin (ou non) de la boucle pour la création de recette
                    autre_recette = inquirer.select(
                        message="Souhaitez-vous ajouter une autre recette ?", choices=["Oui", "Non"]
                    ).execute()

        return MenuAdminVue(message=self.message, utilisateur=self.utilisateur)
