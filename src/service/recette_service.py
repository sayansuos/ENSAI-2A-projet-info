from typing import List, Optional
from business_object.recette import Recette
from dao.recette_dao import RecetteDao
from business_object.ingredient import Ingredient
from view.session import Session


class RecetteService:
    """
    Définis les méthodes de la classe Recette
    """

    def __init__(self):
        pass

    def trouver_recette_par_id(self, id: int) -> Optional[Recette]:
        """
        Permet de trouver une recette par identifiant

        Args:
            id (int):
                Identifiant de la recette recherchée

        Returns:
            Optional[Recette]:
                Retourne la recette correspondant à l'identifiant.
                Retourne None sinon
        """
        return RecetteDao().trouver_par_id(id)

    def trouver_recette_par_nom(self, nom: str) -> Optional[Recette]:
        """
        Permet de trouver une recette en indiquant le nom de celle-ci

        Args:
            nom (str):
                Nom de la recette recherchée

        Returns:
            Optional[Recette]:
                Renvoie la recette si le nom correspond à une recette existante.
                Renvoie None sinon
        """
        if not isinstance(nom, str):
            raise TypeError("nom doit être une instance de str")

        return RecetteDao().trouver_par_nom(nom)

    def trouver_recette_par_ingredient(self, ingredient: Ingredient) -> List[Recette]:
        """
        Permet de trouver une liste de recette contenant l'ingrédient entré
        en paramètre

        Args:
            ingredient (Ingredient):
                Ingrédient recherché

        Returns:
            list[Recette]:
                Renvoie la liste des recettes contenant cet ingrédient
        """

        if not isinstance(ingredient, Ingredient):
            raise TypeError("ingredient doit être une instance de Ingredient")
        return RecetteDao().trouver_par_ingredient(ingredient)

    def lister_toutes_recettes(self) -> List[Recette]:
        """
        Renvoie une liste de toutes les recettes existantes.

        Returns:
            list[Recette]:
                Liste de toutes les recettes existantes
        """
        return Session().liste_recettes

    def creer_recette(self, recette: Recette) -> Optional[Recette]:
        """
        Permet d'ajouter une recette dans la base de données.

        Args:
            recette (Recette):
                Informations de la recette à ajouter

        Returns:
            Optional[Recette]:
                Retourne la recette si elle a été correctement ajoutée à la base de données
                None sinon
        """
        return recette if RecetteDao().creer(recette) is True else None

    def supprimer_recette(self, recette: Recette) -> bool:
        """
        Permet de supprimer une recette de la base de données

        Args:
            recette (Recette):
                Recette à supprimer

        Returns:
            bool:
                True si la recette a été correctement supprimée.
                False sinon.
        """
        return RecetteDao().supprimer(recette)

    def voir_note_avis(self, recette: Recette) -> Optional[float]:
        """
        Permet de voir la note d'une recette

        Args:
            recette (Recette): Recette dont on veut voir la note

        Returns:
            Optional[float]:
                Note de la recette si la recette a été notée au moins une fois.
                None sinon.
        """
        if not isinstance(recette, Recette):
            raise TypeError("recette doit être une instance de Recette.")

        note_avis_str = "\n\n" + str(recette) + "\n\n" + "Avis :"
        if recette.avis[0] != "":
            note_avis_str += "\n"
            for av in recette.avis:
                note_avis_str += f"- {av} \n"
        else:
            note_avis_str += " Il n'y a aucun avis pour cette recette. \n"
        if recette.note:
            note_avis_str += f"\nNote : {round(recette.note, 2)}/5"
        else:
            note_avis_str += "\nNote : Il n'y a aucune note pour cette recette."

        return note_avis_str

    def ajouter_note_et_com(self, recette: Recette, note: int, com: str) -> bool:
        """
        Ajoute une note et un commentaire à une recette.

        Args :
            recette (Recette) : recette dont les ingrédients sont  à ajouter à la table
            note (int) : Note attribuée à la recette
            com (str) : Commentaire attribué à la recette

        Returns:
            bool: True si la note et le commentaires ont été ajouté à la table, False sinon
        """
        if not isinstance(recette, Recette):
            raise TypeError("recette doit être une instance de Recette.")
        if not isinstance(note, int):
            raise TypeError("note doit être une instance de int.")
        if not isinstance(com, str):
            raise TypeError("com doit être une instance de str.")
        if note < 0 or note > 5:
            raise ValueError("La note doit être comprise entre 0 et 5.")
        if ";" in com:
            raise ValueError("';' ne peut pas être utilisé dans le commentaire.")

        return RecetteDao().ajouter_note_et_com(recette=recette, note=note, com=com)

    def lire_recette(self, recette: Recette) -> str:
        """
        Renvoie la description d'une recette

        Args:
            recette (Recette):
                Recette dont on veut voir la description

        Returns:
            str:
                Description de la recette
        """

        if not isinstance(recette, Recette):
            raise TypeError("Recette doit être une instance de Recette.")

        recette_str = "\n\n" + str(recette) + "\n\n" + "Ingredients :\n"
        for ingr in recette.liste_ingredient:
            ingredient, quantites = ingr
            recette_str += f"- {ingredient.nom_ingredient} ({quantites}) \n"
        recette_str += f"\nDescription : \n{recette.description_recette}"

        return recette_str
