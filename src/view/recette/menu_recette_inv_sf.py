from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from src.service.recette_service import RecetteService


class MenuRecetteSf(VueAbstraite):
    """Vue qui affiche :
    - toutes les recettes dispo
    - les options
    """

    def choisir_menu(self):
        recette_service = RecetteService()

        liste_recettes = recette_service.lister_toutes_recettes()
        liste_recettes.append("Retour")

        choix = inquirer.select(
            message="Choisissez une recette : ",
            choices=liste_recettes,
        ).execute()

        if choix == "Retour":
            from src.view.recettes.recettes_vue_inv import RecettesVue

            return RecettesVue()
        else:
            choix_bis = inquirer.select(
                message="Que voulez-vous faire ?",
                choices=[
                    "Lire la recette",
                    "Voir les notes et les avis",
                ],
            ).execute()

            match choix_bis:
                case "Lire la recette":

                    return recette_service.voir_description(choix)
                
                case "Voir les notes et les avis":

                    return recette_service.voir_note(choix), recette_service.voir_avis(choix)

        return MenuRecetteSf()
