from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from view.users.menu_user_vue import MenuUserVue
from view.recettes.recettes_vue_user import RecettesVue

from service.recette_service import RecetteService
from service.liste_favoris_service import ListeFavorisService

lfs = ListeFavorisService()


class MenuRecetteSf(VueAbstraite):
    """Vue qui affiche :
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
                        "Noter et laisser un commentaire",
                        "Ajouter dans les favoris",
                        "Supprimer des favoris",
                        "Ajouter les ingrédients au panier",
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
                                return MenuUserVue()

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
                                return MenuUserVue()

                    case "Noter et laisser un commentaire":

                        pass

                    case "Ajouter dans les favoris":

                        return lfs.ajouter_favoris(choix)

                    case "Supprimer des favoris":

                        return lfs.supprimer_favoris(choix)

                    case "Ajouter les ingredients au panier":
                        ingr = recette_service.ingredients_recette(choix)

                        return lfs.ajouter_ingredient_course(ingr)

        return RecettesVue()
