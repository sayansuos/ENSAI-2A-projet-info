from business_object.recette import Recette
from business_object.ingredient import Ingredient

from utils.singleton import Singleton

from dotenv import load_dotenv


class Utilisateur:
    """
    Cette classe représente un utilisateur avec un pseudo, un mot de passe, un identifiant, une
    liste de recettes favorites, d'ingrédients favoris, d'ingrédients non-désirés, de course, et
    un rôle.
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
        Cette méthode instancie un Utilisateur.

        Args
        ----
            id_utilisateur (int):
                Identifiant de l'utilisateur
            pseudo (str):
                Pseudo de l'utilisateur
            mdp (str):
                Mot de passe de l'utilisateur
            recette_favorite (list[Recette], optional):
                Liste des recettes favorites de l'utilisateur, [] par défaut.
            ingredient_favori (list[Ingredient], optional):
                Liste des ingrédients favoris de l'utilisateur, [] par défaut.
            ingredient_non_desire (list[Ingredient], optional):
                Liste des ingrédients non désirés de l'utilisateur, [] par défaut.
            liste_de_course (list[Ingredient], optional):
                Liste de course de l'utilisateur. [] par défaut.
            admin (str, optional):
                Rôle de l'utilisateur. "user" ou "admin", "user" par défaut.

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
        return f"[{self.id_utilisateur}] {self.pseudo}"

    def afficher_info(self):
        """
        Cette méthode affiche les caractéristique d'un utilisateur.
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
