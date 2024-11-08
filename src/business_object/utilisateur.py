from business_object.recette import Recette
from business_object.ingredient import Ingredient


class Utilisateur:
    """
    Instancie un Utilisateur
    """

    def __init__(
        self,
        pseudo: str,
        mail: str,
        mdp: str,
        id_utilisateur: int = 1,
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
        self.mdp: str = mdp
        self.mail: str = mail
        self.recette_favorite: list[Recette] = recette_favorite
        self.ingredient_favori: list[Ingredient] = ingredient_favori
        self.ingredient_non_desire: list[Ingredient] = ingredient_non_desire
        self.liste_de_course: list[Ingredient] = liste_de_course
        self.role: str = role

    def __str__(self):
        return f"[{self.id_utilisateur}] {self.pseudo}"

    @property
    def mail(self):
        """Retourne l'adresse mail de l'utilisateur."""
        return self.__mail
