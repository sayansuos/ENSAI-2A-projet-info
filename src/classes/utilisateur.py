from src.classes.recette import Recette
from src.classes.ingredient import Ingredient


class Utilisateur:
    """
    Instancie un Utilisateur
    """

    def __init__(self, id_utilisateur: int, pseudo: str, mdp: str, mail: str,
                 recette_favorite: list[Recette] = [],
                 ingredient_favori: list[Ingredient] = [],
                 ingredient_non_desire: list[Ingredient] = [],
                 liste_de_course: list[Ingredient] = []):
        self.id_utilisateur: int = id_utilisateur
        self.pseudo: str = pseudo
        self.__mdp: str = mdp
        self.__mail: str = mail
        self.recette_favorite: list[Recette] = recette_favorite
        self.ingredient_favori: list[Ingredient] = ingredient_favori
        self.ingredient_non_desire: list[Ingredient] = ingredient_non_desire
        self.liste_de_course: list[Ingredient] = liste_de_course
