from typing import List, Optional
from src.business_object.recette import Recette
from src.dao.recette_dao import RecetteDao


class RecetteService(Recette):
    """
    Définis les méthodes de la classe Recette
    """

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

    def trouver_recette_par_ingredient(self, ingredient: str) -> List[Recette]:
        """
        Permet de trouver une liste de recette contenant l'ingrédient entré
        en paramètre

        Args:
            ingredient (str):
                Nom de l'ingrédient recherché

        Returns:
            list[Recette]:
                Renvoie la liste des recettes contenant cet ingrédient
        """

        if not isinstance(ingredient, str):
            raise TypeError("ingredient doit être une instance de str")

        pass
        # return RecetteDao.trouver_par_ingredient(ingredient)

    def lister_toutes_recettes(self) -> List[Recette]:
        """
        Renvoie une liste de toutes les recettes existantes.

        Returns:
            list[Recette]:
                Liste de toutes les recettes existantes
        """

        return RecetteDao.lister_tous()

    def noter_recette(self, note: float):
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

        # super.note = super.note * (nb_notes / (nb_notes + 1)) + note / (nb_notes + 1)
        # nb_notes += 1
        pass

    def commenter_recette(self, commentaire: str):
        """
        Permet de commenter une recette

        Args:
            commentaire (str):
                Avis de l'utilisateur sur la recette
        """

        if not isinstance(commentaire, str):
            raise TypeError("Le commentaire doit être une chaîne de caractères")

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

        return recette if RecetteDao.creer(recette) is False else None

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

        return RecetteDao.supprimer(recette)

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

        return RecetteDao.trouver_par_id(id)

    def voir_avis(self, recette: Recette) -> [List[str]]:
        """
        Permet de voir les avis d'une recette

        Args:
            recette (Recette):
                Recette dont on veut voir les avis

        Returns:
            [List[str]]:
                Liste des avis des utilisateurs sur la recette
        """

        if not isinstance(recette, Recette):
            raise TypeError("recette doit être une instance de Recette.")

        return RecetteDao.voir_avis(recette)

    def voir_note(self, recette: Recette) -> Optional[float]:
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

        return RecetteDao.voir_note(recette)

    def voir_description(self, recette: Recette) -> str:
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
        return super.description
