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
    & recette et/ou ingrédient.
    """

    @log
    def est_dans_favoris(self, recette: Recette, utilisateur: Utilisateur) -> bool:
        """
        Vérifie si les ingrédients d'une recette sont dans la liste des favoris.

        Args :
            recette (Recette) : recette dont on souhaite vérifier les ingrédients
            utilisateur (Utilisateur) : utilisateur à qui appartient la liste de course

        Returns:
            bool: True si les ingrédients sont dans la liste de course, False sinon
        """
        res = None

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
    def consulter_favoris(utilisateur: Utilisateur) -> list[Recette]:
        """
        Renvoie la liste des recettes favorites de l'utilisateur.

        Args :
            utilisateur (Utilisateur) : utilisateur dont on souhaite consulter les favoris

        Returns:
            liste_favoris : liste des recettes favorites
        """
        res = None

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

        liste_favoris = []
        if res:
            for recette in res:
                id_recette = recette["id_recette"]
                liste_favoris.append(RecetteDao().trouver_par_id(id_recette))

        return liste_favoris

    @log
    def ajouter_favoris(self, recette: Recette, utilisateur: Utilisateur) -> bool:
        """
        Ajoute une recette à la table "recette_favorite" de l'utilisateur

        Args :
            recette (Recette) : recette à ajouter à la table
            utilisateur (Utilisateur) : utilisateur à qui on ajoute la recette favorite

        Returns:
            bool: True si la recette a été ajoutée à la table, False sinon
        """
        res = None

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

        added = False

        if res:
            added = True

        return added

    @log
    def retirer_favoris(self, recette: Recette, utilisateur: Utilisateur) -> bool:
        """
        Retire une recette à la table "recette_favorite" de l'utilisateur

        Args :
            recette (Recette) : Recette à retirer de la table
            utilisateur (Utilisateur) : utilisateur à qui on retire la recette favorite

        Returns:
            bool: True si la recette a été supprimée de la table, False sinon
        """
        res = None

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

    def consulter_liste_course(utilisateur: Utilisateur) -> list[Ingredient]:
        """
        Renvoie les ingrédients de la liste de course de l'utilisateur.

        Args :
            utilisateur (Utilisateur) : utilisateur dont on souhaite consulter les favoris

        Returns:
            liste_course : liste des ingrédients de la liste de course
        """
        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                                  "
                        "  FROM liste_course                   "
                        " WHERE id_utilisateur=%(id_utilisateur)s; ",
                        {"id_utilisateur": utilisateur.id_utilisateur},
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise

        liste_course = []
        if res:
            for row in res:
                id_ingredient = row["id_ingredient"]
                liste_course.append(IngredientDao.trouver_par_id(id_ingredient))

        return liste_course

    @log
    def est_dans_liste_course(self, recette: Recette, utilisateur: Utilisateur) -> bool:
        """
        Vérifie si les ingrédients d'une recette sont dans la liste de course.

        Args :
            recette (Recette) : recette dont on souhaite vérifier les ingrédients
            utilisateur (Utilisateur) : utilisateur à qui appartient la liste de course

        Returns:
            bool: True si les ingrédients sont dans la liste de course, False sinon
        """
        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                                  "
                        "  FROM liste_course                   "
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
                est_dans_liste_course = True

        return est_dans_liste_course

    @log
    def ajouter_liste_course(self, recette: Recette, utilisateur: Utilisateur) -> bool:
        """
        Ajoute les ingrédient d'une recette à la table "liste_course" de l'utilisateur

        Args :
            recette (Recette) : recette dont les ingrédients sont  à ajouter à la table
            utilisateur (Utilisateur) : utilisateur à qui on modifie la liste de course

        Returns:
            bool: True si les ingrédients ont été ajouté à la table, False sinon
        """
        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
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
    def retirer_liste_course(self, recette: Recette, utilisateur: Utilisateur) -> bool:
        """
        Enlève tous les ingrédients de la recette à la liste "liste_de_course" de l'utilisateur

        Args :
            recette (Recette) : Recette à retirer de la table
            utilisateur (Utilisateur) : utilisateur à qui on modifie la liste de course

        Returns:
            bool: True si les ingrédients ont été retiré à la liste, False sinon
        """
        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM projet.liste_course            "
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

    @log
    def consulter_preference_ingredient_favori(self, utilisateur: Utilisateur) -> list[Ingredient]:
        """
        Renvoie les préférences pour les ingrédients de l'utilisateur.

        Args :
            utilisateur (Utilisateur) : utilisateur dont on souhaite consulter les préférences

        Returns:
            liste_ingredients_favoris : liste des ingrédients favoris de l'utilisateur
        """
        res = None

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

        liste_ingredients_favoris = []
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
        Renvoie les préférences pour les ingrédients de l'utilisateur.

        Args :
            utilisateur (Utilisateur) : utilisateur dont on souhaite consulter les préférences

        Returns:
            liste_ingredients_favoris : liste des ingrédients favoris de l'utilisateur
        """
        res = None

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

        liste_ingredients_non_desires = []
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
        Vérifie si un ingrédient est dans la liste des préférences

        Args :
            ingredient (Ingredient) : ingredient qu'on souhaite vérifier dans les préférences
            utilisateur (Utilisateur) : utilisateur à qui appartient la liste de course

        Returns:
            bool: True si l'ingrédient est dans la liste des préférences, False sinon
        """
        res = None

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
                    print(res)
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
        Ajoute un ingrédient à la liste des préférences

        Args :
            ingredient (Ingredient) : ingredient qu'on souhaite ajouter aux préférences
            utilisateur (Utilisateur) : utilisateur à qui on modifie la liste de course

        Returns:
            bool: True si l'ingrédients a bien été ajouté à la table, False sinon
        """
        res = None

        if modif == "F":
            raw_non_desire = False
            raw_favori = True
        elif modif == "ND":
            raw_non_desire = True
            raw_favori = False
        else:
            raw_non_desire = False
            raw_favori = False

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
        Retire un ingrédient à la liste des préférences

        Args :
            ingredient (Ingredient) : ingredient qu'on souhaite retirer des préférences
            utilisateur (Utilisateur) : utilisateur à qui on modifie la liste de course

        Returns:
            bool: True si l'ingrédients a bien été retiré à la table, False sinon
        """
        res = None

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
