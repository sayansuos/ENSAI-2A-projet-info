from src.classes.ingredient import Ingredient
from src.classes.utilisateur import Utilisateur
from src.dao.ingredient_dao import IngredientDao
from typing import List


class IngredientService(Utilisateur):
    """
    Définis les méthodes de la classe Ingredient
    """

    def lister_tous(self) -> List[Ingredient]:
        """
        Retourne la liste de tous les ingrédients dans la base de données

        Returns:
            List[Ingredient]: Liste de tous les ingrédients
        """

        return IngredientDao.lister_tous()
