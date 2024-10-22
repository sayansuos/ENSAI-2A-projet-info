from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from view.session import Session

from src.service.utilisateur_service import UtilisateurService


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
                "Consulter les recettes", #done
                "Consulter les suggestions", #done
                "Consulter les favoris", #done
                "Consulter les ingrédients",
                "Consulter le panier",#done
                "Se déconnecter", #done
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

                return voir_suggestions()
            
            case "Consulter les favoris":

                return voir_favoris()

            case "Consulter le panier":

                return voir_liste_course()
            
            case "Voir les ingrédients":

                pass
