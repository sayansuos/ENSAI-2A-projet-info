from unittest.mock import MagicMock

from src.classes.recette import Recette


def test_recette_ok():
    """ Création de Utilisateur réussie"""

    # GIVEN
    id_recette, nom_recette, liste_ingredient = 1, "riz au curry", [["riz", "100"], ["curry", "50"]]

    # WHEN
    utilisateur = UtilisateurService().creer(pseudo, mdp, mail)

    # THEN
    assert utilisateur.pseudo == pseudo


def test_creer_echec():
    """Création de Joueur échouée
    (car la méthode JoueurDao().creer retourne False)"""

    # GIVEN
    pseudo, mdp, mail = "jp", "1234" "z@mail.oo"
    UtilisateurDAO().creer = MagicMock(return_value=False)

    # WHEN
    utilisateur = UtilisateurService().creer(pseudo, mdp, age, mail, fan_pokemon)

    # THEN
    assert utilisateur is None


def test_lister_tous_inclure_mdp_true():
    """Lister les Utilisateurs en incluant les mots de passe"""

    # GIVEN
    UtilisateurDAO().lister_tous = MagicMock(return_value=liste_utilisateurs)

    # WHEN
    res = UtilisateurService().lister_tous(inclure_mdp=True)

    # THEN
    assert len(res) == 3
    for utilisateur in res:
        assert utilisateur.mdp is not None


def test_lister_tous_inclure_mdp_false():
    """Lister les Joueurs en excluant les mots de passe"""

    # GIVEN
    UtilisateurDAO().lister_tous = MagicMock(return_value=liste_utilisateurs)

    # WHEN
    res = UtilisateurService().lister_tous()

    # THEN
    assert len(res) == 3
    for utilisateur in res:
        assert not utilisateur.mdp


def test_pseudo_deja_utilise_oui():
    """Le pseudo est déjà utilisé dans liste_utilisateurs"""

    # GIVEN
    pseudo = "lea"

    # WHEN
    UtilisateurDAO().lister_tous = MagicMock(return_value=liste_utilisateurs)
    res = UtilisateurService().pseudo_deja_utilise(pseudo)

    # THEN
    assert res


def test_pseudo_deja_utilise_non():
    """Le pseudo n'est pas utilisé dans liste_utilisateurs"""

    # GIVEN
    pseudo = "chaton"

    # WHEN
    UtilisateurDAO().lister_tous = MagicMock(return_value=liste_utilisateurs)
    res = UtilisateurService().pseudo_deja_utilise(pseudo)

    # THEN
    assert not res


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
