import logging
from dotenv import load_dotenv

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

from dao.recette_dao import RecetteDao
from dao.ingredient_dao import IngredientDao
from business_object.ingredient import Ingredient
from business_object.recette import Recette
from business_object.utilisateur import Utilisateur


class ListeFavorisDao(metaclass=Singleton):
    """
    Classe contenant les méthodes pour accéder accéder aux tables d'associations entre utilisateurs
    et recette et/ou ingrédient.
    """

    @log
    def est_dans_favoris(self, recette: Recette, utilisateur: Utilisateur) -> bool:
        """
        Cette méthode vérifie si une recette appartient aux favoris d'un utilisateur.

        Parameters
        ----------
        recette : Recette
            Recette à tester
        utilisateur : Utilisateur
            Utilisateur à tester

        Returns
        -------
        bool :
            True si la recette est dans les favoris de l'utilisateur, False sinon

        """
        res = None

        # Connexion à la base de données et commande SQL
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                                  "
                        "  FROM recette_favorite                   "
                        " WHERE id_utilisateur=%(id_utilisateur)s; ",
                        {"id_utilisateur": utilisateur.id_utilisateur},
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise

        est_dans_favoris = False
        for row in res:
            if recette.id_recette == row["id_recette"]:
                est_dans_favoris = True

        return est_dans_favoris

    @log
    def consulter_favoris(self, utilisateur: Utilisateur) -> list[Recette]:
        """
        Cette méthode renvoie la liste des recettes favorites de l'utilisateur.

        Parameters
        ----------
        utilisateur : Utilisateur
            Utilisateur à tester

        Returns
        -------
        list[Recette] :
            Liste des recettes favorites de l'utilisateur

        """
        res = None
        # Connexion à la base de données et commande SQL
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                                    "
                        "  FROM recette_favorite                     "
                        " WHERE id_utilisateur = %(id_utilisateur)s; ",
                        {"id_utilisateur": utilisateur.id_utilisateur},
                    )
                    res = cursor.fetchall()

        except Exception as e:
            logging.info(e)
            raise

        # Initialisation de la liste
        liste_favoris = []
        # Construction des recette et ajout à la liste
        if res:
            for recette in res:
                id_recette = recette["id_recette"]
                liste_favoris.append(RecetteDao().trouver_par_id(id_recette))

        return liste_favoris

    @log
    def ajouter_favoris(self, recette: Recette, utilisateur: Utilisateur) -> bool:
        """
        Cette méthode ajoute une recette aux favoris d'un utilisateur.

        Parameters
        ----------
        recette : Recette
            Recette à ajouter aux favoris
        utilisateur : Utilisateur
            Utilisateur à modifier

        Returns
        -------
        bool :
            True si la recette a été rajoutée aux favoris de l'utilisateur, False sinon

        """
        res = None
        # Connexion à la base de données et commande SQL
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO projet.recette_favorite(id_utilisateur, id_recette) VALUES "
                        "(%(id_utilisateur)s, %(id_recette)s)                                   "
                        "RETURNING id_utilisateur;                                              ",
                        {
                            "id_recette": recette.id_recette,
                            "id_utilisateur": utilisateur.id_utilisateur,
                        },
                    )
                    res = cursor.fetchone()

        except Exception as e:
            logging.info(e)
            raise

        added = False
        if res:
            added = True

        return added

    @log
    def retirer_favoris(self, recette: Recette, utilisateur: Utilisateur) -> bool:
        """
        Cette méthode retire une recette des favoris d'un utilisateur.

        Parameters
        ----------
        recette : Recette
            Recette à retirer des favoris
        utilisateur : Utilisateur
            Utilisateur à modifier

        Returns
        -------
        bool :
            True si la recette a été retirée favoris de l'utilisateur, False sinon

        """
        res = None
        # Connexion à la base de données et commande SQL
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM projet.recette_favorite        "
                        " WHERE id_utilisateur = %(id_utilisateur)s "
                        "   AND id_recette = %(id_recette)s         ",
                        {
                            "id_recette": recette.id_recette,
                            "id_utilisateur": utilisateur.id_utilisateur,
                        },
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise

        return res > 0

    def consulter_liste_course(self, utilisateur: Utilisateur) -> list[Ingredient]:
        """
        Cette méthode renvoie les ingrédients de la liste de course de l'utilisateur.

        Parameters
        ----------
        utilisateur : Utilisateur
            Utilisateur à consulter

        Returns
        -------
        list[Ingredient, Recette] :
            Liste des ingrédients de la liste de courses et la recette associée

        """
        res = None
        # Connexion à la base de données et commande SQL
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                                  "
                        "  FROM liste_course                       "
                        " WHERE id_utilisateur=%(id_utilisateur)s; ",
                        {"id_utilisateur": utilisateur.id_utilisateur},
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise

        # Initialisation de la liste
        liste_course = []
        # Construction de l'objet et ajout à la liste
        if res:
            for row in res:
                id_ingredient = row["id_ingredient"]
                id_recette = row["id_recette"]
                liste_course.append(
                    [
                        IngredientDao().trouver_par_id(id_ingredient),
                        RecetteDao().trouver_par_id(id_recette),
                    ]
                )

        return liste_course

    @log
    def est_dans_liste_course(
        self, recette: Recette, ingredient: Ingredient, utilisateur: Utilisateur
    ) -> bool:
        """
        Cette méthode vérifie si un ingrédient appartient à la liste de course d'un utilisateur.

        Parameters
        ----------
        ingredient : Ingredient
            Ingrédient à ajouter à la liste de course
        recette : Recette
            Recette associée à l'ingrédient
        utilisateur : Utilisateur
            Utilisateur à test

        Returns
        -------
        bool :
            True si l'ingrédient est dans la liste de course, False sinon

        """
        res = None
        # Connexion à la base de données et commande SQL
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                                  "
                        "  FROM liste_course                       "
                        " WHERE id_utilisateur=%(id_utilisateur)s; ",
                        {"id_utilisateur": utilisateur.id_utilisateur},
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise

        est_dans_liste_course = False
        for row in res:
            if recette.id_recette == row["id_recette"]:
                if ingredient.id_ingredient == row["id_ingredient"]:
                    est_dans_liste_course = True

        return est_dans_liste_course

    @log
    def ajouter_liste_course(self, recette: Recette, utilisateur: Utilisateur) -> bool:
        """
        Cette méthode ajoute les ingrédients d'une recette à la liste de course d'un utilisateur.

        Parameters
        ----------
        recette : Recette
            Recette dont on doit ajouter les ingrédients
        utilisateur : Utilisateur
            Utilisateur à modifier

        Returns
        -------
        bool :
            True si les ingrédients ont été rajouté, False sinon

        """
        res = None
        # Connexion à la base de donnée et commandes SQL
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM projet.liste_course          "
                        "WHERE id_utilisateur = %(id_utilisateur)s"
                        "  AND id_recette = %(id_recette)s",
                        {
                            "id_utilisateur": utilisateur.id_utilisateur,
                            "id_recette": recette.id_recette,
                        },
                    )
                    for raw_ingredient in recette.liste_ingredient:
                        cursor.execute(
                            "INSERT INTO projet.liste_course VALUES                     "
                            "(%(id_utilisateur)s, %(id_ingredient)s, %(id_recette)s)    "
                            "RETURNING id_utilisateur;                                  ",
                            {
                                "id_recette": recette.id_recette,
                                "id_ingredient": raw_ingredient[0].id_ingredient,
                                "id_utilisateur": utilisateur.id_utilisateur,
                            },
                        )
                        res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        added = False

        if res:
            added = True

        return added

    @log
    def retirer_liste_course(
        self, recette: Recette, ingredient: Ingredient, utilisateur: Utilisateur
    ) -> bool:
        """
        Cette méthode retire un ingrédient de la liste de course de l'utilisateur.

        Parameters
        ----------
        ingredient : Ingredient
            Ingrédient à retirer de la liste de course
        recette : Recette
            Recette associée à l'ingrédient
        utilisateur : Utilisateur
            Utilisateur à modifier

        Returns
        -------
        bool :
            True si l'ingrédient a été retiré de la liste de course, False sinon

        """
        res = None
        # Connexion à la base de données et commande SQL
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM projet.liste_course            "
                        " WHERE id_utilisateur = %(id_utilisateur)s "
                        "   AND id_recette = %(id_recette)s         "
                        "   AND id_ingredient = %(id_ingredient)s;  ",
                        {
                            "id_recette": recette.id_recette,
                            "id_utilisateur": utilisateur.id_utilisateur,
                            "id_ingredient": ingredient.id_ingredient,
                        },
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise

        return res > 0

    @log
    def consulter_preference_ingredient_favori(self, utilisateur: Utilisateur) -> list[Ingredient]:
        """
        Cette méthode permet de consulter les ingrédients favoris de l'utilisateur.

        Parameters
        ----------
        utilisateur : Utilisateur
            Utilisateur à tester

        Returns
        -------
        list[Ingredient] :
            Liste des ingrédients favoris de l'utilisateur

        """
        res = None
        # Connexion à la base de données et commande SQL
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                                  "
                        "  FROM preference_ingredient              "
                        " WHERE id_utilisateur=%(id_utilisateur)s; ",
                        {"id_utilisateur": utilisateur.id_utilisateur},
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise
        # Initialisation de la liste
        liste_ingredients_favoris = []
        # Construction des ingrédients et ajout à la liste
        if res:
            for row in res:
                if row["favori"] is True:
                    id_ingredient = row["id_ingredient"]
                    liste_ingredients_favoris.append(IngredientDao().trouver_par_id(id_ingredient))
        return liste_ingredients_favoris

    @log
    def consulter_preference_ingredient_non_desire(
        self, utilisateur: Utilisateur
    ) -> list[Ingredient]:
        """
        Cette méthode permet de consulter les ingrédients non-désirés de l'utilisateur.

        Parameters
        ----------
        utilisateur : Utilisateur
            Utilisateur à tester

        Returns
        -------
        list[Ingredient] :
            Liste des ingrédients non-désirés de l'utilisateur

        """
        res = None
        # Connexion à la base de données et commande SQL
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                                  "
                        "  FROM preference_ingredient              "
                        " WHERE id_utilisateur=%(id_utilisateur)s; ",
                        {"id_utilisateur": utilisateur.id_utilisateur},
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise
        # Initialisation de la liste
        liste_ingredients_non_desires = []
        # Construction des objets et ajout à la liste
        if res:
            for row in res:
                if row["non_desire"] is True:
                    id_ingredient = row["id_ingredient"]
                    ingredient = IngredientDao().trouver_par_id(id_ingredient)
                    liste_ingredients_non_desires.append(ingredient)
        return liste_ingredients_non_desires

    @log
    def est_dans_preference_ingredient(
        self, ingredient: Ingredient, utilisateur: Utilisateur
    ) -> bool:
        """
        Cette méthode vérifie si un ingrédient est dans les préférences d'un utilisateur.

        Parameters
        ----------
        ingredient : Ingredient
            Ingrédient à tester
        utilisateur : Utilisateur
            Utilisateur à tester

        Returns
        -------
        bool :
            True si l'ingrédient est dans les préférences de l'utilisateur, False sinon

        """
        res = None
        # Connexion à la base de données et commande SQL
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                                  "
                        "  FROM preference_ingredient              "
                        " WHERE id_utilisateur=%(id_utilisateur)s; ",
                        {"id_utilisateur": utilisateur.id_utilisateur},
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise

        est_dans_preference_ingredient = False
        for row in res:
            if ingredient.id_ingredient == row["id_ingredient"]:
                est_dans_preference_ingredient = True

        return est_dans_preference_ingredient

    @log
    def modifier_preference_ingredient(
        self, ingredient: Ingredient, utilisateur: Utilisateur, modif: str
    ) -> bool:
        """
        Cette méthode permet de modifier la préférence concernant un ingrédient de l'utilisateur.

        Parameters
        ----------
        ingredient : Ingredient
            Ingrédient à modifier
        utilisateur : Utilisateur
            Utilisateur à modifier

        Returns
        -------
        bool :
            True si la préférence ingrédient de l'utilisateur a été modifiée, False sinon

        """
        res = None

        # Détermination de la préférence
        if modif == "F":
            raw_non_desire = False
            raw_favori = True
        elif modif == "ND":
            raw_non_desire = True
            raw_favori = False
        else:
            raw_non_desire = False
            raw_favori = False

        # Connexion à la base de données et commande SQL
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO projet.preference_ingredient VALUES                     "
                        "(%(id_utilisateur)s, %(id_ingredient)s, %(non_desire)s, %(favori)s) "
                        "RETURNING id_utilisateur;                                           ",
                        {
                            "id_utilisateur": utilisateur.id_utilisateur,
                            "id_ingredient": ingredient.id_ingredient,
                            "non_desire": raw_non_desire,
                            "favori": raw_favori,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        added = False
        if res:
            added = True

        return added

    @log
    def retirer_preference_ingredient(
        self, ingredient: Ingredient, utilisateur: Utilisateur
    ) -> bool:
        """
        Cette méthode permet de retirer un ingrédient des préférences.

        Parameters
        ----------
        ingredient : Ingredient
            Ingrédient à retirer
        utilisateur : Utilisateur
            Utilisateur à modifier

        Returns
        -------
        Bool :
            True si la préférence ingrédient a été retirée, False sinon

        """
        res = None
        # Connexion à la base de données et commande SQL
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM projet.preference_ingredient         "
                        " WHERE id_utilisateur = %(id_utilisateur)s       "
                        "   AND id_ingredient = %(id_ingredient)s         ",
                        {
                            "id_ingredient": ingredient.id_ingredient,
                            "id_utilisateur": utilisateur.id_utilisateur,
                        },
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise

        return res > 0


if __name__ == "__main__":
    load_dotenv()
