from typing import List, Optional
from src.classes.recette import Recette


class RecetteService(Recette):
    """
    Définis les méthodes de la classe Recette
    """

    def trouver_recette_par_nom(nom: str) -> Recette:
        pass

    def trouver_recette_par_ingredient(ingredient: str) -> list[Recette]:
        pass

    def lister_toutes_recettes() -> list[Recette]:
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT *      "
                    "FROM Recette  "
                )

                res = cursor.fetchall()

        if res:
            for row in res:
                pass
