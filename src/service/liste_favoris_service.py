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
        Cette méthode renvoie la liste des recettes favorites de l'utilisateur.

        Parameters
        ----------
        utilisateur : Utilisateur
            Utilisateur à tester

        Returns
        -------
        list[Recette] :
            Liste des recettes favorites de l'utilisateur

        """
        # Vérification des attributs
        if not isinstance(utilisateur, Utilisateur):
            raise TypeError("utilisateur doit être une instance de Utilisateur")
        # Appel à la DAO
        return ListeFavorisDao().consulter_favoris(utilisateur=utilisateur)

    def ajouter_favoris(self, recette: Recette, utilisateur: Utilisateur) -> bool:
        """
        Cette méthode ajoute une recette aux favoris d'un utilisateur.

        Parameters
        ----------
        recette : Recette
            Recette à ajouter aux favoris
        utilisateur : Utilisateur
            Utilisateur à modifier

        Returns
        -------
        bool :
            True si la recette a été rajoutée aux favoris de l'utilisateur, False sinon

        """
        # Vérification des attributs
        if not isinstance(recette, Recette):
            raise TypeError("recette doit être une instance de Recette")
        if not isinstance(utilisateur, Utilisateur):
            raise TypeError("utilisateur doit être une instance de Utilisateur")

        # Appel à la DAO
        added = False
        if not ListeFavorisDao().est_dans_favoris(recette=recette, utilisateur=utilisateur):
            ListeFavorisDao().ajouter_favoris(recette=recette, utilisateur=utilisateur)
            added = True

        return added

    def retirer_favoris(self, recette: Recette, utilisateur: Utilisateur) -> bool:
        """
        Cette méthode retire une recette des favoris d'un utilisateur.

        Parameters
        ----------
        recette : Recette
            Recette à retirer des favoris
        utilisateur : Utilisateur
            Utilisateur à modifier

        Returns
        -------
        bool :
            True si la recette a été retirée favoris de l'utilisateur, False sinon

        """
        # Vérification des attributs
        if not isinstance(recette, Recette):
            raise TypeError("recette doit être une instance de Recette")
        if not isinstance(utilisateur, Utilisateur):
            raise TypeError("utilisateur doit être une instance de Utilisateur")

        # Appel à la DAO
        deleted = False
        if ListeFavorisDao().est_dans_favoris(recette=recette, utilisateur=utilisateur):
            ListeFavorisDao().retirer_favoris(recette=recette, utilisateur=utilisateur)
            deleted = True

        return deleted

    def consulter_liste_course(self, utilisateur: Utilisateur) -> list[Ingredient]:
        """
        Cette méthode renvoie les ingrédients de la liste de course de l'utilisateur.

        Parameters
        ----------
        utilisateur : Utilisateur
            Utilisateur à consulter

        Returns
        -------
        list[Ingredient, Recette] :
            Liste des ingrédients de la liste de courses et la recette associée

        """
        # Vérification des attributs
        if not isinstance(utilisateur, Utilisateur):
            raise TypeError("utilisateur doit être une instance de Utilisateur")
        # Appel à la DAO
        liste_course = ListeFavorisDao().consulter_liste_course(utilisateur=utilisateur)
        return liste_course

    def ajouter_liste_course(self, recette: Recette, utilisateur: Utilisateur) -> bool:
        """
        Cette méthode ajoute les ingrédients d'une recette à la liste de course d'un utilisateur.

        Parameters
        ----------
        recette : Recette
            Recette dont on doit ajouter les ingrédients
        utilisateur : Utilisateur
            Utilisateur à modifier

        Returns
        -------
        bool :
            True si les ingrédients ont été rajouté, False sinon

        """
        # Vérification des attributs
        if not isinstance(recette, Recette):
            raise TypeError("ingredient doit être une instance d'Ingredient")
        if not isinstance(utilisateur, Utilisateur):
            raise TypeError("utilisateur doit être une instance de Utilisateur")
        # Appel à la DAO
        added = False
        added = ListeFavorisDao().ajouter_liste_course(recette=recette, utilisateur=utilisateur)
        return added

    def retirer_liste_course(
        self, recette: Recette, ingredient: Ingredient, utilisateur: Utilisateur
    ) -> bool:
        """
        Cette méthode retire un ingrédient de la liste de course de l'utilisateur.

        Parameters
        ----------
        ingredient : Ingredient
            Ingrédient à retirer de la liste de course
        recette : Recette
            Recette associée à l'ingrédient
        utilisateur : Utilisateur
            Utilisateur à modifier

        Returns
        -------
        bool :
            True si l'ingrédient a été retiré de la liste de course, False sinon

        """
        # Vérification des attributs
        if not isinstance(recette, Recette):
            raise TypeError("recette doit être une instance de Recette")
        if not isinstance(ingredient, Ingredient):
            raise TypeError("ingredient doit être une instance d'Ingredient")
        if not isinstance(utilisateur, Utilisateur):
            raise TypeError("utilisateur doit être une instance de Utilisateur")

        # Appel à la DAO
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
        Cette méthode permet de consulter les ingrédients favoris de l'utilisateur.

        Parameters
        ----------
        utilisateur : Utilisateur
            Utilisateur à tester

        Returns
        -------
        list[Ingredient] :
            Liste des ingrédients favoris de l'utilisateur

        """
        # Vérification des attributs
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
        Cette méthode permet de consulter les ingrédients non-désirés de l'utilisateur.

        Parameters
        ----------
        utilisateur : Utilisateur
            Utilisateur à tester

        Returns
        -------
        list[Ingredient] :
            Liste des ingrédients non-désirés de l'utilisateur

        """
        # Vérification des attribus
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
        Cette méthode permet de modifier la préférence concernant un ingrédient de l'utilisateur.

        Parameters
        ----------
        ingredient : Ingredient
            Ingrédient à modifier
        utilisateur : Utilisateur
            Utilisateur à modifier

        Returns
        -------
        bool :
            True si la préférence ingrédient de l'utilisateur a été modifiée, False sinon

        """
        # Vérification des attributs
        if not isinstance(utilisateur, Utilisateur):
            raise TypeError("utilisateur doit être une instance de Utilisateur")
        if not isinstance(ingredient, Ingredient):
            raise TypeError("ingredient doit être une instance de Ingredient")
        if not isinstance(modif, str) and modif is not None:
            raise TypeError("modif doit être une instance de str")
        if modif != "F" and modif != "ND" and modif is not None:
            raise TypeError("modif doit être 'F', 'ND' ou None.")

        # Appel à la DAO
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
        Cette méthode permet de retirer un ingrédient des préférences.

        Parameters
        ----------
        ingredient : Ingredient
            Ingrédient à retirer
        utilisateur : Utilisateur
            Utilisateur à modifier

        Returns
        -------
        Bool :
            True si la préférence ingrédient a été retirée, False sinon

        """
        # Vérification des attributs
        if not isinstance(utilisateur, Utilisateur):
            raise TypeError("utilisateur doit être une instance de Utilisateur")
        if not isinstance(ingredient, Ingredient):
            raise TypeError("ingredient doit être une instance de Ingredient")

        # Appel à la DAO
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
        Cette méthode renvoie une liste de 10 recettes qui ne sont pas dans les favoris mais qui
        contiennent au moins un ingrédient favori et aucun non-désiré.

        Parameters
        ----------
        utilisateur : Utilisateur
            Utilisateur à qui on suggère des recettes

        Returns
        -------
        list[Recette] :
            Liste des recettes suggérées pour l'utilisateur
        """
        # Vérification des attributs
        if not isinstance(utilisateur, Utilisateur):
            raise TypeError("utilisateur doit être une instance de Utilisateur")

        # Appel à la DAO pour obtenir les préférences ingrédients
        liste_favoris = ListeFavorisDao().consulter_preference_ingredient_favori(
            utilisateur=utilisateur
        )
        liste_non_desires = ListeFavorisDao().consulter_preference_ingredient_non_desire(
            utilisateur=utilisateur
        )

        # Construction des listes de recettes associées aux préférences ingrédients
        avec_ing_fav = []
        avec_ing_nd = []
        recette_fav = self.consulter_favoris(utilisateur=utilisateur)
        for ingr_fav in liste_favoris:
            avec_ing_fav += RecetteService().trouver_recette_par_ingredient(ingredient=ingr_fav)
        for ingr_nd in liste_non_desires:
            avec_ing_nd += RecetteService().trouver_recette_par_ingredient(ingredient=ingr_nd)

        # Construction de la liste des recettes suggérées
        # On garde les recettes qui contiennent un ingrédient préférence en excluant celle qui sont
        # les favoris ou qui ont un ingrédient non-désiré
        suggestion = []
        for recette in avec_ing_fav:
            if recette not in avec_ing_nd and recette not in recette_fav:
                suggestion.append(recette)

        return suggestion
