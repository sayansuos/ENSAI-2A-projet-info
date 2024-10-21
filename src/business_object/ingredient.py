class Ingredient:
    """
    Instancie un objet de type Ingredient
    """

    def __init__(self, id_ingredient: int, nom_ingredient: str):
        self.id_ingredient: int = id_ingredient
        self.nom_ingredient: str = nom_ingredient
