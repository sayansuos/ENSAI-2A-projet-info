from unittest.mock import MagicMock
from unittest.mock import patch
import pytest
from service.utilisateur_service import UtilisateurService
from dao.utilisateur_dao import UtilisateurDao
from business_object.utilisateur import Utilisateur


liste_utilisateurs = [
    Utilisateur(pseudo="jp", mdp="123456"),
    Utilisateur(pseudo="lea", mdp="000000"),
    Utilisateur(pseudo="gg", mdp="abcdef"),
]


def test_creer_ok():
    """ "Création de Utilisateur réussie"""

    # GIVEN
    pseudo, mdp = "jp", "123456"
    UtilisateurDao().creer = MagicMock(return_value=True)

    # WHEN
    UtilisateurService().creer(pseudo, mdp)

    # THEN
    assert True


def test_creer_mauvais_pseudo():
    """Création de Utilisateur échoué car le pseudo n'est pas une chaine de
    caractère"""

    # GIVEN
    pseudo, mdp = 123, "azerty"

    # WHEN-THEN:
    with pytest.raises(TypeError, match="Le pseudo doit être une chaîne de caractères."):
        UtilisateurService().creer(pseudo, mdp)


def test_creer_mauvais_mdp():
    """Création de Utilisateur échoué car le mot de passe n'est pas une chaine
    de caractère"""

    # GIVEN
    pseudo, mdp = "michel", 123

    # WHEN-THEN:
    with pytest.raises(TypeError, match="Le mot de passe doit être une chaîne de caractères."):
        UtilisateurService().creer(pseudo, mdp)


def test_creer_mauvais_mdp_longueur():
    """Création de Utilisateur échoué car le mot de passe possède moins
    de 6 caractères"""

    # GIVEN
    pseudo, mdp = "Michel", "azer"

    # WHEN-THEN:
    with pytest.raises(
        ValueError,
        match="Le mot de passe doit contenir au moins 6 caractères.",
    ):
        UtilisateurService().creer(pseudo, mdp)


def test_creer_pseudo_inv_ap():
    """Création de Utilisateur échoué car le pseudo contient un élément
    interdit : '"""

    # GIVEN
    pseudo, mdp = "Mi'chel", "azerty"

    # WHEN-THEN:
    with pytest.raises(
        ValueError,
        match="Le pseudo ne doit pas contenir de caractères spéciaux."
        "Caractères interdits : &, |, ', -",
    ):
        UtilisateurService().creer(pseudo, mdp)


def test_creer_pseudo_inv_esp():
    """Création de Utilisateur échoué car le pseudo contient un élément
    interdit : &"""

    # GIVEN
    pseudo, mdp = "Mi&chel", "azerty"

    # WHEN-THEN:
    with pytest.raises(
        ValueError,
        match="Le pseudo ne doit pas contenir de caractères spéciaux."
        "Caractères interdits : &, |, ', -",
    ):
        UtilisateurService().creer(pseudo, mdp)


def test_creer_pseudo_inv_ba():
    """Création de Utilisateur échoué car le pseudo contient un élément
    interdit : |"""

    # GIVEN
    pseudo, mdp = "Miche|", "azerty"

    # WHEN-THEN:
    with pytest.raises(
        ValueError,
        match="Le pseudo ne doit pas contenir de caractères spéciaux."
        "Caractères interdits : &, |, ', -",
    ):
        UtilisateurService().creer(pseudo, mdp)


def test_creer_pseudo_inv_tir():
    """Création de Utilisateur échoué car le pseudo contient un élément
    interdit : -"""

    # GIVEN
    pseudo, mdp = "Mi-chel", "azerty"

    # WHEN-THEN:
    with pytest.raises(
        ValueError,
        match="Le pseudo ne doit pas contenir de caractères spéciaux."
        "Caractères interdits : &, |, ', -",
    ):
        UtilisateurService().creer(pseudo, mdp)


def test_creer_mdp_inv_ap():
    """Création de Utilisateur échoué car le mot de passe contient un élément
    interdit : '"""

    # GIVEN
    pseudo, mdp = "Michel", "azer'ty"

    # WHEN-THEN:
    with pytest.raises(
        ValueError,
        match="Le mot de passe ne doit pas contenir de caractères spéciaux."
        "Caractères interdits : &, |, ', -",
    ):
        UtilisateurService().creer(pseudo, mdp)


def test_creer_mdp_inv_esp():
    """Création de Utilisateur échoué car le mot de passe contient un élément
    interdit : &"""

    # GIVEN
    pseudo, mdp = "Michel", "az&rty"

    # WHEN-THEN:
    with pytest.raises(
        ValueError,
        match="Le mot de passe ne doit pas contenir de caractères spéciaux."
        "Caractères interdits : &, |, ', -",
    ):
        UtilisateurService().creer(pseudo, mdp)


