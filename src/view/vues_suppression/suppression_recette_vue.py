from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from src.service.recette_service import RecetteService


class SuppressionRecetteVue(VueAbstraite):
    """Vue qui affiche :
    - la liste des recettes dans un premier temps
    puis qui supprime la recette selectionnée
    """

    def choisir_menu(self):
        recette_service = RecetteService()

        liste_recettes = recette_service.lister_toutes_recettes()
        liste_users.append("Retour au Menu Administrateur")

        choix = inquirer.select(
            message="Choisissez une recette à supprimer : ",
            choices=liste_recettes,
        ).execute()

        if choix == "Retour au Menu Administrateur":
            from src.view.users.menu_admin_vue import MenuAdminVue

            return MenuAdminVue()
        else :
            from src.view.users.menu_admin_vue import MenuAdminVue

            recette_service.supprimer(choix)
            message = f"La recette {choix} a été supprimée.\n\n"
            return MenuAdminVue(message)
