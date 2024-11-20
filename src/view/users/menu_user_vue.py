from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from view.session import Session


class MenuUserVue(VueAbstraite):
    """Vue du menu de l'utilisateur

    Attributes
    ----------
    message=''
        str

    Returns
    ------
    view
        retourne la prochaine vue, celle qui est choisie par l'utilisateur
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
