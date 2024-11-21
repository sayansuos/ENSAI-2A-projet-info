import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

from business_object.ingredient import Ingredient


class IngredientDao(metaclass=Singleton):
    """
    Cette classe contient les méthodes pour accéder aux ingrédients de la base de données.
    """

    @log
    def creer(self, ingredient) -> bool:
        """
        Cette méthode permet de créer un ingrédient dans la base de données.

        Parameters
        ----------
        ingredient : Ingredient
            Ingrédient que l'on souhaite créer

        Returns
        -------
        Bool :
            True si la création est un succès, False sinon
        """
        res = None

        # Connexion à la base de données et commande SQL
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO ingredient(id_ingredient, nom_ingredient) VALUES "
                        "(%(id_ingredient)s, %(nom_ingredient)s)                      "
                        "  RETURNING id_ingredient;                                   ",
                        {
                            "id_ingredient": ingredient.id_ingredient,
                            "nom_ingredient": ingredient.nom_ingredient,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise

        # Retourne l'identifiant de l'ingrédient
        created = False
        if res:
            ingredient.id_ingredient = res["id_ingredient"]
            created = True

        return created

    @log
    def trouver_par_id(self, id_ingredient) -> Ingredient:
        """
        Cette méthode permet de trouver un ingrédient grace à son identifiant.

        Parameters
        ----------
        id_ingredient : int
            Identifiant de l'ingrédient que l'on souhaite trouver

        Returns
        -------
        Ingredient :
            Ingrédient que l'on souhaite trouver
        """

        # Connexion à la base de données et commande SQL
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        " SELECT *                                   "
                        "   FROM projet.ingredient                   "
                        "  WHERE id_ingredient = %(id_ingredient)s;  ",
                        {"id_ingredient": id_ingredient},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise

        ingredient = None
        # Construction de l'ingrédient
        if res:
            ingredient = Ingredient(
                nom_ingredient=res["nom_ingredient"],
                id_ingredient=res["id_ingredient"],
            )

        return ingredient

    @log
    def trouver_par_nom(self, nom_ingredient, cursor=None) -> Ingredient:
        """
        Cette méthode permet de trouver un ingrédient grace à son nom.

        Parameters
        ----------
        nom_ingredient : str
            Nom de l'ingrédient que l'on souhaite trouver

        Returns
        -------
        ingredient : Ingredient
            Ingredient que l'on souhaite trouver
        """
        # Si la connexion n'a pas déjà été faite (cf. recette_dao)
        # Connexion à la base de données et commande SQL
        if cursor is None:
            try:
                with DBConnection().connection as connection:
                    with connection.cursor() as cursor:
                        cursor.execute(
                            " SELECT *                                     "
                            "   FROM projet.ingredient                     "
                            "  WHERE nom_ingredient = %(nom_ingredient)s;  ",
                            {"nom_ingredient": nom_ingredient},
                        )
                        res = cursor.fetchone()
            except Exception as e:
                logging.info(e)
                raise
        # Si la connexion a déjà été faite (cf. recette_dao)
        # Commande SQL
        else:
            cursor.execute(
                " SELECT *                                    "
                "   FROM projet.ingredient                     "
                "  WHERE nom_ingredient = %(nom_ingredient)s;  ",
                {"nom_ingredient": nom_ingredient},
            )
            res = cursor.fetchone()

        ingredient = None
        # Construction de l'ingrédient
        if res:
            ingredient = Ingredient(
                nom_ingredient=res["nom_ingredient"],
                id_ingredient=res["id_ingredient"],
            )

        return ingredient

    @log
    def lister_tous(self) -> list[Ingredient]:
        """
        Cette méthode permet de lister tous les ingrédients.

        Returns
        -------
        liste_ingredients : list[Ingredient]
            Liste de tous les ingrédients de la base de données
        """
        # Connexion à la base de données et commande SQL
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                              "
                        "  FROM projet.ingredient;             "
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise

        # Initialisation de la liste
        liste_ingredients = []

        # Construction des ingrédients et ajout à la liste
        if res:
            for row in res:
                ingredient = Ingredient(
                    id_ingredient=row["id_ingredient"], nom_ingredient=row["nom_ingredient"]
                )
                liste_ingredients.append(ingredient)
        return liste_ingredients