def test_creer_mdp_inv_ba():
    """Création de Utilisateur échoué car le mot de passe contient un élément
    interdit : |"""

    # GIVEN
    pseudo, mdp = "Michel", "azert|y"

    # WHEN-THEN:
    with pytest.raises(
        ValueError,
        match="Le mot de passe ne doit pas contenir de caractères spéciaux."
        "Caractères interdits : &, |, ', -",
    ):
        UtilisateurService().creer(pseudo, mdp)


def test_creer_mdp_inv_ti():
    """Création de Utilisateur échoué car le mot de passe contient un élément
    interdit : -"""

    # GIVEN
    pseudo, mdp = "Michel", "azert-y"

    # WHEN-THEN:
    with pytest.raises(
        ValueError,
        match="Le mot de passe ne doit pas contenir de caractères spéciaux."
        "Caractères interdits : &, |, ', -",
    ):
        UtilisateurService().creer(pseudo, mdp)


def test_pseudo_deja_utilise_oui():
    """Le pseudo est déjà utilisé dans liste_utilisateurs"""

    # GIVEN
    pseudo = "lea"

    # WHEN
    UtilisateurDao().lister_tous = MagicMock(return_value=liste_utilisateurs)
    res = UtilisateurService().pseudo_deja_utilise(pseudo)

    # THEN
    assert res


def test_pseudo_deja_utilise_non():
    """Le pseudo n'est pas utilisé dans liste_utilisateurs"""

    # GIVEN
    pseudo = "chaton"

    # WHEN
    UtilisateurDao().lister_tous = MagicMock(return_value=liste_utilisateurs)
    res = UtilisateurService().pseudo_deja_utilise(pseudo)

    # THEN
    assert not res


def test_connecter_pseudo_inv():
    """Connection échouée car le pseudo n'est pas une chaine de caractère"""

    # GIVEN
    pseudo, mdp = 123, "azerty"

    # WHEN - THEN
    with pytest.raises(
        TypeError,
        match="Le pseudo doit être une chaîne de caractères alphanumériques.",
    ):
        UtilisateurService().connecter(pseudo, mdp)


def test_connecter_mdp_inv():
    """Connection échoué car le mot de passe n'est pas une chaine de caractère"""

    # GIVEN
    pseudo, mdp = "Benjamin", ["azerty"]

    # WHEN - THEN
    with pytest.raises(
        TypeError,
        match="Le mot de passe doit être une chaîne de caractères alphanumériques.",
    ):
        UtilisateurService().connecter(pseudo, mdp)


def test_connecter_ok():
    """Connection de l'utilisateur réussie"""

    # GIVEN
    pseudo, mdp = "lea", "000000"
    utilisateur_mock = Utilisateur(pseudo=pseudo, mdp=mdp)

    with patch("dao.utilisateur_dao.UtilisateurDao.se_connecter", return_value=utilisateur_mock):
        utilisateur = UtilisateurService().connecter(pseudo, mdp)

    # THEN
    assert utilisateur.pseudo == pseudo


def test_supprimer_ok():
    """La suppression de l'utilisateur a été correctement effectuée"""

    # GIVEN
    user = Utilisateur(pseudo="lea", mdp="000000")
    UtilisateurDao().supprimer = MagicMock(return_value=True)

    # WHEN
    result = UtilisateurService().supprimer(user)

    # THEN
    assert result


def test_supprimer_echec():
    """La suppression de l'utilisateur n'a pas été effectué car user n'est pas
    une instance de Utilisateur"""

    # GIVEN
    user = "lea"

    # WHEN - THEN
    with pytest.raises(
        TypeError,
        match="L'utilisateur n'est pas renseigné correctement.",
    ):
        UtilisateurService().supprimer(user)


def test_trouver_par_id_existant():
    """Recherche par id d'un utilisateur existant"""

    # GIVEN
    id_user = 998
    utilisateur_mock = Utilisateur(pseudo="test_user", mdp="password")

    # Utilisation de patch pour simuler la méthode trouver_par_id
    with patch("dao.utilisateur_dao.UtilisateurDao.trouver_par_id", return_value=utilisateur_mock):
        utilisateur = UtilisateurDao().trouver_par_id(id_user)

    # THEN
    assert utilisateur is not None


def test_trouver_par_id_non_existant():
    """Recherche par id d'un utilisateur n'existant pas"""

    # GIVEN
    id_user = 9999999999999

    # WHEN
    utilisateur = UtilisateurDao().trouver_par_id(id_user)

    # THEN
    assert utilisateur is None


def test_lister_tous():
    """Vérifie que la méthode renvoie une liste de Joueur
    de taille supérieure ou égale à 2
    """

    # GIVEN

    # WHEN
    utilisateurs = UtilisateurDao().lister_tous()

    # THEN
    assert isinstance(utilisateurs, list)
    for j in utilisateurs:
        assert isinstance(j, Utilisateur)
    assert len(utilisateurs) >= 2


if __name__ == "__main__":

    pytest.main([__file__])
