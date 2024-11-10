from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from view.users.menu_inv_vue import MenuInvVue
from service.recette_service import RecetteService
from view.recettes.recettes_vue_inv import RecettesVue


class MenuRecetteSf(VueAbstraite):
    """
    Vue qui affiche :
      - toutes les recettes dispo
      - les options
    """

    def choisir_menu(self):
        recette_service = RecetteService()
        recettes = recette_service.lister_toutes_recettes()

        choix = "-> Page suivante"
        i = 0

        while choix == "-> Page suivante":
            i += 10
            liste_recettes = recettes[i - 10 : i]
            liste_recettes.append("-> Page suivante")
            liste_recettes.append("Retour")
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
                                return MenuInvVue()

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
                                return MenuInvVue()

        return RecettesVue()
