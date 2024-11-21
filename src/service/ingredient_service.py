from business_object.ingredient import Ingredient
from business_object.utilisateur import Utilisateur
from dao.ingredient_dao import IngredientDao
from typing import List, Optional


class IngredientService:
    """
    Cette classe contient les méthodes de service pour les ingrédients.
    """

    def lister_tous(self) -> List[Ingredient]:
        """
        Retourne la liste de tous les ingrédients dans la base de données

        Returns:
            List[Ingredient]: Liste de tous les ingrédients
        """

        return IngredientDao().lister_tous()

    def creer(self, ingredient: Ingredient) -> Optional[Ingredient]:
        """
        Cette méthode permet de créer un ingrédient dans la base de données.

        Parameters
        ----------
        ingredient : Ingredient
            Ingrédient que l'on souhaite créer

        Returns
        -------
        Bool :
            True si la création est un succès, False sinon
        """
        # Vérification des attribus
        if not isinstance(ingredient, Ingredient):
            raise TypeError("ingredient doit être une instance de Ingredient.")
        # Appel à la DAO
        return ingredient if IngredientDao.creer(ingredient) is True else None

    def trouver_ingredient_par_id(self, id: int) -> Optional[Ingredient]:
        """
        Cette méthode permet de trouver un ingrédient grace à son identifiant.

        Parameters
        ----------
        id_ingredient : int
            Identifiant de l'ingrédient que l'on souhaite trouver

        Returns
        -------
        Ingredient :
            Ingrédient que l'on souhaite trouver
        """
        # Vérification des attributs
        if not isinstance(id, int):
            raise TypeError("id doit être un entier naturel.")
        # Appel à la DAO
        return IngredientDao().trouver_par_id(id)

    def trouver_par_nom(self, nom: str) -> Ingredient:
        """
        Cette méthode permet de trouver un ingrédient grace à son nom.

        Parameters
        ----------
        nom_ingredient : str
            Nom de l'ingrédient que l'on souhaite trouver

        Returns
        -------
        ingredient : Ingredient
            Ingredient que l'on souhaite trouver
        """
        # Vérification des attributs
        if not isinstance(nom, str):
            raise TypeError("nom doit être une instance de str.")
        # Appel à la DAO
        return IngredientDao().trouver_par_nom(nom)
