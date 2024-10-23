from unittest.mock import MagicMock
import pytest
from service.ingredient_service import IngredientService
from dao.ingredient_dao import IngredientDao
from business_object.ingredient import Ingredient

liste_ingredients = [
    Ingredient(nom_ingredient="Tomate", id_ingredient=1),
    Ingredient(nom_ingredient="Oignon", id_ingredient=2),
    Ingredient(nom_ingredient="Carotte", id_ingredient=3),
]


def test_creer_ingredient_ok():
    """Création d'un Ingredient réussie"""

    # GIVEN
    nom_ingredient = "Tomate"
    ingredient = Ingredient(nom_ingredient=nom_ingredient, id_ingredient=1)
    IngredientDao.creer = MagicMock(return_value=True)

    # WHEN
    created_ingredient = IngredientService().creer(ingredient)

    # THEN
    assert created_ingredient.nom_ingredient == nom_ingredient


def test_creer_ingredient_echec():
    """Création d'un Ingredient échouée (car la méthode IngredientDao().creer retourne False)"""

    # GIVEN
    ingredient = Ingredient(nom_ingredient="Tomate", id_ingredient=1)
    IngredientDao.creer = MagicMock(return_value=False)

    # WHEN
    created_ingredient = IngredientService().creer(ingredient)

    # THEN
    assert created_ingredient is None


def test_creer_mauvais_nom():
    """Création d'un Ingredient échouée car le nom n'est pas une chaîne de caractères"""

    # GIVEN
    nom_ingredient = 123
    ingredient = Ingredient(nom_ingredient=nom_ingredient, id_ingredient=1)

    # WHEN-THEN:
    with pytest.raises(TypeError, match="ingredient doit être une instance de Ingredient."):
        IngredientService().creer(nom_ingredient)


def test_creer_ingredient_doublon():
    """Création d'un Ingredient échouée si l'ingrédient existe déjà"""

    # GIVEN
    ingredient = Ingredient(nom_ingredient="Tomate", id_ingredient=1)
    IngredientDao.creer = MagicMock(return_value=False)

    # WHEN
    created_ingredient = IngredientService().creer(ingredient)

    # THEN
    assert created_ingredient is None


def test_trouver_ingredient_par_id_ok():
    """Trouver un Ingredient par ID réussie"""

    # GIVEN
    id_ingredient = 1
    expected_ingredient = Ingredient(nom_ingredient="Tomate", id_ingredient=id_ingredient)
    IngredientDao.trouver_par_id = MagicMock(return_value=expected_ingredient)

    # WHEN
    ingredient = IngredientService().trouver_ingredient_par_id(id_ingredient)

    # THEN
    assert ingredient.nom_ingredient == expected_ingredient.nom_ingredient


def test_trouver_ingredient_par_id_invalide():
    """Trouver un Ingredient par ID échouée si l'ID n'existe pas"""

    # GIVEN
    id_ingredient = 999
    IngredientDao.trouver_par_id = MagicMock(return_value=None)

    # WHEN
    ingredient = IngredientService().trouver_ingredient_par_id(id_ingredient)

    # THEN
    assert ingredient is None
