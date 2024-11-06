from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from service.ingredient_service import IngredientService
from service.liste_favoris_service import ListeFavorisService
lfs = ListeFavorisService()


class MenuIngredient(VueAbstraite):
    """Vue qui affiche :
    - tous les ingrédients dans un premier temps
    - puis les options relatives aux ingrédients pour l'utilisateur
    """

    def choisir_menu(self):
        ingredient_service = IngredientService()

        liste_ingredients = ingredient_service.lister_tous()
        liste_ingredients.append("Retour au menu des ingrédients")

        choix = inquirer.select(
            message="Choisissez un ingrédient : ",
            choices=liste_ingredients,
        ).execute()

        if choix == "Retour au menu des ingrédients":
            from view.ingredients.ingredients_vue import IngredientsVue

            return IngredientsVue()
        else :
            choix_bis = inquirer.select(
                message="Que voulez-vous faire ? : ",
                choices=[
                "Ajouter l'ingrédient aux favoris"#done
                "Retirer l'ingrédient des favoris",#done
                "Ajouter l'ingrédient aux non-désirés",#done
                "Retirer l'ingrédient des non-désirés",#done
                ],
            ).execute()
    
            match choix_bis:
                case "Ajouter l'ingrédient aux favoris":

                    return lfs.ajouter_ingredient_favori(choix)

                case "Retirer l'ingrédient des favoris":

                    return lfs.enlever_ingredient_favori(choix)

                case "Ajouter l'ingredient aux non-désirés":

                    return lfs.ajouter_ingredient_non_desire(choix)

                case "Retirer l'ingredient des non-désirés":

                    return lfs.enlever_ingredient_non_desire(choix)
                   
        
        from view.ingredients.ingredients_vue import IngredientsVue

        message = f"C'est fait !\n\n"
        
        return IngredientsVue(message)
