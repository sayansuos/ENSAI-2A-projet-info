from src.classes.utilisateur import Utilisateur
from src.classes.recette import Recette
from src.classes.ingredient import Ingredient


class ListeFavorisService(Utilisateur):
    """
    Définis les méthodes permettant de modifier les listes de l'utilisateur
    concerné
    """

    def ajouter_favoris(self, recette: Recette) -> bool:
        """
        Ajoute une recette à la liste "recette_favorite" de l'utilisateur

        Args :
            recette (Recette) : Recette à ajouter à la liste

        Returns:
            bool: True si la recette a été ajoutée à la liste, False sinon
        """
        if not isinstance(recette, Recette):
            raise TypeError("recette doit être une instance de Recette")


        # Adapter le code suivant pour une éventuelle classe DAO
        if recette not in super.recette_favorite:
            super.recette_favorite.append(recette)
            return True
        return False

    def enlever_favoris(self, recette: Recette) -> bool:
        """
        Enlève une recette à la liste "recette_favorite" de l'utilisateur

        Args :
            recette (Recette) : Recette à enlever de la liste

        Returns:
            bool: True si la recette a été enlevée de la liste, False sinon
        """
        if not isinstance(recette, Recette):
            raise TypeError("recette doit être une instance de Recette")

        # Adapter le code suivant pour une éventuelle classe DAO
        if recette in super.recette_favorite:
            super.recette_favorite.remove(recette)
            return True
        return False

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
