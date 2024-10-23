import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

from dao.ingredient_dao import IngredientDao
from src.business_object.ingredient import Ingredient
from business_object.recette import Recette


class RecetteDao(metaclass=Singleton):
    """
    Classe contenant les méthodes pour accéder aux recettes de la base de données.
    """

    @log
    def creer(self, recette) -> bool:
        """
        Création d'une recette dans la base de données

        Parameters
        ----------
        recette : Recette

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
                        "INSERT INTO projet.recette VALUES                              "
                        "(%(id)s, %(nom)s, %(description_recette)s, %(avis)s, %(note)s) "
                        "RETURNING id_recette;                                          ",
                        {
                            "id": recette.id_recette,
                            "nom": recette.nom_recette,
                            "description_recette": recette.description_recette,
                            "avis": "".join(recette.avis),
                            "note": recette.note,
                        },
                    )
                    res = cursor.fetchone()

                    for raw_ingredient in recette.liste_ingredient:
                        nom_ingredient = raw_ingredient[0]
                        quantite_ingredient = raw_ingredient[1]
                        id_ingredient = (
                            IngredientDao()
                            .trouver_par_nom(nom_ingredient=nom_ingredient, cursor=cursor)
                            .id_ingredient
                        )

                        cursor.execute(
                            "INSERT INTO projet.recette_ingredient VALUES        "
                            "(%(id_ingredient)s, %(id_recette)s, %(quantite)s);  ",
                            {
                                "id_ingredient": id_ingredient,
                                "id_recette": recette.id_recette,
                                "quantite": quantite_ingredient,
                            },
                        )

        except Exception as e:
            logging.info(e)

        created = False
        if res:
            recette.id_recette = res["id_recette"]
            created = True

        return created, res

    @log
    def trouver_par_id(self, id_recette) -> Recette:
        """
        Trouver une recette grace à son identifant

        Parameters
        ----------
        id_recette : int
            numéro id de la recette que l'on souhaite trouver

        Returns
        -------
        recette : Recette
            renvoie la recette que l'on cherche par id
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                                   "
                        " FROM recette                              "
                        " JOIN recette_ingredient USING (id_recette)"
                        " WHERE id_recette = %(id_recette)s;  ",
                        {"id_recette": id_recette},
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise

        recette = None
        if res:

            id_recette = res["id_recette"][0]
            nom_recette = res["nom_recette"][0]
            description_recette = res["description_recette"]
            note = res["note"]
            avis = res["avis"].split(";")
            liste_ingredient = []
            for i in range(0, len(res)):
                liste_ingredient.append([res["id_ingredient"], res["quantite"]])

            recette = Recette(
                id_recette, nom_recette, liste_ingredient, description_recette, note, avis
            )

        return recette

    @log
    def trouver_par_ingredient(self, ingredient:Ingredient):
        """
        Donne une liste de recette contenant un ingredient

        Parameters
        ----------
        ingredient : Ingredient
            Ingredient par lequel on veut filtrer

        Returns
        -------
        liste_recettes : list[Recette]
            Renvoie une liste de recette filtrée par l'ingrédient voulu
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                                   "
                        " FROM recette                              "
                        " JOIN recette_ingredient USING (id_recette)"
                        " WHERE id_ingredient = %(id_ingredient)s;  ",
                        {"id_ingredient": ingredient.id_ingredient},
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise

    @log
    def lister_tous(self) -> list[Recette]:
        """
        Lister toutes les recettes.

        Parameters
        ----------
        None

        Returns
        -------
        liste_recette : list[Recette]
            renvoie la liste de toutes les recettes dans la base de données
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                                     "
                        " FROM recette                                "
                        " JOIN recette_ingredient USING (id_recette); ",
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise

        liste_recette = []

        if res:
            liste_id = []
            for row in res:
                if row["id_recette"] not in liste_id:
                    liste_id.append(row["id_recette"])

            for id in liste_id:

                recette = self.trouver_par_id(id)
                liste_recette.append(recette)

        return liste_recette

    @log
    def supprimer(self, recette) -> bool:
        """
        Suppression d'une recette dans la base de données.

        Parameters
        ----------
        recette : Recette
            recette à supprimer de la base de données

        Returns
        -------
            True si la recette a bien été supprimée
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Supprimer une recette
                    cursor.execute(
                        "DELETE FROM recette                    "
                        " WHERE id_recette=%(id_recette)s       ",
                        {"id_recette": recette.id_recette},
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise

        return res > 0
