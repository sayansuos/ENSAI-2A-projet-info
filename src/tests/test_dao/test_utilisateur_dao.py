import os
import pytest
from unittest.mock import patch
from utils.reset_database import ResetDatabase
from utils.securite import hash_password
from src.dao.utilisateur_dao import UtilisateurDao
from src.business_object.utilisateur import Utilisateur


@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    """Initialisation des données de test"""
    with patch.dict(os.environ, {"SCHEMA": "projet_test_dao"}):
        ResetDatabase().lancer(test_dao=True)
        yield


def test_trouver_par_id_existant():
    """Recherche par id d'un utilisateur existant"""

    # GIVEN
    id_utilisateur = 1

    # WHEN
    utilisateur = UtilisateurDao().trouver_par_id(id_utilisateur)

    # THEN
    assert utilisateur is not None


def test_trouver_par_id_non_existant():
    """Recherche par id d'un utilisateur n'existant pas"""

    # GIVEN
    id_utilisateur = 9999999999999

    # WHEN
    utilisateur = UtilisateurDao().trouver_par_id(id_utilisateur)

    # THEN
    assert utilisateur is None


def test_trouver_par_pseudo_existant():
    """Recherche par pseudo d'un utilisateur existant"""

    # GIVEN
    pseudo = "miguel"

    # WHEN
    utilisateur = UtilisateurDao().trouver_par_pseudo(pseudo)

    # THEN
    assert utilisateur is not None


def test_trouver_par_pseudo_non_existant():
    """Recherche par pseudo d'un utilisateur n'existant pas"""

    # GIVEN
    pseudo = "unknownuser"

    # WHEN
    utilisateur = UtilisateurDao().trouver_par_pseudo(pseudo)

    # THEN
    assert utilisateur is None


def test_lister_tous():
    """Vérifie que la méthode renvoie une liste d'Utilisateurs
    de taille supérieure ou égale à 2
    """

    # WHEN
    utilisateurs = UtilisateurDao().lister_tous()

    # THEN
    assert isinstance(utilisateurs, list)
    for u in utilisateurs:
        assert isinstance(u, Utilisateur)
    assert len(utilisateurs) >= 2


def test_creer_ok():
    """Création d'un Utilisateur réussie"""

    # GIVEN
    utilisateur = Utilisateur(
        pseudo="newuser", mdp="newpass", mail="new@test.io", role_utilisateur="user"
    )

    # WHEN
    creation_ok = UtilisateurDao().creer(utilisateur)

    # THEN
    assert creation_ok
    assert utilisateur.id_utilisateur


def test_creer_ko_email_invalide():
    """Création d'un Utilisateur échouée (email invalide)"""

    # GIVEN
    utilisateur = Utilisateur(
        pseudo="newuser", mdp="newpass", mail="notanemail", role_utilisateur="user"
    )

    # WHEN
    creation_ok = UtilisateurDao().creer(utilisateur)

    # THEN
    assert not creation_ok


def test_creer_ko_pseudo_deja_utilise():
    """Création d'un Utilisateur échouée (pseudo déjà utilisé)"""

    # GIVEN
    utilisateur_existant = Utilisateur(
        pseudo="testuser", mdp="testpass", mail="test@test.io", role_utilisateur="user"
    )
    UtilisateurDao().creer(utilisateur_existant)
    nouvel_utilisateur = Utilisateur(
        pseudo="testuser", mdp="newpass", mail="new@test.io", role_utilisateur="user"
    )

    # WHEN
    creation_ok = UtilisateurDao().creer(nouvel_utilisateur)

    # THEN
    assert not creation_ok


def test_modifier_ok():
    """Modification d'un Utilisateur réussie"""

    # GIVEN
    new_mail = "modified_email@test.com"
    utilisateur = Utilisateur(
        id_utilisateur=1, pseudo="testuser", mdp="testpass", mail=new_mail, role_utilisateur="user"
    )

    # WHEN
    modification_ok = UtilisateurDao().modifier_utilisateur(utilisateur)

    # THEN
    assert modification_ok


def test_modifier_ko():
    """Modification d'un Utilisateur échouée (id inconnu)"""

    # GIVEN
    utilisateur = Utilisateur(
        id_utilisateur=9999,
        pseudo="unknown",
        mdp="testpass",
        mail="no@mail.com",
        role_utilisateur="user",
    )

    # WHEN
    modification_ok = UtilisateurDao().modifier_utilisateur(utilisateur)

    # THEN
    assert not modification_ok


def test_supprimer_ok():
    """Suppression d'un Utilisateur réussie"""

    # GIVEN
    utilisateur = Utilisateur(
        id_utilisateur=1,
        pseudo="testuser",
        mdp="testpass",
        mail="test@test.io",
        role_utilisateur="user",
    )

    # WHEN
    suppression_ok = UtilisateurDao().supprimer_utilisateur(utilisateur.id_utilisateur)

    # THEN
    assert suppression_ok


def test_supprimer_ko():
    """Suppression d'un Utilisateur échouée (id inconnu)"""

    # GIVEN
    id_inconnu = 99999999

    # WHEN
    suppression_ok = UtilisateurDao().supprimer_utilisateur(id_inconnu)

    # THEN
    assert not suppression_ok


def test_se_connecter_ok():
    """Connexion d'un Utilisateur réussie"""

    # GIVEN
    pseudo = "testuser"
    mdp = "testpass"

    # WHEN
    utilisateur = UtilisateurDao().se_connecter(pseudo, hash_password(mdp, pseudo))

    # THEN
    assert isinstance(utilisateur, Utilisateur)


def test_se_connecter_ko():
    """Connexion d'un Utilisateur échouée (pseudo ou mdp incorrect)"""

    # GIVEN
    pseudo = "unknownuser"
    mdp = "wrongpassword"

    # WHEN
    utilisateur = UtilisateurDao().se_connecter(pseudo, hash_password(mdp, pseudo))

    # THEN
    assert not utilisateur


if __name__ == "__main__":
    pytest.main([__file__])
