from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from src.service.recette_service import RecetteService
from src.service.liste_favoris_service import ListeFavorisService
lfs = ListeFavorisService()


class MenuRecetteSf(VueAbstraite):
    """Vue qui affiche :
    - toutes les recettes dispo
    - les options
    """

    def choisir_menu(self):
        recette_service = RecetteService()

        liste_recettes = recette_service.lister_toutes_recettes()
        liste_recettes.append("Retour")

        choix = inquirer.select(
            message="Choisissez une recette : ",
            choices=liste_recettes,
        ).execute()

        if choix == "Retour":
            from src.view.recettes.recettes_vue_user import RecettesVue

            return RecettesVue()
        else:
            choix_bis = inquirer.select(
                message="Que voulez-vous faire ?",
                choices=[
                    "Lire la recette",
                    "Voir les notes et les avis",
                    "Noter et laisser un commentaire",
                    "Ajouter dans les favoris",
                    "Supprimer des favoris",
                    "Ajouter les ingrédients au panier",
                ],
            ).execute()

            match choix_bis:
                case "Lire la recette":

                    return recette_service.voir_recette(choix)
                
                case "Voir les notes et les avis":

                    return recette_service.voir_note(choix), recette_service.voir_avis(choix)
                
                case "Noter et laisser un commentaire":

                    pass

                case "Ajouter dans les favoris":

                    return lfs.ajouter_favoris(choix)
                
                case "Supprimer des favoris":

                    return lfs.supprimer_favoris(choix)
                
                case "Ajouter les ingredients au panier":
                    ingr = recette_service.ingredients_recette(choix)

                    return lfs.ajouter_ingredient_course(ingr)

        return MenuRecetteSf()
