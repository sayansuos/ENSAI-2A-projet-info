from typing import List, Optional
from src.classes.recette import Recette
from src.dao.db_connection import DBConnection


class RecetteService(Recette):
    """
    Définis les méthodes de la classe Recette
    """

    def trouver_recette_par_nom(self, nom: str) -> Optional[Recette]:
        """
        Permet de trouver une recette en indiquant le nom de celle-ci

        Args:
            nom (str): Nom de la recette recherchée

        Returns:
            Optional[Recette]: Renvoie la recette si le nom correspond à une
                               recette existante. Renvoie None sinon
        """
        if not isinstance(nom, str):
            raise TypeError("nom doit être une instance de str")
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT *      " "FROM Recette  " "WHERE nom_recette = %(nom)s", {"nom": nom}
                )

                res = cursor.fetchone()

        if res:
            id = res["id"]
            nom = res["nom"]
            liste_ingredient = res["liste_ingredient"]

            res = Recette(id_recette=id, nom_recette=nom, liste_ingredient=liste_ingredient)

        return res

    def trouver_recette_par_ingredient(ingredient: str) -> List[Recette]:
        """
        Permet de trouver une liste de recette contenant l'ingrédient entré
        en paramètre

        Args:
            ingredient (str): Nom de l'ingrédient recherché

        Returns:
            list[Recette]: Renvoie la liste des recettes contenant cet ingrédient
        """
        if not isinstance(ingredient, str):
            raise TypeError("ingredient doit être une instance de str")
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                # La requête SQL est à trouver
                cursor.execute("SELECT *      " "FROM Recette  " "WHERE ")

                res = cursor.fetchall()

        Liste_recettes = []

        if res:
            for row in res:
                id = row["id"]
                nom = row["nom"]
                liste_ingredient = row["liste_ingredient"]

                recette = Recette(id_recette=id, nom_recette=nom, liste_ingredient=liste_ingredient)

                Liste_recettes.append(recette)

        return Liste_recettes

    def lister_toutes_recettes() -> List[Recette]:
        """
        Renvoie une liste de toutes les recettes existantes.

        Returns:
            list[Recette]: Liste de toutes les recettes existantes
        """

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT *      " "FROM Recette  ")

                res = cursor.fetchall()

        Liste_recettes = []
        if res:
            for row in res:
                id = row["id"]
                nom = row["nom"]
                liste_ingredient = row["liste_ingredient"]

                recette = Recette(id_recette=id, nom_recette=nom, liste_ingredient=liste_ingredient)

                Liste_recettes.append(recette)

        return Liste_recettes
