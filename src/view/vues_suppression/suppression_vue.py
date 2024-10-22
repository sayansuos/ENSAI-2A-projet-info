from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from src.service.utilisateur_service import UtilisateurService


class SuppressionVue(VueAbstraite):
    """Vue qui affiche :
    - la liste des utilisateurs dans un premier temps
    puis qui supprime l'user selectionné
    """

    def choisir_menu(self):
        utilisateur_service = UtilisateurService()

        liste_users = utilisateur_service.lister_tous()
        liste_users.append("Retour au Menu Administrateur")

        choix = inquirer.select(
            message="Choisissez un utilisateur à supprimer : ",
            choices=liste_users,
        ).execute()

        if choix == "Retour au Menu Administrateur":
            from src.view.users.menu_admin_vue import MenuAdminVue

            return MenuAdminVue()
        else :
            from src.view.users.menu_admin_vue import MenuAdminVue

            utilisateur_service.supprimer(choix)
            message = f"L'utilisateur {choix} a été supprimé.\n\n"
            return MenuAdminVue(message)
