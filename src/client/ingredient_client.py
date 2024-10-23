import os
from dotenv import load_dotenv
import requests

from typing import List


class IngredientClient:
    """Make call to the ingredient endpoint"""

    def __init__(self) -> None:
        self.__host = os.environ["WEBSERVICE_HOST"]

    def get_all_ingredients(self) -> List[str]:
        """
        Returns list of all ingredients
        """
        # Appel du Web service
        req = requests.get(f"{self.__host}/list.php?i=list")

        # Création d'une liste puis parcours du json pour ajouter tous
        # les ingrédients à la liste
        all_ingredients = []
        if req.status_code == 200:
            raw_types = req.json()["meals"]
            for t in raw_types:
                all_ingredients.append([int(t["idIngredient"]), t["strIngredient"]])

        return sorted(all_ingredients)
