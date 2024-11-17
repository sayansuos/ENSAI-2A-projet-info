from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from view.users.menu_inv_vue import MenuInvVue
from service.recette_service import RecetteService
from view.recettes.recettes_vue_inv import RecettesVue


class MenuRecetteSf(VueAbstraite):
    """
    Vue pour la consultation de toutes les recettes d'un utilisateur non connecté.
    """

    def choisir_menu(self):
        print("\n" + "-" * 50 + "\nConsultation de toutes les recettes\n" + "-" * 50 + "\n")

        # Affichage de toutes les recettes
        recettes = RecetteService().lister_toutes_recettes()
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

        if choix == "Retour":
            return RecettesVue()

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
                        # Appel au servie pour afficher la recette
                        RecetteService().lire_recette(choix)

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
                        # Appel au service pour afficher la note et les avis
                        RecetteService().voir_note_avis(choix)

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
