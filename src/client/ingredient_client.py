import os
import requests
from typing import List


class IngredientClient:
    """
    Cette classe permet d'appeler les données de l'endpoint des ingrédients.
    """

    def __init__(self) -> None:
        """
        Constructeur
        """
        self.__host = os.environ["WEBSERVICE_HOST"]

    def get_all_ingredients(self) -> List[str]:
        """
        Cette méthode retourne la liste de tous les ingrédients.
        """
        # Appel du Web service
        req = requests.get(f"{self.__host}/list.php?i=list")

        # Création d'une liste puis parcours du json pour ajouter les ingrédients
        all_ingredients = []
        if req.status_code == 200:
            raw_types = req.json()["meals"]
            for t in raw_types:
                all_ingredients.append([int(t["idIngredient"]), t["strIngredient"]])

        return sorted(all_ingredients)
