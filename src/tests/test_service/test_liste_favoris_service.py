from unittest.mock import patch, MagicMock
from service.liste_favoris_service import ListeFavorisService
from business_object.recette import Recette
from business_object.ingredient import Ingredient
from business_object.utilisateur import Utilisateur
import pytest


utilisateur = Utilisateur(pseudo="maurice", mdp="1234")
ingredient_1 = Ingredient(nom_ingredient="Pasta", id_ingredient=1)
ingredient_2 = Ingredient(nom_ingredient="Tomato", id_ingredient=2)
ingredient_3 = Ingredient(nom_ingredient="Dough", id_ingredient=3)
ingredient_4 = Ingredient(nom_ingredient="Cheese", id_ingredient=4)
ingredient_5 = Ingredient(nom_ingredient="Meat", id_ingredient=2)
liste_recettes = [
    Recette(
        nom_recette="Spaghetti Bolognese",
        liste_ingredient=[[ingredient_1, "100"], [ingredient_5, "100"]],
        description_recette="Spaghetti avec de la viande",
    ),
    Recette(
        nom_recette="Spaghetti Tomato",
        liste_ingredient=[[ingredient_1, "100"], [ingredient_2, "100"]],
        description_recette="Spaghetti avec de la sauce tomate",
    ),
    Recette(
        nom_recette="Pizza Margherita",
        liste_ingredient=[[ingredient_3, "200"], [ingredient_2, "50"], [ingredient_4, "50"]],
        description_recette="Je sais pas quoi écrire, c'est une pizza",
    ),
]


# Test for ajouter_favoris
def test_ajouter_favoris():
    # GIVEN
    recette = liste_recettes[1]
    utilisateur.recette_favorite = []
    liste_favoris_service = ListeFavorisService()

    # WHEN
    result = liste_favoris_service.ajouter_favoris(recette, utilisateur)

    # THEN
    assert result is True
    assert recette in utilisateur.recette_favorite


# Test for enlever_favoris
def test_enlever_favoris():
    # GIVEN
    recette = liste_recettes[1]
    utilisateur.recette_favorite = [recette]
    liste_favoris_service = ListeFavorisService()

    # WHEN
    result = liste_favoris_service.retirer_favoris(recette, utilisateur)

    # THEN
    assert result is True
    assert recette not in utilisateur.recette_favorite


# Test for ajouter_ingredient_course
def test_ajouter_ingredient_course():
    # GIVEN
    ingredient = ingredient_1
    utilisateur.liste_de_course = []
    liste_favoris_service = ListeFavorisService()

    # WHEN
    result = liste_favoris_service.ajouter_liste_course(ingredient, utilisateur)

    # THEN
    assert result is True
    assert ingredient in utilisateur.liste_de_course


# Test for enlever_ingredient_course
def test_enlever_ingredient_course():
    # GIVEN
    ingredient = ingredient_1
    utilisateur.liste_de_course = [ingredient]
    liste_favoris_service = ListeFavorisService()

    # WHEN
    result = liste_favoris_service.retirer_liste_course(ingredient, utilisateur)

    # THEN
    assert result is True
    assert ingredient not in utilisateur.liste_de_course


# Test for ajouter_ingredient_favori
def test_ajouter_ingredient_favori():
    # GIVEN
    ingredient = ingredient_1
    utilisateur.ingredient_favori = []
    liste_favoris_service = ListeFavorisService()

    # WHEN
    result = liste_favoris_service.modifier_preference_ingredient(ingredient, utilisateur, modif="F")

    # THEN
    assert result is True
    assert ingredient in utilisateur.ingredient_favori


# Test for enlever_ingredient_favori
def test_enlever_ingredient_favori():
    # GIVEN
    ingredient = ingredient_1
    utilisateur.ingredient_favori = [ingredient]
    liste_favoris_service = ListeFavorisService()

    # WHEN
    result = liste_favoris_service.retirer_preference_ingredient(ingredient, utilisateur)

    # THEN
    assert result is True
    assert ingredient not in utilisateur.ingredient_favori


# Test for ajouter_ingredient_non_desire
def test_ajouter_ingredient_non_desire():
    # GIVEN
    ingredient = ingredient_1
    utilisateur.ingredient_non_desire = []
    liste_favoris_service = ListeFavorisService()

    # WHEN
    result = liste_favoris_service.modifier_preference_ingredient(ingredient, utilisateur, modif="ND")

    # THEN
    assert result is True
    assert ingredient in utilisateur.ingredient_non_desire


