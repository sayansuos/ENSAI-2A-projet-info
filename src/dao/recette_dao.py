import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

from dao.ingredient_dao import IngredientDao
from business_object.ingredient import Ingredient
from business_object.recette import Recette


class RecetteDao(metaclass=Singleton):
    """
    Cette classe contient les méthodes quo permettent d'accéder aux recettes de la base de données.
    """

    @log
    def creer(self, recette) -> bool:
        """
        Cette méthode permet de créer une recette dans la base de données.

        Parameters
        ----------
        recette : Recette
            Recette que l'on souhaite créer

        Returns
        -------
        Bool :
            True si la création est un succès, False sinon
        """

        res = None

        try:
            # Connexion à la base de données et commande SQL (table recette)
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

                    # Commande SQL (table recette_ingredient)
                    for raw_ingredient in recette.liste_ingredient:
                        cursor.execute(
                            "INSERT INTO projet.recette_ingredient VALUES        "
                            "(%(id_ingredient)s, %(id_recette)s, %(quantite)s);  ",
                            {
                                "id_ingredient": raw_ingredient[0].id_ingredient,
                                "id_recette": recette.id_recette,
                                "quantite": raw_ingredient[1],
                            },
                        )

        except Exception as e:
            logging.info(e)

        created = False
        # Retourne l'identifiant de la recette
        if res:
            recette.id_recette = res["id_recette"]
            created = True

        return created

    @log
    def trouver_par_id(self, id_recette) -> Recette:
        """
        TCette méthode permet de trouver une recette grace à son identifiant.

        Parameters
        ----------
        id_recette : int
            Identifiant de la recette que l'on souhaite trouver

        Returns
        -------
        Recette :
            Recette que l'on souhaite trouver
        """
        # Connexion à la base de données et commande SQL
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
        # Construction de la recette
        if res:
            id_recette = res[0]["id_recette"]
            nom_recette = res[0]["nom_recette"]
            description_recette = res[0]["description_recette"]
            note = res[0]["note"]
            avis = res[0]["avis"].split(";")
            liste_ingredient = []
            for i in range(0, len(res)):
                ingredient = IngredientDao().trouver_par_id(res[i]["id_ingredient"])
                liste_ingredient.append([ingredient, res[i]["quantite"]])

            recette = Recette(
                nom_recette=nom_recette,
                liste_ingredient=liste_ingredient,
                description_recette=description_recette,
                id_recette=id_recette,
                note=note,
                avis=avis,
            )
        return recette

    @log
    def trouver_par_nom(self, nom_recette) -> Recette:
        """
        Cette méthode permet de trouver un ingrédient grace à son nom.

        Parameters
        ----------
        nom_recette : str
            Nom de l'ingrédient que l'on souhaite trouver

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
                        "SELECT *                                   "
                        " FROM recette                              "
                        " JOIN recette_ingredient USING (id_recette)"
                        " WHERE nom_recette = %(nom_recette)s;  ",
                        {"nom_recette": nom_recette},
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise

        recette = None
        # Construction de la recette
        if res:
            id_recette = res[0]["id_recette"]
            nom_recette = res[0]["nom_recette"]
            description_recette = res[0]["description_recette"]
            note = res[0]["note"]
            avis = res[0]["avis"].split(";")
            liste_ingredient = []
            for i in range(0, len(res)):
                ingredient = IngredientDao().trouver_par_id(res[i]["id_ingredient"])
                liste_ingredient.append([ingredient, res[i]["quantite"]])

            recette = Recette(
                nom_recette=nom_recette,
                liste_ingredient=liste_ingredient,
                description_recette=description_recette,
                id_recette=id_recette,
                note=note,
                avis=avis,
            )

        return recette

    @log
    def trouver_par_ingredient(self, ingredient: Ingredient):
        """
        Cette méthode permet de trouver les recettes qui contiennent un ingrédient spécifié.

        Parameters
        ----------
        ingredient : Ingredient
            Ingrédient contenu dans les recettes souhaitées.

        Returns
        -------
        list[Recette] :
            Liste des recettes qui contiennent l'ingrédient souhaité.
        """
        # Connexion à la base de données et commande SQL
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                                   "
                        "FROM recette                               "
                        "JOIN recette_ingredient USING (id_recette) "
                        "WHERE id_ingredient = %(id_ingredient)s;   ",
                        {"id_ingredient": ingredient.id_ingredient},
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise

        # Initialisation de la lite
        liste_recette = []

        # Construction des recettes et ajout à la liste
        if res:
            for recette in res:
                id_recette = recette["id_recette"]
                liste_recette.append(self.trouver_par_id(id_recette))

        return liste_recette

    @log
    def lister_tous(self) -> list[Recette]:
        """
        Cette méthode permet de lister toutes les recettes de la base de données.

        Returns
        -------
        list[Recette] :
            Liste des recettes de la base de données.
        """
        # Connexion à la base de données et commande SQL
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
            print(e)
            raise

        # Initialisation de la liste
        liste_recette = []

        # Construction des recettes et ajout à la liste
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
        Cette méthode permet de supprimer une recette de la base de données.

        Parameters
        ----------
        recette : Recette
            Recette à supprimer

        Returns
        -------
        Bool :
            True si la recette a été supprimée, False sinon

        """
        # Connexion à la base de données et commande SQL
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
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

    @log
    def ajouter_note_et_com(self, recette: Recette, note: int, com: str) -> bool:
        """
        Cette méthode permet d'ajoouter une note et un commentaire à une recette de la base de
        données.

        Parameters
        ----------
        recette : Recette
            Recette à noter et commenter

        Returns
        -------
        Bool :
            True si la modification a été faite, False sinon

        """
        res = None
        avis = ""

        # Décomposition de la liste des avis en un seul str séparé par des ';'
        # Ajout du nouvel avis
        for msg in recette.avis:
            avis += f"{msg} ;"
        avis += com

        # Nécessaire pour le bon calcul de la note
        raw_note = recette.note
        nb_note = len(recette.avis)
        if recette.note is None:
            raw_note = 0
            nb_note = 0
            avis = com

        # Connexion à la base de données et commande SQL
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        " UPDATE recette                            "
                        "    SET avis = %(avis)s, note = %(note)s   "
                        "  WHERE id_recette = %(id_recette)s        "
                        " RETURNING id_recette                      ",
                        {
                            "avis": avis,
                            "note": (raw_note * nb_note + note) / (nb_note + 1),
                            "id_recette": recette.id_recette,
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
