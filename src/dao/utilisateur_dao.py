import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

from business_object.utilisateur import Utilisateur
from business_object.recette import Recette
from business_object.ingredient import Ingredient


class UtilisateurDao(metaclass=Singleton):
    """Classe contenant les méthodes pour accéder aux utilisateurs de la base de données"""

    @log
    def creer(self, utilisateur) -> bool:
        """Creation d'un utilisateur dans la base de données

        Parameters
        ----------
        utilisateur : Utilisateur

        Returns
        -------
        created : bool
            True si la création est un succès
            False sinon
        """

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO utilisateur(id_utilisateur, pseudo, mdp, mail, role_utilisateur) VALUES       "
                        "(%(id_utilisateur)s, %(pseudo)s, %(mdp)s, %(mail)s, %(role_utilisateur)s)                              "
                        "  RETURNING id_utilisateur;                                                                ",
                        {
                            "id_utilisateur": utilisateur.id_utilisateur,
                            "pseudo": utilisateur.pseudo,
                            "mdp": utilisateur.mdp,
                            "mail": utilisateur.mail,
                            "role_utilisateur": utilisateur.role_utilisateur,
                        },
                    )
                    res = cursor.fetchone()

                    for recette in utilisateur.recette_favorite:
                        cursor.execute(
                            "INSERT INTO recette_favorite(id_utilisateur, id_recette) "
                            "VALUES (%(id_utilisateur)s, %(id_recette)s);",
                            {
                                "id_utilisateur": utilisateur.id_utilisateur,
                                "id_recette": recette.id_recette,
                            },
                        )

                    for ingredient in utilisateur.ingredient_favori:
                        cursor.execute(
                            "INSERT INTO preference_ingredient(id_utilisateur, id_ingredient, favori, non_desire) "
                            "VALUES (%(id_utilisateur)s, %(id_ingredient)s, TRUE, FALSE);",
                            {
                                "id_utilisateur": utilisateur.id_utilisateur,
                                "id_ingredient": ingredient.id_ingredient,
                            },
                        )

                    for ingredient in utilisateur.ingredient_non_desire:
                        cursor.execute(
                            "INSERT INTO preference_ingredient(id_utilisateur, id_ingredient, favori, non_desire) "
                            "VALUES (%(id_utilisateur)s, %(id_ingredient)s, FALSE, TRUE);",
                            {
                                "id_utilisateur": utilisateur.id_utilisateur,
                                "id_ingredient": ingredient.id_ingredient,
                            },
                        )

                    for course in utilisateur.liste_de_course:
                        cursor.execute(
                            "INSERT INTO liste_course(id_utilisateur, id_ingredient, id_recette) "
                            "VALUES (%(id_utilisateur)s, %(id_ingredient)s, %(id_recette)s);",
                            {
                                "id_utilisateur": utilisateur.id_utilisateur,
                                "id_ingredient": course["id_ingredient"],
                                "id_recette": course["id_recette"],
                            },
                        )
        except Exception as e:
            logging.info(e)
            raise

        created = False

        if res:
            utilisateur.id_utilisateur = res["id_utilisateur"]
            created = True

        return created

    @log
    def trouver_par_id(self, id_utilisateur) -> Utilisateur:
        """Trouver un utilisateur grâce à son ID.

        Parameters
        ----------
        id_utilisateur : int
            Numéro ID de l'utilisateur que l'on souhaite trouver.

        Returns
        -------
        utilisateur : Utilisateur
            Renvoie l'utilisateur que l'on cherche par ID.
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:

                    cursor.execute(
                        "SELECT * FROM utilisateur WHERE id_utilisateur = %(id_utilisateur)s;",
                        {"id_utilisateur": id_utilisateur},
                    )
                    res_utilisateur = cursor.fetchone()

                    utilisateur = None

                    if res_utilisateur:

                        utilisateur = Utilisateur(
                            id_utilisateur=res_utilisateur["id_utilisateur"],
                            pseudo=res_utilisateur["pseudo"],
                            mdp=res_utilisateur["mdp"],
                            mail=res_utilisateur["mail"],
                            recette_favorite=[],
                            ingredient_favori=[],
                            ingredient_non_desire=[],
                            liste_de_course=[],
                            role_utilisateur=res_utilisateur["role_utilisateur"],
                        )

                        cursor.execute(
                            "SELECT r.id_recette, r.nom "
                            "FROM recette_favorite rf "
                            "JOIN recette r ON rf.id_recette = r.id_recette "
                            "WHERE rf.id_utilisateur = %(id_utilisateur)s;",
                            {"id_utilisateur": id_utilisateur},
                        )
                        res_recettes = cursor.fetchall()

                        if res_recettes:
                            utilisateur.recette_favorite = [
                                Recette(id_recette=row["id_recette"], nom=row["nom"])
                                for row in res_recettes
                            ]

                        cursor.execute(
                            "SELECT pi.id_ingredient, i.nom, pi.favori, pi.non_desire "
                            "FROM preference_ingredient pi "
                            "JOIN ingredient i ON pi.id_ingredient = i.id_ingredient "
                            "WHERE pi.id_utilisateur = %(id_utilisateur)s;",
                            {"id_utilisateur": id_utilisateur},
                        )
                        res_ingredients = cursor.fetchall()

                        if res_ingredients:
                            for row in res_ingredients:
                                if row["favori"]:
                                    utilisateur.ingredient_favori.append(
                                        Ingredient(
                                            id_ingredient=row["id_ingredient"], nom=row["nom"]
                                        )
                                    )
                                if row["non_desire"]:
                                    utilisateur.ingredient_non_desire.append(
                                        Ingredient(
                                            id_ingredient=row["id_ingredient"], nom=row["nom"]
                                        )
                                    )

                        cursor.execute(
                            "SELECT id_ingredient, id_recette "
                            "FROM liste_course "
                            "WHERE id_utilisateur = %(id_utilisateur)s;",
                            {"id_utilisateur": id_utilisateur},
                        )
                        res_courses = cursor.fetchall()

                        if res_courses:
                            utilisateur.liste_de_course = [
                                {
                                    "id_ingredient": row["id_ingredient"],
                                    "id_recette": row["id_recette"],
                                }
                                for row in res_courses
                            ]

        except Exception as e:
            logging.info(e)
            raise

        return utilisateur

    @log
    def lister_tous(self) -> list[Utilisateur]:
        """Lister tous les utilisateurs.

        Parameters
        ----------
        None

        Returns
        -------
        liste_utilisateurs : list[Utilisateur]
            Renvoie la liste de tous les utilisateurs dans la base de données.
        """
        liste_utilisateurs = []

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT                                      *"
                        " FROM utilisateur                           ;"
                    )
                    res_utilisateurs = cursor.fetchall()

                    for row in res_utilisateurs:
                        utilisateur = Utilisateur(
                            id_utilisateur=row["id_utilisateur"],
                            pseudo=row["pseudo"],
                            mdp=row["mdp"],
                            mail=row["mail"],
                            role_utilisateur=row["role_utilisateur"],
                            recette_favorite=[],
                            ingredient_favori=[],
                            ingredient_non_desire=[],
                            liste_de_course=[],
                        )

                        cursor.execute(
                            "SELECT r.id_recette, r.nom "
                            "FROM recette_favorite rf "
                            "JOIN recette r ON rf.id_recette = r.id_recette "
                            "WHERE rf.id_utilisateur = %(id_utilisateur)s;",
                            {"id_utilisateur": utilisateur.id_utilisateur},
                        )
                        res_recettes = cursor.fetchall()

                        if res_recettes:
                            utilisateur.recette_favorite = [
                                Recette(id_recette=row["id_recette"], nom=row["nom"])
                                for row in res_recettes
                            ]

                        cursor.execute(
                            "SELECT pi.id_ingredient, i.nom, pi.favori, pi.non_desire "
                            "FROM preference_ingredient pi "
                            "JOIN ingredient i ON pi.id_ingredient = i.id_ingredient "
                            "WHERE pi.id_utilisateur = %(id_utilisateur)s;",
                            {"id_utilisateur": utilisateur.id_utilisateur},
                        )
                        res_ingredients = cursor.fetchall()

                        if res_ingredients:
                            for row in res_ingredients:
                                if row["favori"]:
                                    utilisateur.ingredient_favori.append(
                                        Ingredient(
                                            id_ingredient=row["id_ingredient"], nom=row["nom"]
                                        )
                                    )
                                if row["non_desire"]:
                                    utilisateur.ingredient_non_desire.append(
                                        Ingredient(
                                            id_ingredient=row["id_ingredient"], nom=row["nom"]
                                        )
                                    )

                        cursor.execute(
                            "SELECT id_ingredient, id_recette "
                            "FROM liste_course "
                            "WHERE id_utilisateur = %(id_utilisateur)s;",
                            {"id_utilisateur": utilisateur.id_utilisateur},
                        )
                        res_courses = cursor.fetchall()

                        if res_courses:
                            utilisateur.liste_de_course = [
                                {
                                    "id_ingredient": row["id_ingredient"],
                                    "id_recette": row["id_recette"],
                                }
                                for row in res_courses
                            ]

                        liste_utilisateurs.append(utilisateur)

        except Exception as e:
            logging.info(e)
            raise

        return liste_utilisateurs

    @log
    def modifier_utilisateur(self, utilisateur) -> bool:
        """Modification d'un utilisateur dans la base de données.

        Parameters
        ----------
        utilisateur : Utilisateur

        Returns
        -------
        bool
            True si la modification est un succès, False sinon.
        """

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE utilisateur                                      "
                        "   SET pseudo      = %(pseudo)s,                       "
                        "       mdp         = %(mdp)s,                          "
                        "       mail        = %(mail)s,                         "
                        "       role_utilisateur        = %(role_utilisateur)s                          "
                        " WHERE id_utilisateur = %(id_utilisateur)s;            ",
                        {
                            "pseudo": utilisateur.pseudo,
                            "mdp": utilisateur.mdp,
                            "mail": utilisateur.mail,
                            "role_utilisateur": utilisateur.role_utilisateur,
                            "id_utilisateur": utilisateur.id_utilisateur,
                        },
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise

        return res == 1

    @log
    def supprimer_utilisateur(self, id_utilisateur) -> bool:
        """
        Suppression d'un utilisateur dans la base de données.

        Parameters
        ----------
        id_utilisateur : int
            ID de l'utilisateur à supprimer de la base de données.

        Returns
        -------
        bool
            True si l'utilisateur a bien été supprimé, False sinon.
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM utilisateur " "WHERE id_utilisateur = %(id_utilisateur)s;",
                        {"id_utilisateur": id_utilisateur},
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise

        return res > 0

    @log
    def se_connecter(self, pseudo, mdp) -> Utilisateur:
        """Se connecter grâce à son pseudo et son mot de passe.

        Parameters
        ----------
        pseudo : str
            Pseudo de l'utilisateur que l'on souhaite trouver.
        mdp : str
            Mot de passe de l'utilisateur.

        Returns
        -------
        Utilisateur
            Renvoie l'utilisateur que l'on cherche, ou None si la connexion échoue.
        """
        res = None
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                           "
                        " FROM utilisateur                   "
                        " WHERE pseudo = %(pseudo)s         "
                        "   AND mdp = %(mdp)s;              ",
                        {"pseudo": pseudo, "mdp": mdp},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise

        utilisateur = None

        if res:
            utilisateur = Utilisateur(
                id_utilisateur=res["id_utilisateur"],
                pseudo=res["pseudo"],
                mdp=res["mdp"],
                mail=res["mail"],
                role_utilisateur=res["role_utilisateur"],
                recette_favorite=[],
                ingredient_favori=[],
                ingredient_non_desire=[],
                liste_de_course=[],
            )

        return utilisateur
