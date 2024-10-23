from src.business_object.recette import Recette
from src.business_object.ingredient import Ingredient


class Utilisateur:
    """
    Instancie un Utilisateur
    """

    def __init__(
        self,
        id_utilisateur: int,
        pseudo: str,
        mdp: str,
        mail: str,
        recette_favorite: list[Recette] = [],
        ingredient_favori: list[Ingredient] = [],
        ingredient_non_desire: list[Ingredient] = [],
        liste_de_course: list[Ingredient] = [],
        role: str = "user",
    ):
        """
        Définis un Utilisateur

        Args:
            id_utilisateur (int): identifiant numérique unique de l'utilisateur
            pseudo (str): pseudo unique choisi par l'utilisateur
            mdp (str): mot de passe choisi par l'utilisateur
            mail (str): adresse mail de l'utilisateur
            recette_favorite (list[Recette], optional): liste des recettes favorites
                de l'utilisateur. [] par défaut.
            ingredient_favori (list[Ingredient], optional): liste des ingrédients
                favoris de l'utilisateur. [] par défaut.
            ingredient_non_desire (list[Ingredient], optional): liste des ingrédients
                non désirés de l'utilisateur. [] par défaut.
            liste_de_course (list[Ingredient], optional): liste de course de l'utilisateur.
                [] par défaut.
            admin (str, optional): Définis le rôle de l'utilisateur. "user" pour un
                utilisateur classique. "admin" pour un administrateur. "user" par défaut.
        """
        self.id_utilisateur: int = id_utilisateur
        self.pseudo: str = pseudo
        self.__mdp: str = mdp
        self.__mail: str = mail
        self.recette_favorite: list[Recette] = recette_favorite
        self.ingredient_favori: list[Ingredient] = ingredient_favori
        self.ingredient_non_desire: list[Ingredient] = ingredient_non_desire
        self.liste_de_course: list[Ingredient] = liste_de_course
        self.role: str = role
