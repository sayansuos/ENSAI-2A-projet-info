class Ingredient:
    """
    Celle classe représente un ingrédient.

    Attributs
    ---------
    nom_ingredient : str
        Nom de l'ingrédient
    id_ingredient : int
        Identifiant de l'ingrédient
    """

    def __init__(self, nom_ingredient: str, id_ingredient: int = 1):
        """
        Constructeur
        """
        self.id_ingredient: int = id_ingredient
        self.nom_ingredient: str = nom_ingredient

    def __str__(self):
        """
        Cette méthode affiche un utilisateur.
        """
        return f"[{self.id_ingredient}] {self.nom_ingredient}"
