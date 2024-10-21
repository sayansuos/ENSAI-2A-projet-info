from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from view.session import Session

from service.joueur_service import JoueurService


class MenuInvVue(VueAbstraite):
    """Vue du menu de l'invité

    Attributes
    ----------
    message=''
        str

    Returns
    ------
    view
        retourne la prochaine vue, celle qui est choisie par l'invité
    """

    def choisir_menu(self):
        """Choix du menu suivant de l'invité

        Return
        ------
        vue
            Retourne la vue choisie par l'invité dans le terminal
        """

        print("\n" + "-" * 50 + "\nMenu Invité\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Consulter les recettes",
                "Retour",
            ],
        ).execute()

        match choix:
            case "Retour":
                from view.accueil.accueil_vue import AccueilVue

                return AccueilVue()
            
            case "Consulter les recettes":
                from src.classes.recettes_service import RecetteService

                return lister_toutes_recettes
