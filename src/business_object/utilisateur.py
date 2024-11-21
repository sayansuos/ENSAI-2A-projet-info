from business_object.recette import Recette
from business_object.ingredient import Ingredient

from utils.singleton import Singleton

from dotenv import load_dotenv


class Utilisateur:
    """
    Cette classe représente un utilisateur connecté.

    Attributes
    ----------
    pseudo : str
        Pseudo de l'utilisateur
    mdp : str
        Mot de passe de l'utilisateur
    id_utilisateur : int
        Identifiant de l'utilisateur, None par défaut
    recette_favorite : list[Recette]
        Liste des recettes favorites de l'utilisateur, vide par défaut
    ingrédient_favori : list[Ingredient]
        Liste des ingrédients favoris de l'utilisateur, vide par défaut
    ingrédient_non_désiré : list[Ingredient]
        Liste des ingrédients non désirés de l'utilisateur, vide par défaut
    liste_de_course : list[Ingredient]
        Liste des ingrédients de la liste de course, vide par défaut
    role : str
        Rôle de l'utilisateur, 'user' par défaut
    """

    def __init__(
        self,
        pseudo: str,
        mdp: str,
        id_utilisateur: int = None,
        recette_favorite: list[Recette] = [],
        ingredient_favori: list[Ingredient] = [],
        ingredient_non_desire: list[Ingredient] = [],
        liste_de_course: list[Ingredient] = [],
        role: str = "user",
    ):
        """
        Constructeur
        """
        self.id_utilisateur = id_utilisateur
        self.pseudo = pseudo
        self.mdp = mdp
        self.recette_favorite = recette_favorite
        self.ingredient_favori = ingredient_favori
        self.ingredient_non_desire = ingredient_non_desire
        self.liste_de_course = liste_de_course
        self.role = role

    def __str__(self):
        """
        Cette méthode affiche un utilisateur.
        """
        return f"[{self.id_utilisateur}] {self.pseudo}"

    def afficher_info(self):
        """
        Cette méthode affiche les caractéristiques d'un utilisateur.
        """
        print(f"\n\n*** DETAILS ABOUT [{self.id_utilisateur}] {self.pseudo} ***\n")

        # Affichage des recettes favorites
        if self.recette_favorite == []:
            print("Favourite recipes: There is no favourite recipe registered.\n")
        else:
            print("Favourite recipes : \n")
            for recette in self.recette_favorite:
                print(f" - {recette}")
            print("\n")

        # Affichage des ingrédients favoris
        if self.ingredient_favori == []:
            print("Favourite ingredients: There is no favourite ingredient registered.\n")
        else:
            print("\nFavourite ingredients:\n")
            for ing_f in self.ingredient_favori:
                print(f" - {ing_f}")
            print("\n")

        # Affichage des ingrédients non-désirés
        if self.ingredient_non_desire == []:
            print("Unwanted ingredients: There is no unwanted ingredient registered.\n")
        else:
            print("Unwanted ingredients:")
            for ing_nd in self.ingredient_non_desire:
                print(f" - {ing_nd}\n")
            print("\n")

        # Affichage de la liste de course
        if self.liste_de_course == []:
            print("Grocery list: The grocery list is empty.\n")
        else:
            print("Grocery list: \n\n")
            for course in self.liste_de_course:
                print(f" - {course}\n")
            print("\n")
        print(f"Role: {self.role}")
        print("\n\n")


if __name__ == "__main__":
    load_dotenv()
