from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from service.utilisateur_service import UtilisateurService
from business_object.utilisateur import Utilisateur

class ModifierCompte(VueAbstraite):

    def choisir_menu(self):
        #demande à l'administrateur l'utilisateur à modifier
        liste_users = UtilisateurService().lister_tous()

        choix = inquirer.select(
            message="Quel est l'utilisateur à modifier ? : ",
            choices=liste_users,
        ).execute()

        mail = inquirer.number(message="Quel est le nouveau mail ? : ")

        pseudo = inquirer.text(message="Quel est le nouveau pseudo ? : ")

        #appel du service pour modifier
        utilisateur = Utilisateur(mail, pseudo)
        user = UtilisateurService().modifier(utilisateur)

        if user:
            message = (f"L'utilisateur {choix} a été modifié")
        else:
            message = "Erreur"
        
        from view.users.menu_admin_vue import MenuAdminVue

        return MenuAdminVue(message)
        
