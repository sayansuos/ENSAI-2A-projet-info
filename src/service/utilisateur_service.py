from business_object.utilisateur import Utilisateur
from dao.utilisateur_dao import UtilisateurDao
import re

from utils.log_decorator import log
from utils.securite import hash_password
from typing import List, Optional


class UtilisateurService:
    """
    Définis les méthodes de la classe Utilisateur
    """

    @log
    def pseudo_deja_utilise(self, pseudo: str) -> bool:
        """
        Vérifie si le pseudo entré est déjà utilisé dans la base de données.

        Args:
            pseudo (str): Pseudo voulu par l'utilisateur

        Returns:
            bool: True si le pseudo est déjà utilisé. False sinon
        """
        utilisateurs = UtilisateurDao().lister_tous()
        return pseudo in [i.pseudo for i in utilisateurs]

    @log
    def creer(self, pseudo: str, mdp: str) -> Utilisateur:
        """
        Cette méthode permet de créer un utilisateur dans la base de données.

        Parameters
        ----------
        pseudo : str
            Pseudo de l'utilisateur
        mdp : str
            Mot de passe de l'utilisateur

        Returns
        -------
        Utilisateur :
            Nouvel utilisateur créé
        """
        # Vérification des attributs
        if not isinstance(pseudo, str):
            raise TypeError("Le pseudo doit être une chaîne de caractères.")
        if not isinstance(mdp, str):
            raise TypeError("Le mot de passe doit être une chaîne de caractères.")
        if len(mdp) < 6:
            raise ValueError("Le mot de passe doit contenir au moins 6 caractères.")
        if re.search(r"[&\'| -]", pseudo):
            raise ValueError(
                "Le pseudo ne doit pas contenir de caractères spéciaux."
                " Caractères interdits : &, |, ', -"
            )
        if re.search(r"[&\'| -]", mdp):
            raise ValueError(
                "Le mot de passe ne doit pas contenir de caractères spéciaux."
                " Caractères interdits : &, |, ', -"
            )
        if self.pseudo_deja_utilise(pseudo):
            raise ValueError("Le pseudo est déjà utilisé")
        # Obtention du mdp haché
        mdp = hash_password(mdp, sel=pseudo)
        utilisateur = Utilisateur(pseudo=pseudo, mdp=mdp)
        # Appel à la DAO
        UtilisateurDao().creer(utilisateur)
        return utilisateur

    @log
    def connecter(self, pseudo: str, mdp: str) -> Utilisateur:
        """
        Cette méthode permet à l'utilisateur de se connecter grâce à son pseudo et son mot de passe.

        Parameters
        ----------
        pseudo : str
            Pseudo de l'utilisateur
        mdp : str
            Mot de passe de l'utilisateur

        Returns
        -------
        Utilisateur :
            Renvoie l'utilisateur que l'on cherche, ou None si la connexion échoue.

        """
        # Vérification des attributs
        if not isinstance(pseudo, str):
            raise TypeError("Le pseudo doit être une chaîne de caractères alphanumériques.")
        if not isinstance(mdp, str):
            raise TypeError("Le mot de passe doit être une chaîne de caractères alphanumériques.")
        # Appel à la DAO
        return UtilisateurDao().se_connecter(pseudo, hash_password(mdp, pseudo))

    @log
    def supprimer(self, user: Utilisateur) -> bool:
        """
        Cette méthode permet de supprimer un utilisateur de la base de données.

        Parameters
        ----------
        utilisateur : Utilisateur
            Utilisateur que l'on souhaite supprimer

        Returns
        -------
        bool
            True si l'utilisateur a bien été supprimé, False sinon.

        """
        # Vérification des attributs
        if not isinstance(user, Utilisateur):
            raise TypeError("L'utilisateur n'est pas renseigné correctement.")

        # Appel à la DAO
        return UtilisateurDao().supprimer(user)

    @log
    def lister_tous(self, inclure_mdp=False) -> List[Utilisateur]:
        """
        Cette méthode permet de lister tous les utilisateurs de la base de données.

        Parameters
        ----------
        inclure_mdp : Bool
            True si le mot de passe est inclu, False sinon
            False par défaut

        Returns
        -------
        list[Utilisateur] :
            Liste de tous les utilisateurs de la base de données
        """
        # Appel à la DAO
        utilisateurs = UtilisateurDao().lister_tous()
        if not inclure_mdp:
            for u in utilisateurs:
                u.mdp = None
        return utilisateurs

    @log
    def trouver_par_id(self, id_user: int) -> Optional[Utilisateur]:
        """
        Cette méthode permet de trouver un utilisateur grâce à son identifiant.

        Parameters
        ----------
        id_user : int
            Identifiant de l'utilisateur

        Returns
        -------
        Utilisateur :
            Utilisateur que l'on souhaite trouver.

        """
        # Vérification des attributs
        if not isinstance(id_user, int):
            raise TypeError("id_user doit être une instance de str")
        # Appel à la DAO
        return UtilisateurDao().trouver_par_id(id_user)

    @log
    def modifier(self, user: Utilisateur) -> Optional[Utilisateur]:
        """
        Cette méthode permet de modifier un utilisateur dans la base de données.

        Parameters
        ----------
        utilisateur : Utilisateur
            Utilisateur que l'on souhaite modifier

        Returns
        -------
        bool
            True si la modification est un succès, False sinon.
        """
        # Hachage du mot de passe
        user.mdp = hash_password(user.mdp, user.pseudo)
        # Appel à la DAO
        return user if UtilisateurDao().modifier(user) else None
