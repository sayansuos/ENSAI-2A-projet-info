class Ingredient:
    """
    Instancie un objet de type Ingredient
    """

    def __init__(self, nom_ingredient: str, id_ingredient: int = 1):
        self.id_ingredient: int = id_ingredient
        self.nom_ingredient: str = nom_ingredient

    def __str__(self):
        return f"[{self.id_ingredient}] {self.nom_ingredient}"
