import pytest
from unittest.mock import patch, MagicMock

from service.recette_service import RecetteService
from business_object.recette import Recette
from business_object.ingredient import Ingredient
from dao.recette_dao import RecetteDao


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


def test_creer_recette_ok():
    """
    Vérifie que la recette crée est bien la recette renseignée dans les paramètres
    """

    # GIVEN
    ingredient_1 = Ingredient(nom_ingredient="Pasta", id_ingredient=1)
    ingredient_2 = Ingredient(nom_ingredient="Meat", id_ingredient=2)
    nom_recette = "Spaghetti Bolognese"
    expected_recette = Recette(
        nom_recette=nom_recette,
        liste_ingredient=[[ingredient_1, "100"], [ingredient_2, "100"]],
        description_recette="Spaghetti avec de la bolognaise",
    )

    RecetteDao().creer = MagicMock(return_value=True)

    # WHEN
    recette = RecetteService().creer_recette(expected_recette)

    # THEN
    assert recette == expected_recette


# Test for trouver_recette_par_nom
def test_trouver_recette_par_nom_ok():
    # GIVEN
    nom_recette = "Spaghetti Bolognese"

    # WHEN
    recette = RecetteDao().trouver_par_nom(nom_recette)

    # THEN
    assert recette is not None


def test_trouver_recette_par_nom_invalid_input():
    # GIVEN
    nom_invalide = 4012

    # WHEN-THEN:
    with pytest.raises(TypeError, match="nom doit être une instance de str"):
        RecetteService().trouver_recette_par_nom(nom_invalide)


def test_trouver_par_nom_non_existant():
    """Recherche par nom d'une recette n'existant pas"""

    # GIVEN
    nom_recette = "Pikachu"

    # WHEN
    recette = RecetteDao().trouver_par_nom(nom_recette)

    # THEN
    assert recette is None


# Test for trouver_recette_par_ingredient
def test_trouver_recette_par_ingredient_ok():
    # GIVEN
    ingredient = ingredient_1
    recette_mock = liste_recettes[1]

    # Utilisation de patch pour simuler la méthode trouver_par_id
    with patch("dao.recette_dao.trouver_par_ingredient", return_value=recette_mock):
        recette = RecetteDao().trouver_par_ingredient(ingredient)

    # THEN
    assert recette != []


def test_trouver_recette_par_ingredient_invalid_input():
    """
    Recherche de Recette par Ingredient échouée car l'ingrédient n'est pas une instance
    de Ingredient
    """

    # GIVEN
    ingredient = ["nom_ingredient", 1]

    # WHEN-THEN:
    with pytest.raises(TypeError, match="ingredient doit être une instance de Ingredient"):
        RecetteService().trouver_recette_par_ingredient(ingredient)


# Test for lister_toutes_recettes
def test_lister_toutes_recettes():
    """
    Vérifie que la méthode pour lister toutes les recettes de la base de données marche bien
    """
    # GIVEN

    # WHEN
    recettes = RecetteDao().lister_tous()

    # THEN
    assert isinstance(recettes, list)
    for recette in recettes:
        assert isinstance(recette, Recette)
    assert len(recettes) >= 2


def test_commenter_recette():
    # GIVEN
    recette = liste_recettes[1]
    note = 5
    commentaire = "avis positif"
    RecetteDao().ajouter_note_et_com = MagicMock(return_value=True)

    # WHEN
    RecetteService().ajouter_note_et_com(recette=recette, note=note, com=commentaire)

    # THEN
    assert True


def test_noter_recette_invalid_input_type():
    """
    Mise à jour de la note d'une recette échouée car la note n'est pas un flottant ou un entier
    """

    # GIVEN
    note = "4"

    # WHEN-THEN:
    with pytest.raises(TypeError, match="note doit être une instance de int."):
        RecetteService().ajouter_note_et_com(recette=liste_recettes[1], note=note, com="")


def test_noter_recette_invalid_input_value():
    """
    Mise à jour de la note d'une recette échouée car la note n'est pas comprise entre 0 et 5
    """

    # GIVEN
    note = 7

    # WHEN-THEN:
    with pytest.raises(ValueError, match="La note doit être comprise entre 0 et 5."):
        RecetteService().ajouter_note_et_com(recette=liste_recettes[1], note=note, com="bla")


def test_commenter_recette_invalid_input_type():
    """
    Ajout d'un commentaire d'une recette échoué car le commentaire n'est pas un str
    """

    # GIVEN
    commentaire = ["avis", "positif"]

    # WHEN-THEN:
    with pytest.raises(TypeError, match="com doit être une instance de str."):
        RecetteService().ajouter_note_et_com(recette=liste_recettes[1], note=5, com=commentaire)


def test_commenter_recette_invalid_input_value():
    """
    Ajout d'un commentaire d'une recette échoué car le commentaire contient un ";"
    """

    # GIVEN
    commentaire = "avis ; positif"

    # WHEN-THEN:
    with pytest.raises(ValueError, match="';' ne peut pas être utilisé dans le commentaire."):
        RecetteService().ajouter_note_et_com(recette=liste_recettes[1], note=5, com=commentaire)


if __name__ == "__main__":
    pytest.main([__file__])
