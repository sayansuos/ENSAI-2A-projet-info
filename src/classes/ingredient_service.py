from src.business_object.ingredient import Ingredient
from src.business.utilisateur import Utilisateur
from src.dao.ingredient_dao import IngredientDao
from typing import List, Optional


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

    def creer(self, ingredient: Ingredient) -> Optional[Ingredient]:
        """
        Permet d'ajouter un ingrédient dans la base de données

        Args:
            ingredient (Ingredient): Ingrédient à ajouter dans la base de données

        Returns:
            Optional[Ingredient]:
                Retourne un ingrédient si celui-ci a été correctement ajouté à la base de données.
                None sinon
        """

        if not isinstance(ingredient, Ingredient):
            raise TypeError("ingredient doit être une instance de Ingredient.")

        return ingredient if IngredientDao.creer(ingredient) is True else None

    def supprimer(self, ingredient: Ingredient) -> bool:
        """
        Permet de supprimer un ingrédient de la base de données

        Args:
            ingredient (Ingredient): Ingrédient à supprimer de la base de données

        Returns:
            bool:
                True si l'ingrédient a bien été supprimé de la base de données
                False sinon
        """

        if not isinstance(ingredient, Ingredient):
            raise TypeError("ingredient doit être une instance de Ingredient.")

        return IngredientDao.supprimer(ingredient)

    def trouver_ingredient_par_id(self, id: int) -> Optional[Ingredient]:
        """
        Permet de trouver un ingrédient grâce à son identifiant

        Args:
            id (int): Identifiant de l'ingrédient recherché

        Returns:
            Optional[Ingredient]:
                Retourne un ingrédient si l'identifiant correspond à quelque chose dans la base
                de données.
                None sinon
        """

        if not isinstance(id, int):
            raise TypeError("id doit être un entier naturel.")

        return IngredientDao.trouver_par_id(id)
