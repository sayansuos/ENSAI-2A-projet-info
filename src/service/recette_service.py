from typing import List, Optional
from business_object.recette import Recette
from dao.recette_dao import RecetteDao
from business_object.ingredient import Ingredient


class RecetteService:
    """
    Définis les méthodes de la classe Recette
    """

    def __init__(self):
        pass

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

        pass
        # return RecetteDao.trouver_par_nom(nom)

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

        pass
        # return RecetteDao.trouver_par_ingredient(ingredient)

    def lister_toutes_recettes(self) -> List[Recette]:
        """
        Renvoie une liste de toutes les recettes existantes.

        Returns:
            list[Recette]:
                Liste de toutes les recettes existantes
        """

        return RecetteDao().lister_tous()

    def noter_recette(self, note: float, recette: Recette):
        """
        Permet de noter une recette de 0 à 5.

        Args:
            note (float):
                Note donnée à la recette. Les notes vont de 0 à 5, avec un pas de 0.5
        """

        if not (isinstance(note, float) or isinstance(note, int)):
            raise TypeError("La note doit être un nombre compris entre 0 et 5.")
        if note < 0 or note > 5:
            raise ValueError("La note doit être comprise entre 0 et 5.")
        if not isinstance(recette, Recette):
            raise TypeError("La recette doit être une instance de Recette.")

        # super.note = super.note * (nb_notes / (nb_notes + 1)) + note / (nb_notes + 1)
        # nb_notes += 1
        pass

    def commenter_recette(self, commentaire: str, recette: Recette):
        """
        Permet de commenter une recette

        Args:
            commentaire (str):
                Avis donné sur la recette
            recette (Recette):
                Recette que l'on veut commenter

        Raises:
            TypeError:
                Retournée si le commentaire n'est pas un str
            TypeError:
                Retournée si la recette n'est pas une instance de Recette
        """

        if not isinstance(commentaire, str):
            raise TypeError("Le commentaire doit être une chaîne de caractères")
        if not isinstance(recette, Recette):
            raise TypeError("La recette doit être une instance de Recette")

        pass

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

        return recette if RecetteDao().creer(recette) is False else None

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

        note_avis_str = f"Les avis de {recette.nom_recette} sont :\n\n"
        for av in recette.avis:
            note_avis_str += f"- {av}"
        note_avis_str += f"La note de cette recette est :\n\n"
        note_avis_str += str(recette.note)
        
        return note_avis_str

    def voir_recette(self, recette: Recette) -> str:
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
            raise TypeError("recette doit être une instance de Recette.")

        # Voir si ça marche bien comme ça. Sinon on passe par la DAO comme d'habitude.
        recette_str = f"La description de {recette.nom_recette} est :\n\n"
        recette_str += str(recette.description_recette)
        recette_str += f"Les ingrédients pour cette recette sont :\n\n"
        for ingr in recette.liste_ingredient:
            ingredient, quantites = ingr
            recette_str += f"- {ingredient.nom_ingredient} ({quantites})"

        return recette_str
