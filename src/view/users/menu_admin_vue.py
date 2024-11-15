from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from view.session import Session

from service.utilisateur_service import UtilisateurService
from service.recette_service import RecetteService


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
                "Consulter les comptes",  # done
                "Consulter les recettes",  # done
                "Supprimer un compte",  # done
                # "Modifier un compte",
                "Ajouter une recette",
                "Supprimer une recette",  # done
                "Se déconnecter",  # done
            ],
        ).execute()

        match choix:
            case "Se déconnecter":
                Session().deconnexion()
                from view.accueil.accueil_vue import AccueilVue

                return AccueilVue()

            case "Consulter les comptes":
                liste_utilisateurs = UtilisateurService().lister_tous()
                print("\n\nListe des utilisateurs de 'MyKitchen' :")
                for u in liste_utilisateurs:
                    print(u)
                print("\n\n")

                ok = inquirer.select(
                    message="Ok ?",
                    choices=["Ok"],
                ).execute()
                if ok == "Ok":
                    return MenuAdminVue(message=self.message, utilisateur=self.utilisateur)

            case "Supprimer un compte":
                liste_utilisateurs = UtilisateurService().lister_tous()
                compte = inquirer.select(
                    message="Quel compte voulez-vous supprimer?",
                    choices=liste_utilisateurs,
                ).execute()
                UtilisateurService().supprimer(compte)
                print("Le compte a bien été supprimé !")
                ok = inquirer.select(
                    message="Ok ?",
                    choices=["Ok"],
                ).execute()
                if ok == "Ok":
                    return MenuAdminVue(message=self.message, utilisateur=self.utilisateur)

            case "Supprimer une recette":
                liste_recette = Session().liste_recettes
                recette = inquirer.select(
                    message="Quelle recette voulez-vous supprimer?",
                    choices=liste_recette,
                ).execute()
                RecetteService().supprimer_recette(recette)
                ok = inquirer.select(
                    message="Ok ?",
                    choices=["Ok"],
                ).execute()
                print("La recette a bien été supprimée !")
                if ok == "Ok":
                    return MenuAdminVue(message=self.message, utilisateur=self.utilisateur)

            case "Consulter les recettes":
                recette_service = RecetteService()
                recettes = recette_service.lister_toutes_recettes()

                choix = "-> Page suivante"
                i = 0

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
                    while autre_action == "Oui":
                        choix_bis = inquirer.select(
                            message="Que voulez-vous faire ?",
                            choices=[
                                "Lire la recette",
                                "Voir les notes et les avis",
                            ],
                        ).execute()

                        match choix_bis:
                            case "Lire la recette":
                                print(recette_service.lire_recette(choix), "\n\n")
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
                                        return MenuAdminVue(
                                            message=self.message, utilisateur=self.utilisateur
                                        )

                            case "Voir les notes et les avis":
                                print(recette_service.voir_note_avis(choix), "\n\n")
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
                                        return MenuAdminVue(
                                            message=self.message, utilisateur=self.utilisateur
                                        )

            case "Ajouter un compte":
                pass

        return MenuAdminVue(message=self.message, utilisateur=self.utilisateur)
