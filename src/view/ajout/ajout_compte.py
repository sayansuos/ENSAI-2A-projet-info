import regex

from InquirerPy import inquirer
from InquirerPy.validator import PasswordValidator, EmptyInputValidator

from prompt_toolkit.validation import ValidationError, Validator

from src.business_object.utilisateur import Utilisateur
from view.vue_abstraite import VueAbstraite
from service.utilisateur_service import UtilisateurService


class AjoutVue(VueAbstraite):
    def choisir_menu(self):
        # Demande à l'administrateur de saisir pseudo, mot de passe...
        pseudo = inquirer.text(message="Entrez le pseudo : ").execute()

        if UtilisateurService().pseudo_deja_utilise(pseudo):
            from view.accueil.accueil_vue import AccueilVue

            return AccueilVue(f"Le pseudo {pseudo} est déjà utilisé.")

        mdp = inquirer.secret(
            message="Entrez le mot de passe : ",
            validate=PasswordValidator(
                length=8,
                cap=True,
                number=True,
                message="Au moins 8 caractères, incluant une majuscule et un chiffre",
            ),
        ).execute()

        mail = inquirer.text(message="Entrez le mail : ", validate=MailValidator()).execute()

        # Appel du service pour créer le joueur
        utilisateur = Utilisateur(pseudo, mdp, mail)
        user = UtilisateurService().creer(utilisateur)

        # Si le joueur a été créé
        if user:
            message = (
                f"Le compte {user.pseudo} a été créé."
            )
        else:
            message = "Erreur de connexion (pseudo ou mot de passe invalide)"

        from src.view.users.menu_admin_vue import MenuAdminVue

        return MenuAdminVue(message)


class MailValidator(Validator):
    """la classe MailValidator verifie si la chaine de caractères
    que l'on entre correspond au format de l'email"""

    def validate(self, document) -> None:
        ok = regex.match(r"^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$", document.text)
        if not ok:
            raise ValidationError(
                message="Please enter a valid mail", cursor_position=len(document.text)
            )
