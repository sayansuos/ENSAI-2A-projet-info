```mermaid
classDiagram
    class Utilisateur {
        +id_utilisateur: int
        +pseudo: str
        +mdp: str
        +mail: str
        +recette_favorite: list[Recette]
        +ingredient_favori: list[Ingredient]
        +ingredient_non_desire: list[Ingredient]
        +liste_de_course: list[Ingredient]
    }

    class UtilisateurService {
        +creer(str...): Utilisateur
        +supprimer(Utilisateur): bool
        +connecter(str, str): Utilisateur

        +voir_suggestions(): list[Recette]

        +voir_favoris(): recette_favorite

        +voir_liste_course(): liste_de_course

        +voir_ingredients_favoris(): ingredient_favori

        +voir_ingredients_non_desires(): ingredient_non_desire
    }


    class ListeFavorisService {
        +ajouter_favoris(Recette): bool
        +enlever_favoris(Recette): bool

        +ajouter_ingredient_course(ingredient): bool
        +enlever_ingredient_course(ingredient): bool

        +ajouter_ingredient_favori(ingredient):
        +enlever_ingredient_favori(ingredient):

        +ajouter_ingredient_non_desire(ingredient):
        +enlever_ingredient_non_desire(ingredient):
    }


    class Recette {
        +id_recette: int
        +nom_recette: str
        +liste_ingredient: list[list[ingredient, str]]
    }

    class RecetteService {
        +trouver_recette_par_nom(str): Recette
        +trouver_recette_par_ingredient(str): list[Recette]
        +lister_toutes_recettes(): list[Recette]
    }


    class Ingredient {
        +id_ingredient: int
        +nom_ingredient: str
    }


    Utilisateur <.. UtilisateurService: utilise
    Utilisateur <.. ListeFavorisService: utilise

    Recette <.. RecetteService: utilise


    Recette <.. Utilisateur: utilise
    Ingredient <.. Utilisateur: utilise
```
