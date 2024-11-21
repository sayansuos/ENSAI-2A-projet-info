from typing import List, Optional

from business_object.ingredient import Ingredient
from business_object.recette import Recette

from dao.recette_dao import RecetteDao

from view.session import Session


class RecetteService:
    """
    Définis les méthodes de la classe Recette
    """

    def trouver_recette_par_id(self, id: int) -> Optional[Recette]:
        """
        Cette méthode permet de trouver une recette grace à son identifiant.

        Parameters
        ----------
        id_recette : int
            Identifiant de la recette que l'on souhaite trouver

        Returns
        -------
        Recette :
            Recette que l'on souhaite trouver
        """
        # Vérification des attributs
        if not isinstance(id, int):
            raise TypeError("id doit être une instance de int")
        # Appel à la DAO
        return RecetteDao().trouver_par_id(id)

    def trouver_recette_par_nom(self, nom: str) -> Optional[Recette]:
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
        # Vérification des attributs
        if not isinstance(nom, str):
            raise TypeError("nom doit être une instance de str")
        # Appel à la DAO
        return RecetteDao().trouver_par_nom(nom)

    def trouver_recette_par_ingredient(self, ingredient: Ingredient) -> List[Recette]:
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
        # Vérification des attributs
        if not isinstance(ingredient, Ingredient):
            raise TypeError("ingredient doit être une instance de Ingredient")
        # Appel à la DAO
        return RecetteDao().trouver_par_ingredient(ingredient)

    def lister_toutes_recettes(self) -> List[Recette]:
        """
        Cette méthode permet de lister toutes les recettes de la base de données.

        Returns
        -------
        list[Recette] :
            Liste des recettes de la base de données.
        """
        # Appel à la liste chargée en session
        return Session().liste_recettes

    def creer_recette(self, recette: Recette) -> Optional[Recette]:
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
        # Vérification des attributs
        if not isinstance(recette, Recette):
            raise TypeError("reccette doit être une instance de Recette")
        # Ajout de la recette dans la liste chargée
        Session().liste_recettes.append(recette)
        # Appel à la DAO
        return recette if RecetteDao().creer(recette) is True else None

    def supprimer_recette(self, recette: Recette) -> bool:
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
        # Vérification des attributs
        if not isinstance(recette, Recette):
            raise TypeError("reccette doit être une instance de Recette")
        # Suppression de la recette dans la liste chargée
        Session().liste_recettes.remove(recette)
        # Appel à la DAO
        return RecetteDao().supprimer(recette)

    def voir_note_avis(self, recette: Recette):
        """
        Cette méthode affiche les notes et avis d'une recette.

        Parameters
        ----------
        recette : Recette
            Recette dont on doit afficher la note et les avis

        """
        # Vérification des attributs
        if not isinstance(recette, Recette):
            raise TypeError("recette doit être une instance de Recette.")

        # Affichage selon si il y a des avis ou non
        print(f"\n\n*** [ {recette.nom_recette} ] ***")
        print(f"Id : {recette.id_recette}\n")
        if recette.avis[0] == "" and recette.note is None:
            print("There is no rewiew or rating for this recipe.")
        else:
            print(f"Rate: {recette.note}/5\n")
            print("Rewiews:\n")
            for a in recette.avis:
                print(f" - {a}")
        print("\n\n")

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
        # Vérification des attributs
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

        # Suppression dans la liste chargée
        Session().liste_recettes.remove(recette)
        # Appel à la DAO
        modified = RecetteDao().ajouter_note_et_com(recette=recette, note=note, com=com)
        update = self.trouver_recette_par_id(recette.id_recette)
        # Ajout de la recette modifiée dans la liste chargée
        Session().liste_recettes.append(update)
        return modified

    def lire_recette(self, recette: Recette):
        """
        Cette méthode affiche la recette et ses attributs.

        Parameters
        ----------
        recette : Recette
            Recette dont on doit afficher les attributs.

        """
        # Vérification des attributs
        if not isinstance(recette, Recette):
            raise TypeError("recette doit être une instance de Recette.")

        # Affichage
        print(f"\n\n*** [ {recette.nom_recette} ] ***")
        print(f"Id : {recette.id_recette}")
        print("\nList of ingredients:\n")
        for ingr in recette.liste_ingredient:
            ingredient, quantite = ingr
            print(f" - {ingredient} ({quantite})")
        print(f"\nDescription: \n\n{recette.description_recette}")
        print("\n\n")
