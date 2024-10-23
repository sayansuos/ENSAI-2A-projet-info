from unittest.mock import MagicMock
import pytest
from service.ingredient_service import IngredientService
from dao.ingredient_dao import IngredientDao
from business_object.ingredient import Ingredient

# Liste d'ingrédients pour les tests
liste_ingredients = [
    Ingredient(nom_ingredient="Tomate", id_ingredient=1),
    Ingredient(nom_ingredient="Oignon", id_ingredient=2),
    Ingredient(nom_ingredient="Carotte", id_ingredient=3),
]


def test_creer_ingredient_ok():
    """Création d'un Ingredient réussie"""

    # GIVEN
    nom_ingredient = "Tomate"
    IngredientDao().creer = MagicMock(return_value=True)

    # WHEN
    ingredient = IngredientService().creer(nom_ingredient)

    # THEN
    assert ingredient.nom_ingredient == nom_ingredient


def test_creer_ingredient_echec():
    """Création d'un Ingredient échouée (car la méthode IngredientDao().creer retourne False)"""

    # GIVEN
    nom_ingredient = "Tomate"
    IngredientDao().creer = MagicMock(return_value=False)

    # WHEN
    ingredient = IngredientService().creer(nom_ingredient)

    # THEN
    assert ingredient is None


def test_creer_mauvais_nom():
    """Création d'un Ingredient échouée car le nom n'est pas une chaîne de caractères"""

    # GIVEN
    nom_ingredient = 123

    # WHEN-THEN:
    with pytest.raises(
        TypeError, match="Le nom de l'ingrédient doit être une chaîne de caractères."
    ):
        IngredientService().creer(nom_ingredient)


def test_creer_ingredient_doublon():
    """Création d'un Ingredient échouée si l'ingrédient existe déjà"""

    # GIVEN
    nom_ingredient = "Tomate"
    IngredientDao().creer = MagicMock(side_effect=lambda x: x == nom_ingredient)

    # WHEN
    ingredient = IngredientService().creer(nom_ingredient)

    # THEN
    assert ingredient is None


def test_supprimer_ingredient_ok():
    """Suppression d'un Ingredient réussie"""

    # GIVEN
    id_ingredient = 1
    IngredientDao().supprimer = MagicMock(return_value=True)

    # WHEN
    result = IngredientService().supprimer(id_ingredient)

    # THEN
    assert result is True


def test_supprimer_ingredient_echec():
    """Suppression d'un Ingredient échouée (car la méthode IngredientDao().supprimer retourne False)"""

    # GIVEN
    id_ingredient = 1
    IngredientDao().supprimer = MagicMock(return_value=False)

    # WHEN
    result = IngredientService().supprimer(id_ingredient)

    # THEN
    assert result is False


def test_trouver_ingredient_par_id_ok():
    """Trouver un Ingredient par ID réussie"""

    # GIVEN
    id_ingredient = 1
    expected_ingredient = Ingredient(nom_ingredient="Tomate", id_ingredient=id_ingredient)
    IngredientDao().trouver_par_id = MagicMock(return_value=expected_ingredient)

    # WHEN
    ingredient = IngredientService().trouver_par_id(id_ingredient)

    # THEN
    assert ingredient.nom_ingredient == expected_ingredient.nom_ingredient


def test_trouver_ingredient_par_id_invalide():
    """Trouver un Ingredient par ID échouée si l'ID n'existe pas"""

    # GIVEN
    id_ingredient = 999
    IngredientDao().trouver_par_id = MagicMock(return_value=None)

    # WHEN
    ingredient = IngredientService().trouver_par_id(id_ingredient)

    # THEN
    assert ingredient is None
