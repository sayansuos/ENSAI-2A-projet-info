from src.business_object.utilisateur import Utilisateur
from src.business_object.recette import Recette
from src.business_object.ingredient import Ingredient

from src.dao.liste_favoris_dao import ListeFavorisDao


class ListeFavorisService:
    """
    Définis les méthodes permettant de modifier les listes de l'utilisateur concerné
    """

    def ajouter_favoris(self, recette: Recette, utilisateur: Utilisateur) -> bool:
        """
        Ajoute un ingrédient à la liste des favoris.

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

        if recette not in utilisateur.recette_favorite:
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
            raise TypeError("recette doit être une instance de Recette")

        deleted = False

        if recette in utilisateur.recette_favorite:
            ListeFavorisDao().retirer_favoris(recette=recette, utilisateur=utilisateur)
            deleted = True

        return deleted

    def ajouter_ingredient_course(self, ingredient: Ingredient) -> bool:
        """
        Ajoute un ingrédient à la liste "liste_de_course" de l'utilisateur

        Args :
            ingredient (Ingredient) : Ingrédient à ajouter à la liste

        Returns:
            bool: True si l'ingrédient a été ajoutée à la liste, False sinon
        """
        if not isinstance(ingredient, Ingredient):
            raise TypeError("ingredient doit être une instance d'Ingredient")

        # Adapter le code suivant pour une éventuelle classe DAO
        if ingredient not in super.liste_de_course:
            super.liste_de_course.append(ingredient)
            return True
        return False

    def enlever_ingredient_course(self, ingredient: Ingredient) -> bool:
        """
        Enlève un ingrédient à la liste "liste_de_course" de l'utilisateur

        Args :
            ingredient (Ingredient) : Ingrédient à enlever de la liste

        Returns:
            bool: True si l'ingrédient a été enlevée de la liste, False sinon
        """
        if not isinstance(ingredient, Ingredient):
            raise TypeError("ingredient doit être une instance d'Ingredient")

        # Adapter le code suivant pour une éventuelle classe DAO
        if ingredient in super.liste_de_course:
            super.liste_de_course.remove(ingredient)
            return True
        return False

    def ajouter_ingredient_favori(self, ingredient: Ingredient) -> bool:
        """
        Ajoute un ingrédient à la liste "ingredient_favori" de l'utilisateur

        Args :
            ingredient (Ingredient) : Ingrédient à ajouter à la liste

        Returns:
            bool: True si l'ingrédient a été ajoutée à la liste, False sinon
        """
        if not isinstance(ingredient, Ingredient):
            raise TypeError("ingredient doit être une instance d'Ingredient")

        # Adapter le code suivant pour une éventuelle classe DAO
        if ingredient not in super.ingredient_favori:
            super.ingredient_favori.append(ingredient)
            return True
        return False

    def enlever_ingredient_favori(self, ingredient: Ingredient) -> bool:
        """
        Enlève un ingrédient à la liste "ingredient_favori" de l'utilisateur

        Args :
            ingredient (Ingredient) : Ingrédient à enlever de la liste

        Returns:
            bool: True si l'ingrédient a été enlevée de la liste, False sinon
        """
        if not isinstance(ingredient, Ingredient):
            raise TypeError("ingredient doit être une instance d'Ingredient")

        # Adapter le code suivant pour une éventuelle classe DAO
        if ingredient in super.ingredient_favori:
            super.ingredient_favori.remove(ingredient)
            return True
        return False

    def ajouter_ingredient_non_desire(self, ingredient: Ingredient) -> bool:
        """
        Ajoute un ingrédient à la liste "ingredient_non_desire" de l'utilisateur

        Args :
            ingredient (Ingredient) : Ingrédient à ajouter à la liste

        Returns:
            bool: True si l'ingrédient a été ajoutée à la liste, False sinon
        """
        if not isinstance(ingredient, Ingredient):
            raise TypeError("ingredient doit être une instance d'Ingredient")

        # Adapter le code suivant pour une éventuelle classe DAO
        if ingredient not in super.ingredient_non_desire:
            super.ingredient_non_desire.append(ingredient)
            return True
        return False

    def enlever_ingredient_non_desire(self, ingredient: Ingredient) -> bool:
        """
        Enlève un ingrédient à la liste "ingredient_non_desire" de l'utilisateur

        Args :
            ingredient (Ingredient) : Ingrédient à enlever de la liste

        Returns:
            bool: True si l'ingrédient a été enlevée de la liste, False sinon
        """
        if not isinstance(ingredient, Ingredient):
            raise TypeError("ingredient doit être une instance d'Ingredient")

        # Adapter le code suivant pour une éventuelle classe DAO
        if ingredient in super.ingredient_non_desire:
            super.ingredient_non_desire.remove(ingredient)
            return True
        return False
