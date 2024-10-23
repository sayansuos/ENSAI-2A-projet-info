import os
import logging
from dotenv import load_dotenv

from utils.log_decorator import log
from utils.singleton import Singleton

from dao.db_connection import DBConnection
from dao.ingredient_dao import IngredientDao
from dao.recette_dao import RecetteDao

from client.ingredient_client import IngredientClient
from client.recette_client import RecetteClient

from business_object.ingredient import Ingredient
from business_object.recette import Recette


class FillDataBase(metaclass=Singleton):
    """
    Remplissage de la base de données.
    """

    @log
    def fill_ingredient(self):
        """
        Lancement du remplissage de la table ingredient.
        Si test_dao = True : réinitialisation des données de test
        """
        liste_ingredient = IngredientClient().get_all_ingredients()
        for ing in liste_ingredient:
            ingredient = Ingredient(id_ingredient=ing[0], nom_ingredient=ing[1])
            IngredientDao().creer(ingredient)
        return True

    @log
    def fill_recette(self):
        """
        Lancement du remplissage de la table recette.
        Si test_dao = True : réinitialisation des données de test
        """
        liste_recette = RecetteClient().get_all_recipes()
        for rec in liste_recette:
            liste_ingredient = []
            for raw_ingredient in rec[2]:
                ingredient = IngredientDao().trouver_par_nom(raw_ingredient[0])
                liste_ingredient.append([ingredient, raw_ingredient[1]])
            recette = Recette(
                id_recette=rec[0],
                nom_recette=rec[1],
                liste_ingredient=liste_ingredient,
                description_recette=rec[3],
                note=None,
                avis=[],
            )
            RecetteDao().creer(recette)
        return True