# Test for enlever_ingredient_non_desire
def test_enlever_ingredient_non_desire():
    # GIVEN
    ingredient = ingredient_1
    utilisateur.ingredient_non_desire = [ingredient]
    liste_favoris_service = ListeFavorisService()

    # WHEN
    result = liste_favoris_service.retirer_preference_ingredient(ingredient, utilisateur)

    # THEN
    assert result is True
    assert ingredient not in utilisateur.ingredient_non_desire


# Test ajouter_favoris with invalid input
def test_ajouter_favoris_invalid_input():
    # GIVEN
    invalid_recette = "NotARecette"  # Invalid type
    liste_favoris_service = ListeFavorisService()

    # WHEN/THEN
    with pytest.raises(TypeError, match="recette doit être une instance de Recette"):
        liste_favoris_service.ajouter_favoris(invalid_recette, utilisateur)


# Test enlever_favoris with invalid input
def test_enlever_favoris_invalid_input():
    # GIVEN
    invalid_recette = 123  # Invalid type
    liste_favoris_service = ListeFavorisService()

    # WHEN/THEN
    with pytest.raises(TypeError, match="recette doit être une instance de Recette"):
        liste_favoris_service.retirer_favoris(invalid_recette, utilisateur)


# Test ajouter_ingredient_course with invalid input
def test_ajouter_ingredient_course_invalid_input():
    # GIVEN
    invalid_ingredient = {"name": "Tomato"}  # Invalid type
    liste_favoris_service = ListeFavorisService()

    # WHEN/THEN
    with pytest.raises(TypeError, match="ingredient doit être une instance d'Ingredient"):
        liste_favoris_service.ajouter_liste_course(invalid_ingredient, utilisateur)


# Test enlever_ingredient_course with invalid input
def test_enlever_ingredient_course_invalid_input():
    # GIVEN
    recette = liste_recettes[1]
    invalid_ingredient = 456  # Invalid type
    liste_favoris_service = ListeFavorisService()

    # WHEN/THEN
    with pytest.raises(TypeError, match="ingredient doit être une instance d'Ingredient"):
        liste_favoris_service.retirer_liste_course(recette, invalid_ingredient, utilisateur)


# Test ajouter_ingredient_favori with invalid input
def test_ajouter_ingredient_favori_invalid_input():
    # GIVEN
    invalid_ingredient = None  # Invalid type
    liste_favoris_service = ListeFavorisService()

    # WHEN/THEN
    with pytest.raises(TypeError, match="ingredient doit être une instance de Ingredient"):
        liste_favoris_service.modifier_preference_ingredient(invalid_ingredient, utilisateur, modif="F")


# Test enlever_ingredient_favori with invalid input
def test_enlever_ingredient_favori_invalid_input():
    # GIVEN
    invalid_ingredient = []  # Invalid type
    liste_favoris_service = ListeFavorisService()

    # WHEN/THEN
    with pytest.raises(TypeError, match="ingredient doit être une instance de Ingredient"):
        liste_favoris_service.retirer_preference_ingredient(invalid_ingredient, utilisateur)


# Test ajouter_ingredient_non_desire with invalid input
def test_ajouter_ingredient_non_desire_invalid_input():
    # GIVEN
    invalid_ingredient = 789  # Invalid type
    liste_favoris_service = ListeFavorisService()

    # WHEN/THEN
    with pytest.raises(TypeError, match="ingredient doit être une instance de Ingredient"):
        liste_favoris_service.modifier_preference_ingredient(invalid_ingredient, utilisateur, modif="ND")


# Test enlever_ingredient_non_desire with invalid input
def test_enlever_ingredient_non_desire_invalid_input():
    # GIVEN
    invalid_ingredient = False  # Invalid type
    liste_favoris_service = ListeFavorisService()

    # WHEN/THEN
    with pytest.raises(TypeError, match="ingredient doit être une instance de Ingredient"):
        liste_favoris_service.retirer_preference_ingredient(invalid_ingredient, utilisateur)


if __name__ == "__main__":
    pytest.main([__file__])
