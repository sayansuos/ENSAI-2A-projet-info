from unittest.mock import patch, MagicMock
from src.services.recette_service import RecetteService
from src.classes.recette import Recette


# Test for trouver_recette_par_nom
@patch("src.services.recette_service.DBConnection")
def test_trouver_recette_par_nom(mock_db_connection):
    # GIVEN
    nom_recette = "Spaghetti Bolognese"
    expected_recette = Recette(id_recette=1, nom_recette=nom_recette,
                               liste_ingredient=[["Pasta", "100"], ["Meat", "100"]])

    # Mock the DB response
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = {"id": 1, "nom": nom_recette,
                                         "liste_ingredient": [["Pasta", "100"], ["Meat", "100"]]}
    mock_db_connection().connection.cursor.return_value.__enter__.return_value = mock_cursor

    recette_service = RecetteService()

    # WHEN
    result = recette_service.trouver_recette_par_nom(nom_recette)

    # THEN
    assert result == expected_recette
    mock_cursor.execute.assert_called_once_with(
        "SELECT * FROM Recette WHERE nom_recette = %(nom)s", {"nom": nom_recette}
    )


# Test for trouver_recette_par_ingredient
@patch("src.services.recette_service.DBConnection")
def test_trouver_recette_par_ingredient(mock_db_connection):
    # GIVEN
    ingredient = "Tomato"
    expected_recettes = [
        Recette(id_recette=1, nom_recette="Spaghetti Bolognese",
                liste_ingredient=[["Pasta", "100"], ["Tomato", "100"]]),
        Recette(id_recette=2, nom_recette="Pizza Margherita",
                liste_ingredient=[["Dough", "200"], ["Tomato", "50"], ["Cheese", "50"]]),
    ]

    # Mock the DB response
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = [
        {"id": 1, "nom": "Spaghetti Bolognese",
         "liste_ingredient": [["Pasta", "100"], ["Tomato", "100"]]},
        {"id": 2, "nom": "Pizza Margherita",
         "liste_ingredient": [["Dough", "200"], ["Tomato", "50"], ["Cheese", "50"]]}
    ]
    mock_db_connection().connection.cursor.return_value.__enter__.return_value = mock_cursor

    recette_service = RecetteService()

    # WHEN
    result = recette_service.trouver_recette_par_ingredient(ingredient)

    # THEN
    assert result == expected_recettes
    mock_cursor.execute.assert_called_once_with(
        "SELECT * FROM Recette WHERE ?", {"ingredient": ingredient}  # Modify SQL as per your query.
    )


# Test for lister_toutes_recettes
@patch("src.services.recette_service.DBConnection")
def test_lister_toutes_recettes(mock_db_connection):
    # GIVEN
    expected_recettes = [
        Recette(id_recette=1, nom_recette="Spaghetti Bolognese",
                liste_ingredient=[["Pasta", "100"], ["Tomato", "100"]]),
        Recette(id_recette=2, nom_recette="Pizza Margherita",
                liste_ingredient=[["Dough", "200"], ["Tomato", "50"], ["Cheese", "50"]]),
    ]

    # Mock the DB response
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = [
        {"id": 1, "nom": "Spaghetti Bolognese",
         "liste_ingredient": [["Pasta", "100"], ["Tomato", "100"]]},
        {"id": 2, "nom": "Pizza Margherita",
         "liste_ingredient": [["Dough", "200"], ["Tomato", "50"], ["Cheese", "50"]]}
    ]
    mock_db_connection().connection.cursor.return_value.__enter__.return_value = mock_cursor

    recette_service = RecetteService()

    # WHEN
    result = recette_service.lister_toutes_recettes()

    # THEN
    assert result == expected_recettes
    mock_cursor.execute.assert_called_once_with("SELECT * FROM Recette")


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
