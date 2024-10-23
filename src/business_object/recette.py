from business_object.ingredient import Ingredient


class Recette:
    """
    Instancie un objet de type Recette
    """

    def __init__(
        self,
        nom_recette: str,
        liste_ingredient: list[list[Ingredient, str]],
        description_recette: str,
        id_recette: int = 1,
        note: float = None,
        avis: list[str] = [],
    ):
        self.id_recette: int = id_recette
        self.nom_recette: str = nom_recette
        self.liste_ingredient: list[list[Ingredient, str]] = liste_ingredient
        self.liste_ingredient: list[list[Ingredient, str]] = liste_ingredient
        self.description_recette: str = description_recette
        self.note: float = note
        self.avis: list[str] = avis
