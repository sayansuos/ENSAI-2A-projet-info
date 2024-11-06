from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from view.session import Session

from service.utilisateur_service import UtilisateurService


class MenuAdminVue(VueAbstraite):
    """Vue du menu de l'administrateur

    Attributes
    ----------
    message=''
        str

    Returns
    ------
    view
        retourne la prochaine vue, celle qui est choisie par l'administrateur
    """

    def choisir_menu(self):
        """Choix du menu suivant de l'administrateur

        Return
        ------
        vue
            Retourne la vue choisie par l'administrateur dans le terminal
        """

        print("\n" + "-" * 50 + "\nMenu Administrateur\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Consulter les comptes",#done
                "Consulter les recettes",#done
                "Ajouter un compte",
                "Supprimer un compte", #done
                "Modifier un compte",
                "Ajouter une recette",
                "Supprimer une recette",#done
                "Se déconnecter", #done
            ],
        ).execute()

        match choix:
            case "Se déconnecter":
                Session().deconnexion()
                from view.accueil.accueil_vue import AccueilVue

                return AccueilVue()
            
            case "Consulter les comptes":

                return lister_tous()
            
            case "Supprimer un compte":
                from view.vues_suppression.suppression_vue import SuppressionVue

                return SuppressionVue()
            
            case "Supprimer une recette":
                from view.vues_suppression.suppression_recette_vue import SuppressionRecetteVue

                return SuppressionRecetteVue()

            case "Consulter les recettes":
                from service.recette_service import RecetteService

                return lister_toutes_recettes()
            
            case "Ajouter un compte":
                pass