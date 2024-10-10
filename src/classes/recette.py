class Recette:
    """
    Instancie un objet de type Recette
    """

    def __init__(self, id_recette: int, nom_recette: str, liste_ingredient: list[list[str, str]]):
        self.id_recette: int = id_recette
        self.nom_recette: str = nom_recette
        self.liste_ingredient: list[list[str, str]] = liste_ingredient
