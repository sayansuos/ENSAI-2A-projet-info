from unittest.mock import MagicMock

from src.classes.utilisateur_service import UtilisateurService

# from src.dao.utilisateur_dao import UtilisateurDAO

from src.classes.utilisateur import Utilisateur


liste_utilisateurs = [
    Utilisateur(pseudo="jp", mail="jp@mail.fr", mdp="1234"),
    Utilisateur(pseudo="lea", mail="lea@mail.fr", mdp="0000"),
    Utilisateur(pseudo="gg", mail="gg@mail.fr", mdp="abcd"),
]


def test_creer_ok():
    """ "Création de Utilisateur réussie"""

    # GIVEN
    pseudo, mdp, age, mail, fan_pokemon = "jp", "1234", 15, "z@mail.oo", True
    JoueurDao().creer = MagicMock(return_value=True)

    # WHEN
    joueur = JoueurService().creer(pseudo, mdp, age, mail, fan_pokemon)

    # THEN
    assert joueur.pseudo == pseudo


def test_creer_echec():
    """Création de Joueur échouée
    (car la méthode JoueurDao().creer retourne False)"""

    # GIVEN
    pseudo, mdp, age, mail, fan_pokemon = "jp", "1234", 15, "z@mail.oo", True
    JoueurDao().creer = MagicMock(return_value=False)

    # WHEN
    joueur = JoueurService().creer(pseudo, mdp, age, mail, fan_pokemon)

    # THEN
    assert joueur is None


def test_lister_tous_inclure_mdp_true():
    """Lister les Joueurs en incluant les mots de passe"""

    # GIVEN
    JoueurDao().lister_tous = MagicMock(return_value=liste_joueurs)

    # WHEN
    res = JoueurService().lister_tous(inclure_mdp=True)

    # THEN
    assert len(res) == 3
    for joueur in res:
        assert joueur.mdp is not None


def test_lister_tous_inclure_mdp_false():
    """Lister les Joueurs en excluant les mots de passe"""

    # GIVEN
    JoueurDao().lister_tous = MagicMock(return_value=liste_joueurs)

    # WHEN
    res = JoueurService().lister_tous()

    # THEN
    assert len(res) == 3
    for joueur in res:
        assert not joueur.mdp


def test_pseudo_deja_utilise_oui():
    """Le pseudo est déjà utilisé dans liste_joueurs"""

    # GIVEN
    pseudo = "lea"

    # WHEN
    JoueurDao().lister_tous = MagicMock(return_value=liste_joueurs)
    res = JoueurService().pseudo_deja_utilise(pseudo)

    # THEN
    assert res


def test_pseudo_deja_utilise_non():
    """Le pseudo n'est pas utilisé dans liste_joueurs"""

    # GIVEN
    pseudo = "chaton"

    # WHEN
    JoueurDao().lister_tous = MagicMock(return_value=liste_joueurs)
    res = JoueurService().pseudo_deja_utilise(pseudo)

    # THEN
    assert not res


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
