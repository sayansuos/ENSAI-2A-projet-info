from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from view.users.menu_user_vue import MenuUserVue
from view.recettes.recettes_vue_user import RecettesVue

from business_object.recette import Recette

from service.recette_service import RecetteService
from service.liste_favoris_service import ListeFavorisService


class MenuRecetteSugg(VueAbstraite):
    """Vue qui affiche :
    - toutes les recettes dispo
    - les options
    """

    def __init__(self, message, utilisateur):
        super().__init__(message)
        self.utilisateur = utilisateur

    def choisir_menu(self):
        recette_service = RecetteService()
        recettes = ListeFavorisService().consulter_suggestion(utilisateur=self.utilisateur)

        choix = "-> Page suivante"
        i = 0

        while choix == "-> Page suivante":
            i += 1
            if abs(10 * (i - 1) - len(recettes)) > 10:
                liste_recettes = recettes[10 * (i - 1) : 10 * i]
            else:
                liste_recettes = recettes[10 * (i - 1) :]
                i = 0

            liste_recettes.append("-> Page suivante")
            liste_recettes.append("Retour")
            choix = inquirer.select(
                message="Choisissez une recette : ",
                choices=liste_recettes,
            ).execute()

        if choix == "Retour":
            return MenuUserVue(message=self.message, utilisateur=self.utilisateur)

        else:
            autre_action = "Oui"
            while autre_action == "Oui":
                choix_bis = inquirer.select(
                    message="Que voulez-vous faire ?",
                    choices=[
                        "Lire la recette",
                        "Voir les notes et les avis",
                        "Noter et laisser un commentaire",
                        "Ajouter dans les favoris",
                        "Supprimer des favoris",
                        "Ajouter les ingrédients au panier",
                    ],
                ).execute()

                match choix_bis:
                    case "Lire la recette":
                        print(recette_service.lire_recette(choix), "\n\n")

                    case "Voir les notes et les avis":
                        print(recette_service.voir_note_avis(choix), "\n\n")

                    case "Noter et laisser un commentaire":
                        note = inquirer.select(
                            message="Quelle note attribuez-vous à cette recette ?",
                            choices=[
                                "0/5",
                                "1/5",
                                "2/5",
                                "3/5",
                                "4/5",
                                "5/5",
                            ],
                        ).execute()
                        note = int(note[0])
                        com = inquirer.text(
                            message="Laissez un commentaire ! (pas de ';')\n"
                        ).execute()
                        recette_service.ajouter_note_et_com(recette=choix, note=note, com=com)
                        choix = recette_service.trouver_recette_par_id(choix.id_recette)
                        print("\n\nC'est fait !!!\n\n")

                    case "Ajouter dans les favoris":
                        ListeFavorisService().ajouter_favoris(
                            recette=choix, utilisateur=self.utilisateur
                        )
                        print("\n\nC'est fait !!!\n\n")

                    case "Supprimer des favoris":
                        ListeFavorisService().retirer_favoris(
                            recette=choix, utilisateur=self.utilisateur
                        )
                        print("\n\nC'est fait !!!\n\n")

                    case "Ajouter les ingredients au panier":
                        ListeFavorisService().ajouter_liste_course(
                            recette=choix, utilisateur=self.utilisateur
                        )
                        print("\n\nC'est fait !!!\n\n")

                autre_action = inquirer.select(
                    message="Réaliser une autre action pour cette recette ?",
                    choices=["Oui", "Non"],
                ).execute()
                if autre_action == "Non":
                    choix_bis_bis = inquirer.select(
                        message="Consulter une autre recette ? ",
                        choices=["Oui", "Non"],
                    ).execute()
                    if choix_bis_bis == "Non":
                        return MenuUserVue(message=self.message, utilisateur=self.utilisateur)

        return MenuRecetteSugg(message=self.message, utilisateur=self.utilisateur)
