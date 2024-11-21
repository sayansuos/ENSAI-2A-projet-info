from business_object.utilisateur import Utilisateur
from business_object.recette import Recette
from business_object.ingredient import Ingredient

from dao.liste_favoris_dao import ListeFavorisDao
from service.recette_service import RecetteService


class ListeFavorisService:
    """
    Définis les méthodes permettant de modifier les listes de l'utilisateur concerné
    """

    def consulter_favoris(self, utilisateur: Utilisateur) -> list[Recette]:
        """
            Liste les recettes favorites de l'utilisateur.

        Args :
            utilisateur (Utilisateur) : utilisateur dont on souhaite consulter les favoris

        Returns:
            liste_favoris : liste des recettes favorites
        """
        if not isinstance(utilisateur, Utilisateur):
            raise TypeError("utilisateur doit être une instance de Utilisateur")

        return ListeFavorisDao().consulter_favoris(utilisateur=utilisateur)

    def ajouter_favoris(self, recette: Recette, utilisateur: Utilisateur) -> bool:
        """
        Ajoute une recette à la liste des favoris.

        Args :
            recette (Recette) : recette à ajouter à la liste
            utilisateur (Utilisateur) : utilisateur à qui on ajoute la recette favorite

        Returns:
            Bool : True si la recette a été ajoutée à la liste, False sinon
        """

        if not isinstance(recette, Recette):
            raise TypeError("recette doit être une instance de Recette")
        if not isinstance(utilisateur, Utilisateur):
            raise TypeError("utilisateur doit être une instance de Utilisateur")

        added = False

        if not ListeFavorisDao().est_dans_favoris(recette=recette, utilisateur=utilisateur):
            ListeFavorisDao().ajouter_favoris(recette=recette, utilisateur=utilisateur)
            added = True

        return added

    def retirer_favoris(self, recette: Recette, utilisateur: Utilisateur) -> bool:
        """
        Retirer une recette de la liste des favoris.

        Args :
            recette (Recette) : Recette à enlever de la liste
            utilisateur (Utilisateur) : utilisateur à qui on retire la recette favorite

        Returns:
            Bool : True si la recette a été enlevée de la liste, False sinon
        """
        if not isinstance(recette, Recette):
            raise TypeError("recette doit être une instance de Recette")
        if not isinstance(utilisateur, Utilisateur):
            raise TypeError("utilisateur doit être une instance de Utilisateur")

        deleted = False

        if ListeFavorisDao().est_dans_favoris(recette=recette, utilisateur=utilisateur):
            ListeFavorisDao().retirer_favoris(recette=recette, utilisateur=utilisateur)
            deleted = True

        return deleted

    def consulter_liste_course(self, utilisateur: Utilisateur) -> list[Ingredient]:
        """
        Liste les ingrédients de la liste de course de l'utilisateur.

        Args :
            utilisateur (Utilisateur) : utilisateur dont on souhaite consulter la liste de course

        Returns:
            liste_course : liste des ingrédients de la liste de course
        """
        if not isinstance(utilisateur, Utilisateur):
            raise TypeError("utilisateur doit être une instance de Utilisateur")

        liste_course = ListeFavorisDao().consulter_liste_course(utilisateur=utilisateur)
        return liste_course

    def ajouter_liste_course(self, recette: Recette, utilisateur: Utilisateur) -> bool:
        """
        Ajoute tous les ingrédients de la recette à la liste "liste_de_course" de l'utilisateur

        Args :
            recette (Recette) : recette dont on ajoute les ingrédients à la liste
            utilisateur (Utilisateur) : utilisateur à qui on modifie la liste de course

        Returns:
            bool: True si les ingrédients ont été ajouté à la liste , False sinon
        """
        if not isinstance(recette, Recette):
            raise TypeError("ingredient doit être une instance d'Ingredient")
        if not isinstance(utilisateur, Utilisateur):
            raise TypeError("utilisateur doit être une instance de Utilisateur")

        added = False
        added = ListeFavorisDao().ajouter_liste_course(recette=recette, utilisateur=utilisateur)
        return added

    def retirer_liste_course(
        self, recette: Recette, ingredient: Ingredient, utilisateur: Utilisateur
    ) -> bool:
        """
        Enlève tous les ingrédients de la recette à la liste "liste_de_course" de l'utilisateur

        Args :
            recette (Recette) : recette dont on retire les ingrédients à la liste
            utilisateur (Utilisateur) : utilisateur à qui on modifie la liste de course

        Returns:
            bool: True si les ingrédients ont été retiré à la liste, False sinon
        """
        if not isinstance(recette, Recette):
            raise TypeError("recette doit être une instance de Recette")
        if not isinstance(ingredient, Ingredient):
            raise TypeError("ingredient doit être une instance d'Ingredient")
        if not isinstance(utilisateur, Utilisateur):
            raise TypeError("utilisateur doit être une instance de Utilisateur")

        deleted = False

        if ListeFavorisDao().est_dans_liste_course(
            recette=recette, ingredient=ingredient, utilisateur=utilisateur
        ):
            ListeFavorisDao().retirer_liste_course(
                recette=recette, ingredient=ingredient, utilisateur=utilisateur
            )
            deleted = True

        return deleted

    def consulter_preference_ingredient_favori(self, utilisateur: Utilisateur) -> list[Ingredient]:
        """
        Liste les ingrédients favoris de l'utilisateur

        Args :
            utilisateur (Utilisateur) : utilisateur dont on souhaite consulter les préférences
        """
        if not isinstance(utilisateur, Utilisateur):
            raise TypeError("utilisateur doit être une instance de Utilisateur")

        # Appel à la DAO pour avoir la liste des ingrédients favoris
        fav = ListeFavorisDao().consulter_preference_ingredient_favori(utilisateur=utilisateur)
        utilisateur.ingredient_favori = fav

        # Affichage des ingrédients favoris
        print("\n\n*** Favourite ingredients ***\n\n")
        if len(fav) > 0:
            for ingr in fav:
                print(f" - {ingr}")
        else:
            print("There is no favourite ingredient registered.")
        print("\n\n")

    def consulter_preference_ingredient_non_desire(
        self, utilisateur: Utilisateur
    ) -> list[Ingredient]:
        """
        Liste les ingrédients non désirés de l'utilisateur

        Args :
            utilisateur (Utilisateur) : utilisateur dont on souhaite consulter les préférences

        """
        if not isinstance(utilisateur, Utilisateur):
            raise TypeError("utilisateur doit être une instance de Utilisateur")

        # Appel à la DAO pour avoir la liste des ingrédients non-désirés
        non_desires = ListeFavorisDao().consulter_preference_ingredient_non_desire(
            utilisateur=utilisateur
        )
        utilisateur.ingredient_non_desire = non_desires

        # Affichage des ingrédients non-désirés
        print("\n\n*** Unwanted ingredients ***\n\n")
        if len(non_desires) > 0:
            for ingr in non_desires:
                print(f"- {ingr}")
        else:
            print("There is no unwanted ingredient registered.")
        print("\n\n")

    def modifier_preference_ingredient(
        self, ingredient: Ingredient, utilisateur: Utilisateur, modif: str
    ) -> bool:
        """
        Modifie les préférences liées à un ingrédient :
            modif = 'F' : l'ingrédient est ajouté aux favoris
            modif = 'ND' : l'ingrédient est ajouté aux non-désirés
            modif = None : l'ingredient est ni favori, ni désiré.

        Args :
            utilisateur (Utilisateur) : utilisateur dont on souhaite modifier les préférences

        Returns:
            bool : True si les préférences liées à l'ingrédient ont bien été modifié, False sinon
        """
        if not isinstance(utilisateur, Utilisateur):
            raise TypeError("utilisateur doit être une instance de Utilisateur")
        if not isinstance(ingredient, Ingredient):
            raise TypeError("ingredient doit être une instance de Ingredient")
        if not isinstance(modif, str) and modif is not None:
            raise TypeError("modif doit être une instance de str")
        if modif != "F" and modif != "ND" and modif is not None:
            raise TypeError("modif doit être 'F', 'ND' ou None.")

        modified = False

        if ListeFavorisDao().est_dans_preference_ingredient(
            ingredient=ingredient, utilisateur=utilisateur
        ):
            ListeFavorisDao().retirer_preference_ingredient(
                ingredient=ingredient, utilisateur=utilisateur
            )
            ListeFavorisDao().modifier_preference_ingredient(
                ingredient=ingredient, utilisateur=utilisateur, modif=modif
            )
            modified = True

        if not ListeFavorisDao().est_dans_preference_ingredient(
            ingredient=ingredient, utilisateur=utilisateur
        ):
            ListeFavorisDao().modifier_preference_ingredient(
                ingredient=ingredient, utilisateur=utilisateur, modif=modif
            )
            modified = True

        return modified

    def retirer_preference_ingredient(
        self, ingredient: Ingredient, utilisateur: Utilisateur
    ) -> bool:
        """
        Retire un ingrédient à la liste des préférences

        Args :
            ingredient (Ingredient) : ingredient qu'on souhaite retirer des préférences
            utilisateur (Utilisateur) : utilisateur à qui on modifie la liste de course

        Returns:
            bool: True si l'ingrédients a bien été retiré à la table, False sinon
        """

        if not isinstance(utilisateur, Utilisateur):
            raise TypeError("utilisateur doit être une instance de Utilisateur")
        if not isinstance(ingredient, Ingredient):
            raise TypeError("ingredient doit être une instance de Ingredient")

        deleted = False

        if ListeFavorisDao().est_dans_preference_ingredient(
            ingredient=ingredient, utilisateur=utilisateur
        ):
            ListeFavorisDao().retirer_preference_ingredient(
                ingredient=ingredient, utilisateur=utilisateur
            )
            deleted = True

        return deleted

    def consulter_suggestion(self, utilisateur: Utilisateur) -> list[Recette]:
        """
        Renvoie une liste de 10 recettes qui ne sont pas dans les favoris mais qui contiennent au
        moins un ingrédient favori et aucun non-désiré.

        Args :
            utilisateur (Utilisateur) : utilisateur à qui on modifie la liste de course

        Returns:
            bool: True si l'ingrédients a bien été retiré à la table, False sinon
        """
        liste_favoris = ListeFavorisDao().consulter_preference_ingredient_favori(
            utilisateur=utilisateur
        )
        liste_non_desires = ListeFavorisDao().consulter_preference_ingredient_non_desire(
            utilisateur=utilisateur
        )

        avec_ing_fav = []
        avec_ing_nd = []
        recette_fav = self.consulter_favoris(utilisateur=utilisateur)

        for ingr_fav in liste_favoris:
            avec_ing_fav += RecetteService().trouver_recette_par_ingredient(ingredient=ingr_fav)

        for ingr_nd in liste_non_desires:
            avec_ing_nd += RecetteService().trouver_recette_par_ingredient(ingredient=ingr_nd)

        suggestion = []
        for recette in avec_ing_fav:
            if recette not in avec_ing_nd and recette not in recette_fav:
                suggestion.append(recette)

        return suggestion
