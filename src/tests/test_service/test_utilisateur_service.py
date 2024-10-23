from unittest.mock import MagicMock
import pytest
from src.service.utilisateur_service import UtilisateurService
from src.dao.utilisateur_dao import UtilisateurDAO
from src.business_object.utilisateur import Utilisateur


liste_utilisateurs = [
    Utilisateur(pseudo="jp", mail="jp@mail.fr", mdp="1234"),
    Utilisateur(pseudo="lea", mail="lea@mail.fr", mdp="0000"),
    Utilisateur(pseudo="gg", mail="gg@mail.fr", mdp="abcd"),
]


def test_creer_ok():
    """ "Création de Utilisateur réussie"""

    # GIVEN
    pseudo, mdp, mail = "jp", "1234", "z@mail.oo"
    UtilisateurDAO().creer = MagicMock(return_value=True)

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


def test_creer_mauvais_pseudo():
    """Création de Utilisateur échoué car le pseudo n'est pas une chaine de
    caractère"""

    # GIVEN
    pseudo, mdp, mail = 123, "azerty", "az@gmail.fr"

    # WHEN-THEN:
    with pytest.raises(
        TypeError, match="Le pseudo doit être une chaîne de caractères alphanumériques."
    ):
        UtilisateurService().creer(pseudo, mdp, mail)


def test_creer_mauvais_mdp():
    """Création de Utilisateur échoué car le mot de passe n'est pas une chaine
    de caractère"""

    # GIVEN
    pseudo, mdp, mail = "michel", 123, "michel@gmail.fr"

    # WHEN-THEN:
    with pytest.raises(
        TypeError, match="Le mot de passe doit être une chaîne de caractères alphanumériques."
    ):
        UtilisateurService().creer(pseudo, mdp, mail)


def test_creer_mauvais_mail_str():
    """Création de Utilisateur échoué car le mail n'est pas une chaine de
    caractère"""

    # GIVEN
    pseudo, mdp, mail = "Michel", "azerty", ["az@gmail.fr"]

    # WHEN-THEN:
    with pytest.raises(
        TypeError,
        match="L'adresse mail doit être une chaîne de caractères sous la"
        " forme : 'blabla@domaine.truc'",
    ):
        UtilisateurService().creer(pseudo, mdp, mail)


def test_creer_mauvais_mdp_longueur():
    """Création de Utilisateur échoué car le mot de passe possède moins
    de 6 caractères"""

    # GIVEN
    pseudo, mdp, mail = "Michel", "azerty", "az@gmail.fr"

    # WHEN-THEN:
    with pytest.raises(
        ValueError,
        match="Le mot de passe doit contenir au moins 6 caractères.",
    ):
        UtilisateurService().creer(pseudo, mdp, mail)


def test_creer_mail_missing_arobase():
    """Création de Utilisateur échoué car il n'y a pas d'arobase dans le mail"""

    # GIVEN
    pseudo, mdp, mail = "Michel", "azerty", "azgmail.fr"

    # WHEN-THEN:
    with pytest.raises(
        ValueError,
        match="Il n'y a pas de @ dans l'adresse mail renseignée."
        "Format attendu : 'blabla@domaine.truc'",
    ):
        UtilisateurService().creer(pseudo, mdp, mail)


def test_creer_mail_trop_arobase():
    """Création de Utilisateur échoué car il y a trop d'arobase dans le mail"""

    # GIVEN
    pseudo, mdp, mail = "Michel", "azerty", "az@gm@il.fr"

    # WHEN-THEN:
    with pytest.raises(
        ValueError,
        match="Il ne doit y avoir qu'un seul @ dans votre adresse mail."
        "Format attendu : 'blabla@domaine.truc'",
    ):
        UtilisateurService().creer(pseudo, mdp, mail)


def test_creer_mail_pas_point():
    """Création de Utilisateur échoué car il n'y a pas de point dans le mail"""

    # GIVEN
    pseudo, mdp, mail = "Michel", "azerty", "az@gmailfr"

    # WHEN-THEN:
    with pytest.raises(
        ValueError,
        match="Il doit y avoir un '.' dans votre nom de domaine."
        "Format attendu : 'blabla@domaine.truc'",
    ):
        UtilisateurService().creer(pseudo, mdp, mail)


def test_creer_pseudo_inv_ap():
    """Création de Utilisateur échoué car le pseudo contient un élément
    interdit : '"""

    # GIVEN
    pseudo, mdp, mail = "Mi'chel", "azerty", "az@gmail.fr"

    # WHEN-THEN:
    with pytest.raises(
        ValueError,
        match="Le pseudo ne doit pas contenir de caractères spéciaux."
        "Caractères interdits : &, |, ', -",
    ):
        UtilisateurService().creer(pseudo, mdp, mail)


