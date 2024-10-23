from unittest.mock import patch, MagicMock
from services.recette_service import RecetteService
from business_object.recette import Recette
from business_object.ingredient import Ingredient


# Test for trouver_recette_par_nom
@patch("services.recette_service.DBConnection")
def test_trouver_recette_par_nom_ok(mock_db_connection):
    # GIVEN
    nom_recette = "Spaghetti Bolognese"
    expected_recette = Recette(
        id_recette=1, nom_recette=nom_recette, liste_ingredient=[["Pasta", "100"], ["Meat", "100"]]
    )

    # Mock the DB response
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = {
        "id": 1,
        "nom": nom_recette,
        "liste_ingredient": [["Pasta", "100"], ["Meat", "100"]],
    }
    mock_db_connection().connection.cursor.return_value.__enter__.return_value = mock_cursor

    recette_service = RecetteService()

    # WHEN
    result = recette_service.trouver_recette_par_nom(nom_recette)

    # THEN
    assert result == expected_recette
    mock_cursor.execute.assert_called_once_with(
        "SELECT * FROM Recette WHERE nom_recette = %(nom)s", {"nom": nom_recette}
    )


def test_trouver_recette_par_nom_invalid_input():
    # GIVEN
    nom_invalide = 4012

    # WHEN-THEN:
    with pytest.raises(
        TypeError, match="nom doit être une instance de str"
    ):
        RecetteService().trouver_recette_par_nom(nom_invalide)


# Test for trouver_recette_par_ingredient
@patch("services.recette_service.DBConnection")
def test_trouver_recette_par_ingredient(mock_db_connection):
    # GIVEN
    ingredient = "Tomato"
    expected_recettes = [
        Recette(
            id_recette=1,
            nom_recette="Spaghetti Bolognese",
            liste_ingredient=[["Pasta", "100"], ["Tomato", "100"]],
        ),
        Recette(
            id_recette=2,
            nom_recette="Pizza Margherita",
            liste_ingredient=[["Dough", "200"], ["Tomato", "50"], ["Cheese", "50"]],
        ),
    ]

    # Mock the DB response
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = [
        {
            "id": 1,
            "nom": "Spaghetti Bolognese",
            "liste_ingredient": [["Pasta", "100"], ["Tomato", "100"]],
        },
        {
            "id": 2,
            "nom": "Pizza Margherita",
            "liste_ingredient": [["Dough", "200"], ["Tomato", "50"], ["Cheese", "50"]],
        },
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


def test_trouver_recette_par_ingredient_invalid_input():
    """
    Recherche de Recette par Ingredient échouée car l'ingrédient n'est pas une instance
    de Ingredient
    """

    # GIVEN
    ingredient = ["nom_ingredient", 1]

    # WHEN-THEN:
    with pytest.raises(
        TypeError, match="ingredient doit être une instance de Ingredient"
    ):
        RecetteService().trouver_recette_par_ingredient(ingredient)


# Test for lister_toutes_recettes
@patch("services.recette_service.DBConnection")
def test_lister_toutes_recettes(mock_db_connection):
    # GIVEN
    expected_recettes = [
        Recette(
            id_recette=1,
            nom_recette="Spaghetti Bolognese",
            liste_ingredient=[["Pasta", "100"], ["Tomato", "100"]],
        ),
        Recette(
            id_recette=2,
            nom_recette="Pizza Margherita",
            liste_ingredient=[["Dough", "200"], ["Tomato", "50"], ["Cheese", "50"]],
        ),
    ]

    # Mock the DB response
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = [
        {
            "id": 1,
            "nom": "Spaghetti Bolognese",
            "liste_ingredient": [["Pasta", "100"], ["Tomato", "100"]],
        },
        {
            "id": 2,
            "nom": "Pizza Margherita",
            "liste_ingredient": [["Dough", "200"], ["Tomato", "50"], ["Cheese", "50"]],
        },
    ]
    mock_db_connection().connection.cursor.return_value.__enter__.return_value = mock_cursor

    recette_service = RecetteService()

    # WHEN
    result = recette_service.lister_toutes_recettes()

    # THEN
    assert result == expected_recettes
    mock_cursor.execute.assert_called_once_with("SELECT * FROM Recette")


def test_noter_recette(mock_db_connection):
    """
    bla

    Args:
        mock_db_connection (_type_): _description_
    """

    pass


def test_noter_recette_invalid_input_type():
    """
    Mise à jour de la note d'une recette échouée car la note n'est pas un flottant ou un entier
    """

    # GIVEN
    note = "4.5"

    # WHEN-THEN:
    with pytest.raises(
        TypeError, match="La note doit être un nombre compris entre 0 et 5."
    ):
        RecetteService().noter_recette(note)


def test_noter_recette(mock_db_connection):
    """
    bla

    Args:
        mock_db_connection (_type_): _description_
    """

    pass


def test_noter_recette_invalid_input_type():
    """
    Mise à jour de la note d'une recette échouée car la note n'est pas un flottant ou un entier
    """

    # GIVEN
    note = "4.5"

    # WHEN-THEN:
    with pytest.raises(
        TypeError, match="La note doit être un nombre compris entre 0 et 5."
    ):
        RecetteService().noter_recette(note)


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
