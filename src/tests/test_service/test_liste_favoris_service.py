from unittest.mock import patch, MagicMock
from src.services.liste_favoris_service import ListeFavorisService
from src.business_object.recette import Recette
from src.business_object.ingredient import Ingredient


# Test for ajouter_favoris
@patch("src.services.liste_favoris_service.Utilisateur")
def test_ajouter_favoris(mock_utilisateur):
    # GIVEN
    recette = Recette(
        id_recette=1,
        nom_recette="Spaghetti Bolognese",
        liste_ingredient=[["Pasta", "100"], ["Meat", "100"]],
    )
    mock_utilisateur.recette_favorite = []
    liste_favoris_service = ListeFavorisService()

    # WHEN
    result = liste_favoris_service.ajouter_favoris(recette)

    # THEN
    assert result is True
    assert recette in mock_utilisateur.recette_favorite


# Test for enlever_favoris
@patch("src.services.liste_favoris_service.Utilisateur")
def test_enlever_favoris(mock_utilisateur):
    # GIVEN
    recette = Recette(
        id_recette=1,
        nom_recette="Spaghetti Bolognese",
        liste_ingredient=[["Pasta", "100"], ["Meat", "100"]],
    )
    mock_utilisateur.recette_favorite = [recette]
    liste_favoris_service = ListeFavorisService()

    # WHEN
    result = liste_favoris_service.enlever_favoris(recette)

    # THEN
    assert result is True
    assert recette not in mock_utilisateur.recette_favorite


# Test for ajouter_ingredient_course
@patch("src.classes.Utilisateur")
def test_ajouter_ingredient_course(mock_utilisateur):
    # GIVEN
    ingredient = Ingredient(id_ingredient=1, nom_ingredient="Tomato")
    mock_utilisateur.liste_de_course = []
    liste_favoris_service = ListeFavorisService()

    # WHEN
    result = liste_favoris_service.ajouter_ingredient_course(ingredient)

    # THEN
    assert result is True
    assert ingredient in mock_utilisateur.liste_de_course


# Test for enlever_ingredient_course
@patch("src.classes.Utilisateur")
def test_enlever_ingredient_course(mock_utilisateur):
    # GIVEN
    ingredient = Ingredient(id_ingredient=1, nom_ingredient="Tomato")
    mock_utilisateur.liste_de_course = [ingredient]
    liste_favoris_service = ListeFavorisService()

    # WHEN
    result = liste_favoris_service.enlever_ingredient_course(ingredient)

    # THEN
    assert result is True
    assert ingredient not in mock_utilisateur.liste_de_course


# Test for ajouter_ingredient_favori
@patch("src.classes.Utilisateur")
def test_ajouter_ingredient_favori(mock_utilisateur):
    # GIVEN
    ingredient = Ingredient(id_ingredient=1, nom_ingredient="Cheese")
    mock_utilisateur.ingredient_favori = []
    liste_favoris_service = ListeFavorisService()

    # WHEN
    result = liste_favoris_service.ajouter_ingredient_favori(ingredient)

    # THEN
    assert result is True
    assert ingredient in mock_utilisateur.ingredient_favori


# Test for enlever_ingredient_favori
@patch("src.classes.Utilisateur")
def test_enlever_ingredient_favori(mock_utilisateur):
    # GIVEN
    ingredient = Ingredient(id_ingredient=1, nom_ingredient="Cheese")
    mock_utilisateur.ingredient_favori = [ingredient]
    liste_favoris_service = ListeFavorisService()

    # WHEN
    result = liste_favoris_service.enlever_ingredient_favori(ingredient)

    # THEN
    assert result is True
    assert ingredient not in mock_utilisateur.ingredient_favori


# Test for ajouter_ingredient_non_desire
@patch("src.classes.Utilisateur")
def test_ajouter_ingredient_non_desire(mock_utilisateur):
    # GIVEN
    ingredient = Ingredient(id_ingredient=1, nom_ingredient="Broccoli")
    mock_utilisateur.ingredient_non_desire = []
    liste_favoris_service = ListeFavorisService()

    # WHEN
    result = liste_favoris_service.ajouter_ingredient_non_desire(ingredient)

    # THEN
    assert result is True
    assert ingredient in mock_utilisateur.ingredient_non_desire


