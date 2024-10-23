from unittest.mock import MagicMock
import pytest
from src.service.ingredient_service import IngredientService
from src.dao.ingredient_dao import IngredientDao
from src.business_object.ingredient import Ingredient

# Liste d'ingrédients de test
liste_ingredients = [
    Ingredient(name="Tomate", quantity=5),
    Ingredient(name="Carotte", quantity=10),
    Ingredient(name="Pomme", quantity=8),
]


def test_creer_ingredient_ok():
    """Création d'un ingrédient réussie."""

    # GIVEN
    name, quantity = "Tomate", 5
    IngredientDao().creer = MagicMock(return_value=True)

    # WHEN
    ingredient = IngredientService().creer(name, quantity)

    # THEN
    assert ingredient.name == name
    assert ingredient.quantity == quantity


def test_creer_ingredient_echec():
    """Création d'un ingrédient échouée
    (car la méthode IngredientDao().creer retourne False)"""

    # GIVEN
    name, quantity = "Tomate", 5
    IngredientDao().creer = MagicMock(return_value=False)

    # WHEN
    ingredient = IngredientService().creer(name, quantity)

    # THEN
    assert ingredient is None


def test_creer_mauvais_name():
    """Création d'un ingrédient échouée car le nom n'est pas une chaîne de caractères."""

    # GIVEN
    name, quantity = 123, 5

    # WHEN-THEN:
    with pytest.raises(TypeError, match="Le nom doit être une chaîne de caractères."):
        IngredientService().creer(name, quantity)


def test_creer_mauvais_quantity():
    """Création d'un ingrédient échouée car la quantité n'est pas un entier."""

    # GIVEN
    name, quantity = "Tomate", "cinq"

    # WHEN-THEN:
    with pytest.raises(TypeError, match="La quantité doit être un entier positif."):
        IngredientService().creer(name, quantity)


def test_creer_quantity_negatif():
    """Création d'un ingrédient échouée car la quantité est négative."""

    # GIVEN
    name, quantity = "Tomate", -5

    # WHEN-THEN:
    with pytest.raises(ValueError, match="La quantité doit être un entier positif."):
        IngredientService().creer(name, quantity)


def test_trouver_ingredient_par_id_ok():
    """Trouver un ingrédient par ID réussie."""

    # GIVEN
    ingredient_id = 1
    IngredientDao().trouver_par_id = MagicMock(return_value=liste_ingredients[0])

    # WHEN
    ingredient = IngredientService().trouver_par_id(ingredient_id)

    # THEN
    assert ingredient.name == liste_ingredients[0].name


def test_trouver_ingredient_par_id_echec():
    """Trouver un ingrédient par ID échouée (ingrédient non trouvé)."""

    # GIVEN
    ingredient_id = 999  # ID qui n'existe pas
    IngredientDao().trouver_par_id = MagicMock(return_value=None)

    # WHEN
    ingredient = IngredientService().trouver_par_id(ingredient_id)

    # THEN
    assert ingredient is None


def test_lister_tous_ingredients():
    """Lister tous les ingrédients réussie."""

    # GIVEN
    IngredientDao().lister_tous = MagicMock(return_value=liste_ingredients)

    # WHEN
    ingredients = IngredientService().lister_tous()

    # THEN
    assert len(ingredients) == len(liste_ingredients)
