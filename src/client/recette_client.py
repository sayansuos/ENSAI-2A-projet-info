import os
from dotenv import load_dotenv
import requests
import string

from typing import List


class RecetteClient:
    """Make call to the recipe endpoint"""

    def __init__(self) -> None:
        self.__host = os.environ["WEBSERVICE_HOST"]

    def get_all_recipes(self) -> List[str]:
        """
        Returns list of all recipes
        """

        all_recipes = []

        # Appel du Web service
        for letter in list(string.ascii_lowercase):
            req = requests.get(f"{self.__host}/search.php?f={letter}")

            # Création d'une liste puis parcours du json pour ajouter tous
            # les ingrédients à la liste
            if req.status_code == 200:
                raw_types = req.json()["meals"]
                if raw_types:
                    for t in raw_types:
                        id = int(t["idMeal"])
                        name = t["strMeal"]
                        strIngredient = []
                        qttIngredient = []
                        for i in range(1, 21):
                            if t["strIngredient" + str(i)] and t["strIngredient" + str(i)] != "":
                                strIngredient.append(t["strIngredient" + str(i)])
                                qttIngredient.append(t["strMeasure" + str(i)])
                        ingredient = [
                            [strIngredient[i], qttIngredient[i]]
                            for i in range(0, len(strIngredient))
                        ]
                        description = t["strInstructions"]
                        recette = [id, name, ingredient, description]
                        all_recipes.append(recette)

        return sorted(all_recipes)


if __name__ == "__main__":
    load_dotenv()
    print(RecetteClient().get_all_recipes()[0:3])