# Test for enlever_ingredient_non_desire
@patch("src.classes.Utilisateur")
def test_enlever_ingredient_non_desire(mock_utilisateur):
    # GIVEN
    ingredient = Ingredient(id_ingredient=1, nom_ingredient="Broccoli")
    mock_utilisateur.ingredient_non_desire = [ingredient]
    liste_favoris_service = ListeFavorisService()

    # WHEN
    result = liste_favoris_service.enlever_ingredient_non_desire(ingredient)

    # THEN
    assert result is True
    assert ingredient not in mock_utilisateur.ingredient_non_desire


# Test ajouter_favoris with invalid input
def test_ajouter_favoris_invalid_input():
    # GIVEN
    invalid_recette = "NotARecette"  # Invalid type
    liste_favoris_service = ListeFavorisService()

    # WHEN/THEN
    with pytest.raises(TypeError, match="recette doit être une instance de Recette"):
        liste_favoris_service.ajouter_favoris(invalid_recette)


# Test enlever_favoris with invalid input
def test_enlever_favoris_invalid_input():
    # GIVEN
    invalid_recette = 123  # Invalid type
    liste_favoris_service = ListeFavorisService()

    # WHEN/THEN
    with pytest.raises(TypeError, match="recette doit être une instance de Recette"):
        liste_favoris_service.enlever_favoris(invalid_recette)


# Test ajouter_ingredient_course with invalid input
def test_ajouter_ingredient_course_invalid_input():
    # GIVEN
    invalid_ingredient = {"name": "Tomato"}  # Invalid type
    liste_favoris_service = ListeFavorisService()

    # WHEN/THEN
    with pytest.raises(TypeError, match="ingredient doit être une instance d'Ingredient"):
        liste_favoris_service.ajouter_ingredient_course(invalid_ingredient)


# Test enlever_ingredient_course with invalid input
def test_enlever_ingredient_course_invalid_input():
    # GIVEN
    invalid_ingredient = 456  # Invalid type
    liste_favoris_service = ListeFavorisService()

    # WHEN/THEN
    with pytest.raises(TypeError, match="ingredient doit être une instance d'Ingredient"):
        liste_favoris_service.enlever_ingredient_course(invalid_ingredient)


# Test ajouter_ingredient_favori with invalid input
def test_ajouter_ingredient_favori_invalid_input():
    # GIVEN
    invalid_ingredient = None  # Invalid type
    liste_favoris_service = ListeFavorisService()

    # WHEN/THEN
    with pytest.raises(TypeError, match="ingredient doit être une instance d'Ingredient"):
        liste_favoris_service.ajouter_ingredient_favori(invalid_ingredient)


# Test enlever_ingredient_favori with invalid input
def test_enlever_ingredient_favori_invalid_input():
    # GIVEN
    invalid_ingredient = []  # Invalid type
    liste_favoris_service = ListeFavorisService()

    # WHEN/THEN
    with pytest.raises(TypeError, match="ingredient doit être une instance d'Ingredient"):
        liste_favoris_service.enlever_ingredient_favori(invalid_ingredient)


# Test ajouter_ingredient_non_desire with invalid input
def test_ajouter_ingredient_non_desire_invalid_input():
    # GIVEN
    invalid_ingredient = 789  # Invalid type
    liste_favoris_service = ListeFavorisService()

    # WHEN/THEN
    with pytest.raises(TypeError, match="ingredient doit être une instance d'Ingredient"):
        liste_favoris_service.ajouter_ingredient_non_desire(invalid_ingredient)


# Test enlever_ingredient_non_desire with invalid input
def test_enlever_ingredient_non_desire_invalid_input():
    # GIVEN
    invalid_ingredient = False  # Invalid type
    liste_favoris_service = ListeFavorisService()

    # WHEN/THEN
    with pytest.raises(TypeError, match="ingredient doit être une instance d'Ingredient"):
        liste_favoris_service.enlever_ingredient_non_desire(invalid_ingredient)


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
