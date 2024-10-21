from unittest.mock import MagicMock

from src.classes.utilisateur_service import UtilisateurService

from src.dao.utilisateur_dao import UtilisateurDAO

from src.classes.utilisateur import Utilisateur


liste_utilisateurs = [
    Utilisateur(pseudo="jp", mail="jp@mail.fr", mdp="1234"),
    Utilisateur(pseudo="lea", mail="lea@mail.fr", mdp="0000"),
    Utilisateur(pseudo="gg", mail="gg@mail.fr", mdp="abcd"),
]


def test_creer_ok():
    """ "Création de Utilisateur réussie"""

    # GIVEN
    pseudo, mdp, mail = "jp", "1234", "z@mail.oo"
    UtilsateurDAO().creer = MagicMock(return_value=True)

    # WHEN
    utilisateur = UtilisateurService().creer(pseudo, mdp, mail)

    # THEN
    assert utilisateur.pseudo == pseudo


def test_creer_echec():
    """Création de Utilisateur échouée
    (car la méthode UtilisateurDAO().creer retourne False)"""

    # GIVEN
    pseudo, mdp, mail = "jp", "1234", "z@mail.oo"
    UtilisateurDAO().creer = MagicMock(return_value=False)

    # WHEN
    utilisateur = UtilisateurService().creer(pseudo, mdp, mail)

    # THEN
    assert utilisateur is None


def test_lister_tous_inclure_mdp_true():
    """Lister les Joueurs en incluant les mots de passe"""

    # GIVEN
    UtilisateurDAO().lister_tous = MagicMock(return_value=liste_utilisateurs)

    # WHEN
    res = UtilisateurService().lister_tous(inclure_mdp=True)

    # THEN
    assert len(res) == 3
    for utilisateur in res:
        assert utilisateur.mdp is not None


def test_lister_tous_inclure_mdp_false():
    """Lister les Utilisateurs en excluant les mots de passe"""

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
