import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

from business_object.recette import Recette


class RecetteDao(metaclass=Singleton):
    """Classe contenant les méthodes pour accéder aux recettes de la base de données"""

    @log
    def creer(self, recette) -> bool:
        """Creation d'une recette dans la base de données

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
                        "INSERT INTO recette(id_recette, nom_recette, description_recette, avis, note) VALUES       "
                        "(%(id_recette)s, %(nom_recette)s, %(description_recette)s, %(avis)s, %(note)s)             "
                        "  RETURNING id_recette;                                                ",
                        {
                            "id_recette": recette.id_recette,
                            "nom_recette": recette.nom_recette,
                            "description_recette": recette.description_recette,
                            "avis": recette.avis,
                            "note": recette.note,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        created = False
        if res:
            recette.id_recette = res["id_recette"]
            created = True

        return created

    @log
    def trouver_par_id(self, id_recette) -> Recette:
        """trouver une recette grace à son id

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
                        "SELECT *                           "
                        " FROM recette                      "
                        " JOIN recette_ingredient USING (id_recette)"
                        " WHERE id_recette = %(id_recette)s;  ",
                        {"id_recette": id_recette},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise

        recette = None
        if res:
            recette = Recette(
                id_recette=res["id_recette"],
                nom_recette=res["nom_recette"],
                liste_ingredient=[res["id_ingredient"], res["quantite"]],
                description_recette=res["description_recette"],
                note=res["note"],
                avis=res["avis"],
            )

        return recette
