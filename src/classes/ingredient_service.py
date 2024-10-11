from src.classes.ingredient import Ingredient
from src.dao.db_connection import DBConnection


class IngredientService(Ingredient):
    """
    Définis les méthodes de la classe Ingredient
    """

    def ajouter_ingredient_course(ingredient):
        """
        Ajoute l'ingrédient dans la liste de course de l'utilisateur
        """
        if not isinstance(ingredient, Ingredient):
            raise TypeError("ingredient doit être une instance de Ingredient")
        pass

    def enlever_ingredient_course(ingredient):
        """
        Retire l'ingrédient de la liste de course de l'utilisateur
        """
        if not isinstance(ingredient, Ingredient):
            raise TypeError("ingredient doit être une instance de Ingredient")
        pass

    def ajouter_ingredient_favori(ingredient):
        """
        Ajoute l'ingrédient à la liste des ingrédients favoris de l'utilisateur
        """
        if not isinstance(ingredient, Ingredient):
            raise TypeError("ingredient doit être une instance de Ingredient")
        pass

    def enlever_ingredient_favori(ingredient):
        """
        Retire l'ingrédient de la liste des ingrédients favoris de
        l'utilisateur
        """
        if not isinstance(ingredient, Ingredient):
            raise TypeError("ingredient doit être une instance de Ingredient")
        pass

    def ajouter_ingredient_non_desire(ingredient):
        """
        Ajoute l'ingrédient à la liste des ingrédients non désirés de
        l'utilisateur
        """
        if not isinstance(ingredient, Ingredient):
            raise TypeError("ingredient doit être une instance de Ingredient")
        pass

    def enlever_ingredient_non_desire(ingredient):
        """
        Retire l'ingrédient de la liste des ingrédients non désirés de
        l'utilisateur
        """
        if not isinstance(ingredient, Ingredient):
            raise TypeError("ingredient doit être une instance de Ingredient")
        pass
