from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from view.session import Session

from service.utilisateur_service import UtilisateurService


class MenuUserVue(VueAbstraite):
    """
    Vue du menu de l'utilisateur
    """

    def __init__(self, message, utilisateur):
        super().__init__(message)
        self.utilisateur = utilisateur

    def choisir_menu(self):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """
        print("\n" + "-" * 50 + "\nMenu Utilisateur\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Consulter les recettes",
                "Consulter les suggestions",
                "Consulter les favoris",
                "Consulter les préférences ingrédients",
                "Consulter le panier",
                "Modifier mon compte",
                "Se déconnecter",
            ],
        ).execute()

        match choix:
            case "Se déconnecter":
                Session().deconnexion()
                from view.accueil.accueil_vue import AccueilVue

                return AccueilVue()

            case "Consulter les recettes":
                from view.recette.menu_recette_user_vue import MenuRecetteUserVue

                return MenuRecetteUserVue(message=self.message, utilisateur=self.utilisateur)

            case "Consulter les suggestions":
                from view.recette.recette_user_sugg_vue import RecetteUserSuggVue

                return RecetteUserSuggVue(message=self.message, utilisateur=self.utilisateur)

            case "Consulter les favoris":
                from view.recette.recette_user_fav_vue import RecetteUserFavVue

                return RecetteUserFavVue(message=self.message, utilisateur=self.utilisateur)

            case "Consulter le panier":
                from view.ingredient.liste_ingredient_vue import ListeIngredientVue

                return ListeIngredientVue(message=self.message, utilisateur=self.utilisateur)

            case "Consulter les préférences ingrédients":
                from view.ingredient.pref_ingredient_vue import PrefIngredientVue

                return PrefIngredientVue(message=self.message, utilisateur=self.utilisateur)

            case "Modifier mon compte":
                print("\n" + "-" * 50 + "\nModification du compte\n" + "-" * 50 + "\n")

                user = self.utilisateur
                autre_changement = "Oui"  # Pour faire plusieurs modifications
                # Choix des modifications
                while autre_changement == "Oui":
                    modif = inquirer.select(
                        message="Quelle modification souhaitez-vous appliquer ?",
                        choices=[
                            "Pseudo",
                        ],
                    ).execute()
                    if modif == "Pseudo":
                        pseudo = inquirer.text(
                            message="Veuillez saisir le nouveau pseudo : "
                        ).execute()
                        user.pseudo = pseudo
                    autre_changement = inquirer.select(
                        message="Souhaitez-vous effectuer une autre modification ?",
                        choices=["Oui", "Non"],
                    ).execute()

                # Modification de l'utilisateur
                user.mdp = inquirer.secret(message="Entrez votre mot de passe :").execute()
                UtilisateurService().modifier(user=user)
                user.mdp = None
                print(f"\n\nLe compte {user.pseudo} a bien été modifié !\n\n")
                inquirer.select(message="", choices=["Ok"]).execute()

                return MenuUserVue(message=self.message, utilisateur=self.utilisateur)
