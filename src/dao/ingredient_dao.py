import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

from business_object.ingredient import Ingredient


class IngredientDao(metaclass=Singleton):
    """
    Classe contenant les méthodes pour accéder aux ingrédients de la base de données.
    """

    @log
    def creer(self, ingredient) -> bool:
        """
        Création d'un ingrédient dans la base de données.

        Parameters
        ----------
        ingredient : Ingredient

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

        created = False
        if res:
            ingredient.id_ingredient = res["id_ingredient"]
            created = True

        return created

    @log
    def trouver_par_id(self, id_ingredient) -> Ingredient:
        """
        Trouver un ingrédient grace à son identifiant.

        Parameters
        ----------
        id_ingredient : int
            numéro id de l'ingrédient que l'on souhaite trouver

        Returns
        -------
        ingredient : Ingredient
            renvoie l'ingrédient que l'on cherche par id
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        " SELECT *                                   "
                        "   FROM ingredient                          "
                        "  WHERE id_ingredient = %(id_ingredient)s;  ",
                        {"id_ingredient": id_ingredient},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise

        ingredient = None
        if res:
            ingredient = Ingredient(
                nom_ingredient=res["nom_ingredient"],
                id_ingredient=res["id_ingredient"],
            )

        return ingredient

    @log
    def trouver_par_nom(self, nom_ingredient) -> Ingredient:
        """
        Trouver un ingrédient grace à son nom.

        Parameters
        ----------
        nom_ingredient : str
            nom de l'ingrédient que l'on souhaite trouver

        Returns
        -------
        ingredient : Ingredient
            renvoie l'ingrédient que l'on cherche par id
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        " SELECT *                                   "
                        "   FROM ingredient                          "
                        "  WHERE nom_ingredient = %(nom_ingredient)s;  ",
                        {"nom_ingredient": nom_ingredient},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise

        ingredient = None
        if res:
            ingredient = Ingredient(
                nom_ingredient=res["nom_ingredient"],
                id_ingredient=res["id_ingredient"],
            )

        return ingredient

    @log
    def lister_tous(self) -> list[Ingredient]:
        """
        Lister tous les ingrédients

        Parameters
        ----------
        None

        Returns
        -------
        liste_ingredients : list[Ingredient]
            renvoie la liste de tous les ingrédients dans la base de données
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                              "
                        "  FROM ingredient;                    "
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise

        liste_ingredients = []

        if res:
            for row in res:
                ingredient = Ingredient(
                    id_ingredient=row["id_ingredient"], nom_ingredient=row["nom_ingredient"]
                )

                liste_ingredients.append(ingredient)

        return liste_ingredients
