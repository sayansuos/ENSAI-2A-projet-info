from business_object.ingredient import Ingredient


class Recette:
    """
    Cette classe représente une recette avec un nom, un identifiant, une liste d'ingrédient,
    une description, une note et une liste d'avis.
    """

    def __init__(
        self,
        nom_recette: str,
        liste_ingredient: list[list[Ingredient, str]],
        description_recette: str,
        id_recette: int,
        note: float = None,
        avis: list[str] = [],
    ):
        """
        Cette méthode instancie une Recette.

        Args
        ----
            id_recette (int):
                Identifiant de la recette
            nom_recette (str):
                Nom de la recette
            liste_ingredient (list[Ingredient, str]):
                Liste des ingrédients de la recette et des quantités associées
            description_recette (str):
                Description de la recette
            note (float):
                Note de la recette
            avis (list[str]):
                Liste des avis de la recette

        """
        self.id_recette: int = id_recette
        self.nom_recette: str = nom_recette
        self.liste_ingredient: list[list[Ingredient, str]] = liste_ingredient
        self.description_recette: str = description_recette
        self.note: float = note
        self.avis: list[str] = avis

    def __str__(self):
        """
        Affichage d'une recette
        """
        return f"[{self.id_recette}] {self.nom_recette}"
