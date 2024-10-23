import logging
from dotenv import load_dotenv

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

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
            recette.id_recette = res["id_recette"]
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
                                "id_ingredient": raw_ingredient.id_ingredient,
                                "id_utilisateur": utilisateur.id_utilisateur,
                            },
                        )
                        res = cursor.fetchone()

        except Exception as e:
            logging.info(e)

        added = False
        if res:
            recette.id_recette = res["id_recette"]
            added = True

        return added


if __name__ == "__main__":
    load_dotenv()
