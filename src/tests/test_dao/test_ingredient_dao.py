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
def test_creer_ingredient(db_connection_mock, ingredient_dao):
    """
    GIVEN an ingredient to be added to the database
    WHEN the creer() method is called
    THEN the ingredient should be added and return True
    """

    # Given
    ingredient = Ingredient(id_ingredient=1, nom_ingredient="Tomato")

    # When
    creation_ok = IngredientDao.creer(ingredient)

    # Then
    assert creation_ok
    assert ingredient.id_ingredient == 1


# Test for the trouver_par_id() method
def test_trouver_par_id(db_connection_mock, ingredient_dao):
    """
    GIVEN an ingredient's id
    WHEN the trouver_par_id() method is called
    THEN the corresponding ingredient should be returned
    """

    # Given
    id_ingredient = 1

    # When
    ingredient = IngredientDao.trouver_par_id(id_ingredient)

    # Then
    assert ingredient is not None


# Test for the lister_tous() method
def test_lister_tous(db_connection_mock, ingredient_dao):
    """
    GIVEN ingredients in the database
    WHEN the lister_tous() method is called
    THEN a list of all ingredients should be returned
    """

    # Given

    # When
    ingredients = ingredient_dao.lister_tous()

    # Then
    assert len(ingredients) == 2
    assert ingredients[0].id_ingredient == 1
    assert ingredients[0].nom_ingredient == "Tomato"
    assert ingredients[1].id_ingredient == 2
    assert ingredients[1].nom_ingredient == "Lettuce"
