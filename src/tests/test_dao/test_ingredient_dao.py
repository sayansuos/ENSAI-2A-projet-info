import os
import pytest
from unittest.mock import patch
from utils.reset_database import ResetDatabase
from utils.securite import hash_password
from dao.ingredient_dao import IngredientDao
from business_object.ingredient import Ingredient


@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    """Initialisation des données de test"""
    with patch.dict(os.environ, {"SCHEMA": "projet_test_dao"}):
        ResetDatabase().lancer(test_dao=True)
        yield


# Test for the creer() method
def test_creer_ok():
    """
    Création d'un ingrédient réussie.
    """

    # GIVEN
    ingredient = Ingredient(id_ingredient=1, nom_ingredient="Tomato")

    # When
    creation_ok = IngredientDao.creer(ingredient)

    # Then
    assert creation_ok
    assert ingredient.id_ingredient == 1


def test_trouver_par_id_existant():
    """
    Recherche par id d'un joueur existant.
    """

    # GIVEN
    id_ingredient = 1

    # WHEN
    ingredient = IngredientDao.trouver_par_id(id_ingredient)

    # THEN
    assert ingredient is not None


def test_trouver_par_id_non_existant():
    """
    Recherche par id d'un joueur non existant.
    """

    # GIVEN
    id_ingredient = 9999999999999

    # WHEN
    ingredient = IngredientDao.trouver_par_id(id_ingredient)

    # THEN
    assert ingredient is None


def test_lister_tous():
    """
    Vérifie que la méthode renvoie une liste d'ingrédients de taille supérieure ou égale à 2.
    """

    # GIVEN

    # WHEN
    ingredients = IngredientDao().lister_tous()

    # Then
    assert isinstance(ingredients, list)
    for i in ingredients:
        assert isinstance(i, Ingredient)
    assert len(ingredients) >= 2