def test_creer_pseudo_inv_esp():
    """Création de Utilisateur échoué car le pseudo contient un élément
    interdit : &"""

    # GIVEN
    pseudo, mdp, mail = "Mi&chel", "azerty", "az@gmail.fr"

    # WHEN-THEN:
    with pytest.raises(
        ValueError,
        match="Le pseudo ne doit pas contenir de caractères spéciaux."
        "Caractères interdits : &, |, ', -",
    ):
        UtilisateurService().creer(pseudo, mdp, mail)


def test_creer_pseudo_inv_ba():
    """Création de Utilisateur échoué car le pseudo contient un élément
    interdit : |"""

    # GIVEN
    pseudo, mdp, mail = "Miche|", "azerty", "az@gmail.fr"

    # WHEN-THEN:
    with pytest.raises(
        ValueError,
        match="Le pseudo ne doit pas contenir de caractères spéciaux."
        "Caractères interdits : &, |, ', -",
    ):
        UtilisateurService().creer(pseudo, mdp, mail)


def test_creer_pseudo_inv_tir():
    """Création de Utilisateur échoué car le pseudo contient un élément
    interdit : -"""

    # GIVEN
    pseudo, mdp, mail = "Mi-chel", "azerty", "az@gmail.fr"

    # WHEN-THEN:
    with pytest.raises(
        ValueError,
        match="Le pseudo ne doit pas contenir de caractères spéciaux."
        "Caractères interdits : &, |, ', -",
    ):
        UtilisateurService().creer(pseudo, mdp, mail)


def test_creer_mdp_inv_ap():
    """Création de Utilisateur échoué car le mot de passe contient un élément
    interdit : '"""

    # GIVEN
    pseudo, mdp, mail = "Michel", "azer'ty", "az@gmail.fr"

    # WHEN-THEN:
    with pytest.raises(
        ValueError,
        match="Le mot de passe ne doit pas contenir de caractères spéciaux."
        "Caractères interdits : &, |, ', -",
    ):
        UtilisateurService().creer(pseudo, mdp, mail)


def test_creer_mdp_inv_esp():
    """Création de Utilisateur échoué car le mot de passe contient un élément
    interdit : &"""

    # GIVEN
    pseudo, mdp, mail = "Michel", "az&rty", "az@gmail.fr"

    # WHEN-THEN:
    with pytest.raises(
        ValueError,
        match="Le mot de passe ne doit pas contenir de caractères spéciaux."
        "Caractères interdits : &, |, ', -",
    ):
        UtilisateurService().creer(pseudo, mdp, mail)


def test_creer_mdp_inv_ba():
    """Création de Utilisateur échoué car le mot de passe contient un élément
    interdit : |"""

    # GIVEN
    pseudo, mdp, mail = "Michel", "azert|y", "az@gmail.fr"

    # WHEN-THEN:
    with pytest.raises(
        ValueError,
        match="Le mot de passe ne doit pas contenir de caractères spéciaux."
        "Caractères interdits : &, |, ', -",
    ):
        UtilisateurService().creer(pseudo, mdp, mail)


def test_creer_mdp_inv_ti():
    """Création de Utilisateur échoué car le mot de passe contient un élément
    interdit : -"""

    # GIVEN
    pseudo, mdp, mail = "Michel", "azert-y", "az@gmail.fr"

    # WHEN-THEN:
    with pytest.raises(
        ValueError,
        match="Le mot de passe ne doit pas contenir de caractères spéciaux."
        "Caractères interdits : &, |, ', -",
    ):
        UtilisateurService().creer(pseudo, mdp, mail)


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
    pseudo, mdp = "lea", "0000"
    utilisateur_mock = Utilisateur(pseudo=pseudo, mail="lea@mail.fr", mdp=mdp)
    UtilisateurDAO().connecter = MagicMock(return_value=utilisateur_mock)

    # WHEN
    utilisateur = UtilisateurService().connecter(pseudo, mdp)

    # THEN
    assert utilisateur.pseudo == pseudo
    assert utilisateur.mail == "lea@mail.fr"


def test_supprimer_ok():
    """La suppression de l'utilisateur a été correctement effectuée"""

    # GIVEN
    user = Utilisateur(pseudo="lea", mail="lea@mail.fr", mdp="0000")
    UtilisateurDAO().supprimer = MagicMock(return_value=True)

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

    # WHEN
    utilisateur = UtilisateurDAO().trouver_par_id(id_user)

    # THEN
    assert utilisateur is not None


def test_trouver_par_id_non_existant():
    """Recherche par id d'un utilisateur n'existant pas"""

    # GIVEN
    id_user = 9999999999999

    # WHEN
    utilisateur = UtilisateurDAO().trouver_par_id(id_user)

    # THEN
    assert utilisateur is None


def test_lister_tous():
    """Vérifie que la méthode renvoie une liste de Joueur
    de taille supérieure ou égale à 2
    """

    # GIVEN

    # WHEN
    utilisateurs = UtilisateurDAO().lister_tous()

    # THEN
    assert isinstance(utilisateurs, list)
    for j in utilisateurs:
        assert isinstance(j, Utilisateur)
    assert len(utilisateurs) >= 2


if __name__ == "__main__":

    pytest.main([__file__])
