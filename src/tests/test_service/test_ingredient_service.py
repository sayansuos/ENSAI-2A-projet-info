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
    """Création d'un Ingredient réussi"""
    nom_ingredient, id_ingredient = "Salade", 10
    # ingredient = Ingredient(nom_ingredient=nom_ingredient, id_ingredient=id_ingredient)
    IngredientDao().creer = MagicMock(return_value=True)

    created_ingredient = IngredientService().creer(
        ingredient=Ingredient(nom_ingredient=nom_ingredient, id_ingredient=id_ingredient)
    )

    assert created_ingredient.nom_ingredient == nom_ingredient


def test_creer_mauvais_nom():
    """Création d'un Ingredient échouée car ce n'est pas un Ingredient"""
    ingredient = 123

    with pytest.raises(TypeError, match="ingredient doit être une instance de Ingredient."):
        IngredientService().creer(ingredient)


def test_creer_nom_vide():
    """Création d'un Ingredient échouée car le nom est vide"""
    ingredient = Ingredient(nom_ingredient="", id_ingredient=1)
    IngredientDao().creer = MagicMock(return_value=False)

    created_ingredient = IngredientService().creer(ingredient)

    assert created_ingredient is None


def test_creer_ingredient_doublon():
    """Création d'un Ingredient échouée si l'ingrédient existe déjà"""
    ingredient = Ingredient(nom_ingredient="Tomate", id_ingredient=1)
    IngredientDao().creer = MagicMock(return_value=False)

    created_ingredient = IngredientService().creer(ingredient)

    assert created_ingredient is None


def test_creer_ingredient_erreur_connexion():
    """Création d'un Ingredient échouée en raison d'une erreur de connexion à la base de données"""
    ingredient = Ingredient(nom_ingredient="Tomate", id_ingredient=1)
    IngredientDao().creer = MagicMock(side_effect=Exception("Erreur de connexion"))

    with pytest.raises(Exception, match="Erreur de connexion"):
        IngredientService().creer(ingredient)


def test_trouver_ingredient_par_id_ok():
    """Trouver un Ingredient par ID réussie"""
    id_ingredient = 1
    expected_ingredient = Ingredient(nom_ingredient="Tomate", id_ingredient=id_ingredient)
    IngredientDao().trouver_par_id = MagicMock(return_value=expected_ingredient)

    ingredient = IngredientService().trouver_ingredient_par_id(id_ingredient)

    assert ingredient.nom_ingredient == expected_ingredient.nom_ingredient


def test_trouver_ingredient_par_id_invalide():
    """Trouver un Ingredient par ID échouée si l'ID n'existe pas"""
    id_ingredient = 999
    IngredientDao().trouver_par_id = MagicMock(return_value=None)

    ingredient = IngredientService().trouver_ingredient_par_id(id_ingredient)

    assert ingredient is None


def test_trouver_ingredient_par_nom_ok():
    """Trouver un Ingredient par nom réussie"""
    nom_ingredient = "Tomate"
    expected_ingredient = Ingredient(nom_ingredient=nom_ingredient, id_ingredient=1)
    IngredientDao().trouver_par_nom = MagicMock(return_value=expected_ingredient)

    ingredient = IngredientService().trouver_par_nom(nom_ingredient)

    assert ingredient.nom_ingredient == expected_ingredient.nom_ingredient


def test_trouver_ingredient_par_nom_invalide():
    """Trouver un Ingredient par nom échouée si le nom n'existe pas"""
    nom_ingredient = "Ingredient pas bon"
    IngredientDao().trouver_par_nom = MagicMock(return_value=None)

    ingredient = IngredientService().trouver_par_nom(nom_ingredient)

    assert ingredient is None


if __name__ == "__main__":
    pytest.main([__file__])
