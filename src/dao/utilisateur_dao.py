import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

from business_object.utilisateur import Utilisateur


class UtilisateurDao(metaclass=Singleton):
    """
    Cette classe contient les méthodes qui permettent d'accéder aux utilisateurs de
    la base de données.
    """

    @log
    def creer(self, utilisateur) -> bool:
        """
        Cette méthode permet de créer un utilisateur dans la base de données.

        Parameters
        ----------
        utilisateur : Utilisateur
            Utilisateur que l'on souhaite créer

        Returns
        -------
        Bool
            True si la création est un succès, False sinon
        """

        res = None

        # Connexion à la base de données et commande SQL
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO utilisateur(pseudo, mdp, role_utilisateur) VALUES "
                        "( %(pseudo)s, %(mdp)s, %(role_utilisateur)s) "
                        "RETURNING id_utilisateur;",
                        {
                            "pseudo": utilisateur.pseudo,
                            "mdp": utilisateur.mdp,
                            "role_utilisateur": utilisateur.role,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise

        created = False
        # Retourne l'identifiant de l'utilisateur
        if res:
            utilisateur.id_utilisateur = res["id_utilisateur"]
            created = True
        return created

    @log
    def trouver_par_id(self, id_utilisateur) -> Utilisateur:
        """
        Cette méthode permet de trouver un utilisateur grâce à son identifiant.

        Parameters
        ----------
        id_utilisateur : int
            Identifiant de l'utilisateur

        Returns
        -------
        Utilisateur :
            Utilisateur que l'on souhaite trouver.

        """
        # Connexion à la base de données et commande SQL
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM utilisateur WHERE id_utilisateur = %(id_utilisateur)s;",
                        {"id_utilisateur": id_utilisateur},
                    )
                    res_utilisateur = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise

        utilisateur = None
        # Construction de l'utilisateur
        if res_utilisateur:
            utilisateur = Utilisateur(
                id_utilisateur=res_utilisateur["id_utilisateur"],
                pseudo=res_utilisateur["pseudo"],
                mdp=res_utilisateur["mdp"],
                role_utilisateur=res_utilisateur["role_utilisateur"],
            )

        return utilisateur

    @log
    def lister_tous(self) -> list[Utilisateur]:
        """
        Cette méthode permet de lister tous les utilisateurs de la base de données.

        Returns
        -------
        list[Utilisateur] :
            Liste de tous les utilisateurs de la base de données
        """
        # Connexion à la base de données et commande SQL
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT * FROM utilisateur;")
                    res_utilisateurs = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            print(e)
            raise

        # Initialisation de la liste
        liste_utilisateurs = []

        # Construction des utilisateurs et ajout à la liste
        if res_utilisateurs:
            for row in res_utilisateurs:
                utilisateur = Utilisateur(
                    id_utilisateur=row["id_utilisateur"],
                    pseudo=row["pseudo"],
                    mdp=row["mdp"],
                    role=row["role_utilisateur"],
                )
                liste_utilisateurs.append(utilisateur)

        return liste_utilisateurs

    @log
    def modifier(self, utilisateur) -> bool:
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
        res = None

        # Connexion à la base de données et commande SQL
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE utilisateur "
                        "SET pseudo = %(pseudo)s, "
                        "mdp = %(mdp)s, "
                        "role_utilisateur = %(role_utilisateur)s "
                        "WHERE id_utilisateur = %(id_utilisateur)s;",
                        {
                            "pseudo": utilisateur.pseudo,
                            "mdp": utilisateur.mdp,
                            "role_utilisateur": utilisateur.role,
                            "id_utilisateur": utilisateur.id_utilisateur,
                        },
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise

        return res == 1

    @log
    def supprimer(self, utilisateur: Utilisateur) -> bool:
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
        # Connexion à la base de données et commande SQL
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM utilisateur WHERE id_utilisateur = %(id_utilisateur)s;",
                        {"id_utilisateur": utilisateur.id_utilisateur},
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise

        return res > 0

    @log
    def se_connecter(self, pseudo, mdp) -> Utilisateur:
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
        # Connexion à la base de données et commande SQL
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM projet.utilisateur "
                        "WHERE pseudo = %(pseudo)s AND mdp = %(mdp)s;",
                        {"pseudo": pseudo, "mdp": mdp},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            print(e)
            raise

        utilisateur = None
        # Construction de l'utilisateur
        if res:
            utilisateur = Utilisateur(
                id_utilisateur=res["id_utilisateur"],
                pseudo=res["pseudo"],
                mdp=res["mdp"],
                role=res["role_utilisateur"],
            )

        return utilisateur
