# import regex

from InquirerPy import inquirer
from InquirerPy.validator import PasswordValidator, EmptyInputValidator

from prompt_toolkit.validation import ValidationError, Validator


from view.vue_abstraite import VueAbstraite
from service.utilisateur_service import UtilisateurService


class InscriptionVue(VueAbstraite):

    def choisir_menu(self):

        print("\n" + "-" * 50 + "\nCréation de compte\n" + "-" * 50 + "\n")

        # Demande à l'utilisateur de saisir pseudo, mot de passe...
        pseudo = inquirer.text(message="Entrez votre pseudo : ").execute()

        if UtilisateurService().pseudo_deja_utilise(pseudo):
            from view.accueil.accueil_vue import AccueilVue

            return AccueilVue(f"Le pseudo {pseudo} est déjà utilisé.")

        mdp = inquirer.secret(
            message="Entrez votre mot de passe : ",
            validate=PasswordValidator(
                length=8,
                cap=True,
                number=True,
                message="Au moins 8 caractères, incluant une majuscule et un chiffre",
            ),
        ).execute()

        # Appel du service pour créer le joueur
        user = UtilisateurService().creer(pseudo, mdp)

        # Si le joueur a été créé
        if user:
            message = (
                f"Votre compte {user.pseudo} a été créé. Vous pouvez maintenant vous connecter."
            )
        else:
            message = "Erreur de connexion (pseudo ou mot de passe invalide)"

        from view.accueil.accueil_vue import AccueilVue

        return AccueilVue(message)
