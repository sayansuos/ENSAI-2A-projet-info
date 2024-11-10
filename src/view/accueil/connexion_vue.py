from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from view.session import Session

from service.utilisateur_service import UtilisateurService


class ConnexionVue(VueAbstraite):
    """Vue de Connexion (saisie de pseudo et mdp)"""

    def choisir_menu(self):
        # Demande à l'utilisateur de saisir pseudo et mot de passe
        pseudo = inquirer.text(message="Entrez votre pseudo : ").execute()
        mdp = inquirer.secret(message="Entrez votre mot de passe :").execute()

        # Appel du service pour trouver l'utilisateur
        utilisateur = UtilisateurService().connecter(pseudo, mdp)

        # Si l'utilisateur a été trouvé à partir des ses identifiants de connexion
        if utilisateur:
            message = f"Vous êtes connecté sous le pseudo {utilisateur.pseudo}"

            # Sauvegarder la session
            Session().connexion(utilisateur)

            if utilisateur.role == "admin":
                # Afficher un menu spécifique pour l'admin
                from view.users.menu_admin_vue import MenuAdminVue

                return MenuAdminVue(message, utilisateur=utilisateur)
            else:
                # Afficher un menu pour un utilisateur normal
                from view.users.menu_user_vue import MenuUserVue

                return MenuUserVue(message, utilisateur=utilisateur)

        # En cas d'erreur de connexion
        message = "Erreur de connexion (pseudo ou mot de passe invalide)"
        from view.accueil.accueil_vue import AccueilVue

        return AccueilVue(message)
