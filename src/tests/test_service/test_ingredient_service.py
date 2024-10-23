import pytest
from unittest.mock import MagicMock
from src.business_object.ingredient import Ingredient
from src.dao.ingredient_dao import IngredientDao
from src.service.ingredient_service import IngredientService


@pytest.fixture
def ingredient_service():
    """Fixture pour créer une instance d'IngredientService."""
    service = IngredientService()
    service.lister_tous = MagicMock()
    service.creer = MagicMock()
    service.supprimer = MagicMock()
    service.trouver_ingredient_par_id = MagicMock()
    return service


def test_lister_tous(ingredient_service):
    """Test de la méthode lister_tous."""
    # Given
    ingredient_service.lister_tous.return_value = [
        Ingredient(name="Tomate"),
        Ingredient(name="Oignon"),
    ]

    # When
    result = ingredient_service.lister_tous()

    # Then
    assert len(result) == 2
    assert result[0].name == "Tomate"
    assert result[1].name == "Oignon"


def test_creer_ingredient_valide(ingredient_service):
    """Test de la méthode creer avec un ingrédient valide."""
    # Given
    ingredient = Ingredient(name="Carotte")
    ingredient_service.creer.return_value = ingredient

    # When
    result = ingredient_service.creer(ingredient)

    # Then
    assert result is not None
    assert result.name == "Carotte"


def test_creer_ingredient_invalide(ingredient_service):
    """Test de la méthode creer avec un ingrédient invalide."""
    # Given
    ingredient_service.creer.return_value = None

    # When
    result = ingredient_service.creer("invalid_ingredient")

    # Then
    assert result is None


def test_supprimer_ingredient_valide(ingredient_service):
    """Test de la méthode supprimer avec un ingrédient valide."""
    # Given
    ingredient = Ingredient(name="Poivron")
    ingredient_service.supprimer.return_value = True

    # When
    result = ingredient_service.supprimer(ingredient)

    # Then
    assert result is True


def test_supprimer_ingredient_invalide(ingredient_service):
    """Test de la méthode supprimer avec un ingrédient qui n'existe pas."""
    # Given
    ingredient = Ingredient(name="Inexistant")
    ingredient_service.supprimer.return_value = False

    # When
    result = ingredient_service.supprimer(ingredient)

    # Then
    assert result is False


def test_trouver_ingredient_par_id(ingredient_service):
    """Test de la méthode trouver_ingredient_par_id."""
    # Given
    ingredient = Ingredient(name="Ail", id=1)
    ingredient_service.trouver_ingredient_par_id.return_value = ingredient

    # When
    result = ingredient_service.trouver_ingredient_par_id(1)

    # Then
    assert result is not None
    assert result.name == "Ail"
    assert result.id == 1


def test_trouver_ingredient_par_id_invalide(ingredient_service):
    """Test de la méthode trouver_ingredient_par_id pour un ID inexistant."""
    # Given
    ingredient_service.trouver_ingredient_par_id.return_value = None

    # When
    result = ingredient_service.trouver_ingredient_par_id(999)

    # Then
    assert result is None
