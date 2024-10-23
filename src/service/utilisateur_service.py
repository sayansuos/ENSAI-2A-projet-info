from src.business_object.utilisateur import Utilisateur
from src.service.recette_service import RecetteService
from src.business_object.recette import Recette
from src.business_object.ingredient import Ingredient
from src.dao.utilisateur_dao import UtilisateurDAO

from utils.log_decorator import log
from utils.securite import hash_password
from typing import List, Optional


class UtilisateurService(Utilisateur):
    """
    Définis les méthodes de la classe Utilisateur
    """

    @log
    def pseudo_deja_utilise(self, pseudo: str) -> bool:
        """
        Vérifie si le pseudo entré est déjà utilisé dans la base de données.

        Args:
            pseudo (str): Pseudo voulu par l'utilisateur

        Returns:
            bool: True si le pseudo est déjà utilisé. False sinon
        """
        utilisateurs = UtilisateurDAO().lister_tous()
        return pseudo in [i.pseudo for i in utilisateurs]

    @log
    def creer(self, pseudo: str, mdp: str, mail: str) -> Utilisateur:
        """
        Créer un utilisateur selon les paramètres renseignés.

        Args:
            pseudo (str): Pseudo voulu pour l'utilisateur
            mdp (str): Mot de passe voulu pour l'utilisateur
            mail (str): Adresse mail voulue pour l'utilisateur

        Raises:
            TypeError: pseudo doit être une str
            TypeError: mdr doit être une str
            TypeError: mail doit être une str
            ValueError: mdr doit contenir plus de 6 caractères
            ValueError: Il faut un "@" dans mail
            ValueError: Il ne doit y avoir qu'un seul "@" dans mail
            ValueError: Il doit y avoir un point après le "@" dans mail

        Returns:
            Utilisateur: Retourne l'utilisateur crée
        """
        if not isinstance(pseudo, str):
            raise TypeError("Le pseudo doit être une chaîne de caractères alphanumériques.")
        if not isinstance(mdp, str):
            raise TypeError("Le mot de passe doit être une chaîne de caractères alphanumériques.")
        if not isinstance(mail, str):
            raise TypeError(
                "L'adresse mail doit être une chaîne de caractères sous la"
                " forme : 'blabla@domaine.truc'"
            )
        if len(mdp) < 6:
            raise ValueError("Le mot de passe doit contenir au moins 6 caractères.")
        if "@" not in mail:
            raise ValueError(
                "Il n'y a pas de @ dans l'adresse mail renseignée."
                "Format attendu : 'blabla@domaine.truc'"
            )
        for i in range(len(mail)):
            if mail[i] == "@":
                domaine_mail = mail[i : len(mail)]
                break
        if "@" in domaine_mail:
            raise ValueError(
                "Il ne doit y avoir qu'un seul @ dans votre adresse mail."
                "Format attendu : 'blabla@domaine.truc'"
            )
        if "." not in domaine_mail:
            raise ValueError(
                "Il doit y avoir un '.' dans votre nom de domaine."
                "Format attendu : 'blabla@domaine.truc'"
            )
        if ("'" in pseudo) or ("&" in pseudo) or ("|" in pseudo) or ("-" in pseudo):
            raise ValueError(
                "Le pseudo ne doit pas contenir de caractères spéciaux."
                "Caractères interdits : &, |, ', -"
            )
        if ("'" in mdp) or ("&" in mdp) or ("|" in mdp) or ("-" in mdp):
            raise ValueError(
                "Le mot de passe ne doit pas contenir de caractères spéciaux."
                "Caractères interdits : &, |, ', -"
            )
        if Utilisateur.pseudo_deja_utilise(pseudo):
            raise ValueError("Le pseudo a déjà été attribué.")

        # Pour finir la fonction :
        # - Définir des méthodes de sécurité (échappement des caractères spéciaux)
        #   (commencé un peu mais à voir si c'est suffisant)
        # - Définir un id non attribué (prendre le dernier id de la table
        #   Utilisateur et ajouter 1)
        # - Hacher le mot de passe (et utiliser l'id, le pseudo ou le mail comme sel)

        # Ligne à modifier quand on aura écrit la classe UtilisateurDAO
        # return UtilisateurDAO.creer(Utilisateur(pseudo=pseudo, mdp=mdp, mail=mail))

        mdp = hash_password(mdp, sel=pseudo)
        return UtilisateurDAO.creer(Utilisateur(pseudo=pseudo, mdp=mdp, mail=mail))

    @log
    def connecter(self, pseudo: str, mdp: str) -> Utilisateur:
        """
        Permet de se connecter à un utilisateur.

        Args:
            pseudo (str): Pseudo de l'utilisateur qui veut se connecter
            mdp (str): Mot de passe de l'utilisateur qui veut se connecter

        Returns:
            Utilisateur: Renvoie l'utilisateur correspondant aux paramètres entrés.
        """
        if not isinstance(pseudo, str):
            raise TypeError("Le pseudo doit être une chaîne de caractères alphanumériques.")
        if not isinstance(mdp, str):
            raise TypeError("Le mot de passe doit être une chaîne de caractères alphanumériques.")

        # Il faudrait aussi faire attention aux caractères spéciaux
        return UtilisateurDAO().se_connecter(pseudo, hash_password(mdp, pseudo))

    @log
    def supprimer(self, user: Utilisateur) -> bool:
        """
        Permet de supprimer un utilisateur existant.

        Args:
            user (Utilisateur): Utilisateur dont on veut supprimer le compte

        Returns:
            bool: True si l'utilisateur a bien été supprimé. False sinon.
        """
        if not isinstance(user, Utilisateur):
            raise TypeError("L'utilisateur n'est pas renseigné correctement.")
        # Vérifier si l'utilisateur existe bien dans la base de données
        # Proposer à l'utilisateur de confirmer son choix (Oui ou Non)
        # Renvoie True si l'utilisateur a bien été supprimé, False sinon
        return UtilisateurDAO().supprimer(user)

    @log
    def lister_tous(self) -> List[Utilisateur]:
        """
        Renvoie la liste de tous les utilisateurs dans la base de données

        Returns:
            List[Utilisateur]: Liste des utilisateurs
        """

        utilisateurs = UtilisateurDAO().lister_tous()
        return utilisateurs

    @log
    def trouver_par_id(self, id_user: int) -> Optional[Utilisateur]:
        """
        Permet de trouver un utilisateur avec son identifiant

        Args:
            id_user (int): Identifiant de l'utilisateur recherché

        Returns:
            Optional[Utilisateur]: Utilisateur correspondant à l'identifiant recherché.
                                    None si la recherche ne correspond à rien
        """
        return UtilisateurDAO().trouver_par_id(id_user)

    @log
    def modifier(self, user: Utilisateur, new_user: Utilisateur) -> Optional[Utilisateur]:
        """
        Permet de modifier les informations d'un utilisateur

        Args:
            user (Utilisateur):
                Utilisateur dont on veut modifier les données
            new_user (Utilisateur):
                Nouvelles informations de l'utilisateur concerné

        Returns:
            Optional[Utilisateur]:
                Informations de l'utilisateur modifiées.
                None si la modification a échoué.
        """

        user.mdp = hash_password(user.mdp, user.pseudo)
        return user if UtilisateurDAO().modifier(user) else None

    def voir_suggestions(self) -> list[Recette]:
        """
        Renvoie une liste de recettes suggérées à l'utilisateur grâce à
        la liste de ses ingrédients favoris et non désirés.

        Returns:
            List[Recette]: Liste des recettes suggérées à l'utilisateur.
        """

        ingredients_favoris = super._ingredients_favoris
        nb_favoris = 0

        ingredients_non_desires = super._ingredients_non_desires
        nb_non_desires = 0

        recettes_suggerees = []
        toutes_les_recettes = RecetteService.lister_toutes_recettes()

        for recette in toutes_les_recettes:
            ingredients = recette.liste_ingredient
            for ingredient in ingredients:
                if ingredient in ingredients_favoris:
                    nb_favoris += 1
                if ingredient in ingredients_non_desires:
                    nb_non_desires += 1
            if nb_favoris - nb_non_desires > 0:
                recettes_suggerees.append(recette)

        # Amélioration : trier la liste selon le résultat du dernier calcul
        return recettes_suggerees

    def voir_favoris(self) -> list[Recette]:
        """
        Renvoie la liste "recette_favorite" de l'utilisateur

        Returns:
            list[Recette]: Liste des recettes favorites de l'utilisateur
        """

        return super._recette_favorite

    def voir_liste_course(self) -> list[Recette]:
        """
        Renvoie la liste "liste_de_course" de l'utilisateur

        Returns:
            list[Recette]: Liste de course de l'utilisateur
        """

        return super._liste_course

    def voir_ingredients_favoris(self) -> list[Ingredient]:
        """
        Renvoie la liste "ingredient_favori" de l'utilisateur

        Returns:
            list[Ingredient]: Liste des ingrédients favoris de l'utilisateur
        """

        return super._ingredients_favoris

    def voir_ingredients_non_desires(self) -> list[Ingredient]:
        """
        Renvoie la liste "ingredient_non_desire" de l'utilisateur

        Returns:
            list[Ingredient]: Liste des ingrédients non désirés de l'utilisateur
        """

        return super._ingredients_non_desires
