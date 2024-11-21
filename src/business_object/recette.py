from business_object.ingredient import Ingredient


class Recette:
    """
    Cette classe représente une recette.

    Attributes
    ----------
    nom_recette : str
        Nom de la recette
    liste_ingredient : list[list[Ingredient, str]]
        Liste de couples constitués par les ingrédients de la recette et la quantitée associée
    description_recette : str
        Description de la recette
    id_recette : int
        Identifiant de la recette
    note : float
        Note associée à la recette
    avis : list[str]
        Liste des avis associés à la recette
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
        Constructeur
        """
        self.id_recette: int = id_recette
        self.nom_recette: str = nom_recette
        self.liste_ingredient: list[list[Ingredient, str]] = liste_ingredient
        self.description_recette: str = description_recette
        self.note: float = note
        self.avis: list[str] = avis

    def __str__(self):
        """
        Cette méthode affiche une recette.
        """
        return f"[{self.id_recette}] {self.nom_recette}"
