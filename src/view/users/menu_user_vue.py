from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from view.session import Session

from service.joueur_service import JoueurService


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
                "Consulter les ingrédients",
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
                from src.view.recettes.recettes_vue_user import RecettesVue

                return RecettesVue()

            case "Consulter les suggestions":
                from src.classes.utilisateur_service import UtilisateurService

                return voir_suggestions()

