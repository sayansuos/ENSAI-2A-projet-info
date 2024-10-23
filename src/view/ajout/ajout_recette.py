import regex

from InquirerPy import inquirer
from InquirerPy.validator import PasswordValidator, EmptyInputValidator

from prompt_toolkit.validation import ValidationError, Validator

from src.business_object.recette import Recette
from view.vue_abstraite import VueAbstraite
from src.service.recette_service import RecetteService


class AjoutRecetteVue(VueAbstraite):
    def choisir_menu(self):
        # Demande à l'administrateur de saisir nom de la recette, description et liste des ingredients
        nom_recette = inquirer.text(message="Quel est le nom de la recette ? : ").execute()

        if RecetteService().recette_deja_faite(nom_recette):
            from src.view.users.menu_admin_vue import MenuAdminVue

            return MenuAdminVue(f"La recette {nom_recette} a déjà été créée.")

        description_recette = inquirer.text(
            message="Donnez une description : "
        ).execute()

        nb_ingredients = inquirer.number(message="Combien il y a d'ingrédients ? : ")

        liste_ingredients = []

        for i in range(liste_ingredients):
            ingredients = inquirer.text(message=f"Entrez l'ingrédient {i+1} : ")
            liste_ingredients.append(ingredients)

        # Appel du service pour créer la recette

        la_recette = Recette(nom_recette, description_recette, liste_ingredients)
        recette = RecetteService().creer_recette(la_recette)

        # Si le joueur a été créé
        if recette:
            message = (
                f"La recette a été créée."
            )
        else:
            message = "Erreur"

        from src.view.users.menu_admin_vue import MenuAdminVue

        return MenuAdminVue(message)
