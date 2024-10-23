from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from src.service.utilisateur_service import UtilisateurService


class PanierVue(VueAbstraite):
    """Vue qui affiche :
    - le panier de l'utilisateur
    - les options
    """

    def choisir_menu(self):
        utilisateur_service = UtilisateurService()

        liste_course = utilisateur_service.voir_liste_course()
        liste_course.append("Retour")

        choix = inquirer.select(
            message="Choisissez un ingrédient de la liste à retirer : ",
            choices=liste_course,
        ).execute()

        if choix == "Retour":
            from src.view.menu_user_vue import MenuUserVue

            return MenuUserVue()
        else:
            from src.service.liste_favoris_service import ListeFavorisService

            return enlever_ingredient_course(choix)

        from src.view.menu_user_vue import MenuUserVue

        message = f"L'ingrédient {choix} a été retiré de la liste de course\n\n"
        
        return MenuUserVue(message)
