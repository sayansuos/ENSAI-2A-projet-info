```mermaid
classDiagram
    class Utilisateur {
        +id_joueur: int
        +pseudo: string
        +mdp: string
        +mail: string
        +recette_favorite: list[Recette]
        +ingredient_favori: list[Ingredient]
        +ingredient_non_desire: list[Ingredient]
        +liste_de_course: list[Ingredient]
    }

    class UtilisateurDAO {
        +creer(str...): bool
        +connecter(str, str): Utilisateur
        +trouver_recette_par_nom(str): Recette
        +trouver_recette_par_ingredient(str): list[Recette]
        +lister_toutes_recettes(): list[Recette]
        +voir_suggestions(): list[Recette]

        +voir_favoris(): recette_favorite
        +ajouter_favoris(ingredient): bool
        +enlever_favoris(ingredient): bool

        +voir_liste_course(): liste_de_course
        +ajouter_ingredient_course(ingredient): bool
        +enlever_ingredient_course(ingredient): bool

        +voir_ingredients_favoris(): ingredient_favori
        +ajouter_ingredient_favori(ingredient): bool
        +enlever_ingredient_favori(ingredient): bool

        +voir_ingredients_non_desires(): ingredient_non_desire
        +ajouter_ingredient_non_desire(ingredient): bool
        +enlever_ingredient_non_desirek(ingredient): bool

        +supprimer(Utilisateur): bool
        +se_connecter(str,str): Utilisateur
    }

    class UtilisateurService {
        +creer(str...): Utilisateur
        +connecter(str, str): Utilisateur
        +trouver_recette_par_nom(str): Recette
        +trouver_recette_par_ingredient(str): list[Recette]
        +lister_toutes_recettes(): list[Recette]
        +voir_suggestions(): list[Recette]

        +voir_favoris(): recette_favorite
        +ajouter_favoris(ingredient):
        +enlever_favoris(ingredient):

        +voir_liste_course(): liste_de_course
        +ajouter_ingredient_course(ingredient):
        +enlever_ingredient_course(ingredient):

        +voir_ingredients_favoris(): ingredient_favori
        +ajouter_ingredient_favori(ingredient):
        +enlever_ingredient_favori(ingredient):

        +voir_ingredients_non_desires(): ingredient_non_desire
        +ajouter_ingredient_non_desire(ingredient):
        +enlever_ingredient_non_desirek(ingredient):

        +supprimer(Utilisateur): bool
        +se_connecter(str,str): Utilisateur
    }

    class Recette {
        +id_recette: int
        +nom_recette: str
        +liste_ingredient: list[list[ingredient, str]]
    }

    class Ingredient {
        +id_ingredient: int
        +nom_ingredient: str
    }

    class MenuUtilisateurVue {
    }

    class VueAbstraite{
      +afficher()
      +choisir_menu()
    }

    VueAbstraite <|-- AccueilVue
    VueAbstraite <|-- ConnexionVue
    VueAbstraite <|-- MenuUtilisateurVue
    MenuUtilisateurVue ..> UtilisateurService : appelle
    ConnexionVue ..> UtilisateurService : appelle
    UtilisateurService ..> UtilisateurDAO : appelle
    Utilisateur <.. UtilisateurService: utilise
    Utilisateur <.. UtilisateurDAO: utilise
    Recette <.. Utilisateur: utilise
    Ingredient <.. Utilisateur: utilise
```
