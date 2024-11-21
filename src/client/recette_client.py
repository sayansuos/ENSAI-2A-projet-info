import os
import requests
import string
from typing import List


class RecetteClient:
    """
    Cette classe permet d'appeler les données de l'endpoint des ingrédients.
    """

    def __init__(self) -> None:
        self.__host = os.environ["WEBSERVICE_HOST"]

    def get_all_recipes(self) -> List[str]:
        """
        Cette méthode retourne la liste de tous les recettes.
        """

        all_recipes = []

        # Appel du Web service (boucle pour avoir toutes les recettes par lettre)
        for letter in list(string.ascii_lowercase):
            req = requests.get(f"{self.__host}/search.php?f={letter}")

            # Création d'une liste puis parcours du json pour ajouter les recettes
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
