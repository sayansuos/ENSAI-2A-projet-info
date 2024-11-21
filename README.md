# ENSAI 2A : IT Project

## :arrow_forward: Presentation

My Kitchen is a cooking recipe application. It's an interactive application that allows individuals to consult thousands of recipes from all over the world. By creating an account, loyal users can benefit from additional services such as the selection of favorite recipes, the creation of a shopping list or even suggestions tailored to their preferences. Likewise, only My Kitchen account holders will be able to rate recipes and leave comments for all to see.

All this is achieved via an online ordering interface. All the recipes listed in this application come from TheMealDB API. A database specific to the application will also be developed to ensure the smooth running of our application, but also to enable the addition of new recipes and their associated notations.

The application's main functions are :
- Display the list of all recipes
- Display a recipe, i.e. its title, ingredients, instructions, rating and comments
- Create a "Favourites" area for a logged-in user, enabling them to add, delete and view their favourite recipes
- Create a "Notes and commentary" area, enabling all users to consult notes and commentaries for each recipe. Only account holders will be able to rate and comment.

The application's advanced functions are :
- Display the list of recipes containing aspecified ingredient
- Create a "Shopping list" for a logged-in user, enabling them to add all the ingredients of a recipe to their shopping list, consult it and delete purchased items.
- Create a "My ingredients" area for a logged-in user, enabling them to enter their preferences, i.e. add favourite and/or unwanted ingredients, view them and delete them.
- Create a "My suggestions" area for a logged-in user, which will suggest recipes that are not in the Favourite recipes but contain at least one favourite ingredient and no unwanted ingredients.

---

## :arrow_forward: Required software

- [Visual Studio Code](https://code.visualstudio.com/)
- [Python 3.10](https://www.python.org/)
- [Git](https://git-scm.com/)
- A Database [PostgreSQL](https://www.postgresql.org/)

---

## :arrow_forward: Clone the repository

- [ ] Open **Git Bash**
- [ ] Create  folder `P:/Cours2A/UE3-Projet-info` and position yourself inside
  - `mkdir -p /p/Cours2A/UE3-Projet-info && cd $_`
- [ ] Clone the repository
  - `git clone https://github.com/ludo2ne/ENSAI-2A-projet-info.git`

---

## :arrow_forward: Open the depository with VSCode

- [ ] Open **Visual Studio Code**
- [ ] File > Open Folder
- [ ] Click once on *ENSAI-2A-projet-info* and click on `Sélectionner un dossier`
  - :warning: If the parent folder in the VSCode explorer (on the left) is not *ENSAI-2A-projet-info*, the application will not work.

### VScode parameters

This repository contains a file `.vscode/settings.json` which defines parameters for this project. For example :

- **Black formatter** automatically formats a python file
  - `editor.formatOnSave` : each time a file is saved, the code is automatically formatted
- **Flake8** is a Linter
  - it checks that the code is clean and displays a message if it is not
- **Path** : indicates the folders in which the python modules are located
  - `"PYTHONPATH": "${workspaceFolder}/src"` : src is the root folder for imports


### Fichiers de configuration


| Fichier                      | Description                                                         |
|------------------------------|---------------------------------------------------------------------|
| `.env`                       | Defining environment variables                                      |
| `.vscode/settings.json`      | Configuration specific to Visual Studio Code                        |
| `.github/workflows/ci.yml`   | Definition of GitHub Actions workflows                              |
| `logging_config.yml`         | Configuring the logging system                                      |
| `.gitignore`                 | List of files and directories to ignore during Git operations       |
| `.coveragerc`                | Configuring the code coverage tool                                  |
| `requirements.txt`           | List of Python dependencies required for the project                |

---

## :arrow_forward: Install necessary packages

In VSCode :

- [ ] Open a *Git Bash* terminal
- [ ] Run the following commands

```bash
pip install -r requirements.txt
pip list
```

---

## :arrow_forward: Environment variables

At the root of the project :

- [ ] Create a file named `.env`
- [ ] Paste and complete the folowing code :

```default
WEBSERVICE_HOST=http://themealdb.com/api/json/v1/1

POSTGRES_HOST=sgbd-eleves.domensai.ecole
POSTGRES_PORT=5432
POSTGRES_DATABASE=idxxxx
POSTGRES_USER=idxxxx
POSTGRES_PASSWORD=idxxxx
POSTGRES_SCHEMA=projet
```

---

## :arrow_forward: Lancer les tests unitaires

- [ ] Dans Git Bash : `pytest -v`
  - ou `python -m pytest -v` si *pytest* n'a pas été ajouté au *PATH*

### TU DAO

Les tests unitaires de la DAO utilisent les données du fichier `data/pop_db_test.sql`.

Ces données sont chargées dans un schéma à part (projet_test_dao) pour ne pas polluer les autres données.

### Couverture de tests

Il est également possible de générer la couverture de tests avec [Coverage](https://coverage.readthedocs.io/en/7.4.0/index.html)

:bulb: Le fichier `.coveragerc` permet de modifier le paramétrage

- [ ] `coverage run -m pytest`
- [ ] `coverage html`
- [ ] Ouvrir le fichier coverage_report/index.html

---

## :arrow_forward: Lancer le programme

Cette application propose une interface graphique très basique pour naviguer entre différents menus.

- [ ] Dans Git Bash : `python src/__main__.py`
- [ ] Au premier lancement, choisissez **Ré-initialiser la base de données**
  - cela appelle le programme `src/utils/reset_database.py`
  - qui lui même va exécuter les scripts SQL du dossier `data`



---

## :arrow_forward: Les logs

L'initialisation se fait dans le module `src/utils/log_init.py` :

- Celui-ci est appelé au démarrage de l'application ou du webservice
- Il utilise le fichier `logging_config.yml` pour la configuration
  - pour modifier le niveau de logs :arrow_right: balise *level*

Un décorateur a été créé dans `src/utils/log_decorator.py`.

Appliqué à une méthode, il permettra d'afficher dans les logs :

- les paramètres d'entrée
- la sortie

Les logs sont consultables dans le dossier `logs`.

Exemple de logs :

```
07/08/2024 09:07:07 - INFO     - ConnexionVue
07/08/2024 09:07:08 - INFO     -     JoueurService.se_connecter('a', '*****') - DEBUT
07/08/2024 09:07:08 - INFO     -         JoueurDao.se_connecter('a', '*****') - DEBUT
07/08/2024 09:07:08 - INFO     -         JoueurDao.se_connecter('a', '*****') - FIN
07/08/2024 09:07:08 - INFO     -            └─> Sortie : Joueur(a, 20 ans)
07/08/2024 09:07:08 - INFO     -     JoueurService.se_connecter('a', '*****') - FIN
07/08/2024 09:07:08 - INFO     -        └─> Sortie : Joueur(a, 20 ans)
07/08/2024 09:07:08 - INFO     - MenuJoueurVue
```

---

## :arrow_forward: Intégration continue

Le dépôt contient un fichier `.github/workflow/main.yml`.

Lorsque vous faîtes un *push* sur GitHub, cela déclenche un pipeline qui va effectuer les les étapes suivantes :

- Création d'un conteneur à partir d'une image Ubuntu (Linux)
  - Autrement dit, cela crée une machine virtuelle avec simplement un noyau Linux
- Installation de Python
- Installation des packages requis
- Lancement des tests unitaires (uniquement les tests de service car plus compliqué de lancer les tests dao)
- Analyse du code avec *pylint*
  - Si la note est inférieure à 7.5, l'étape sera en échec

Vous pouvez consulter le bon déroulement de ce pipeline sur la page GitHub de votre dépôt, onglet *Actions*.

---

## :construction: Lancer le projet sur le Datalab

Il est également possible de développer sur le Datalab.

:warning: Pensez bien à *push* régulièrement votre code, car les services du Datalab ne sont pas éternels.


### Paramétrage Git

Dans un premier temps, il faut autoriser de *push* du code depuis le Datalab vers GitHub.

Générez un jeton dans GitHub :

- [ ] Connectez-vous à [GitHub](https://github.com/)
- [ ] [Générez un nouveau token (classic)](https://github.com/settings/tokens/new)
  - si le lien direct ne fonctionne pas : allez dans *Settings* > *Developer Settings* > *Personal access tokens (classic)*
  - Note : Datalab
  - Date d'expiration : 90j (minimum)
  - Cochez repo
  - `Generate token`
- [ ] Copiez le token et collez le dans Notepad
  - :warning: Celui-ci ne sera visible qu'une seule fois
  - si vous le perdez, il faut en générer un nouveau

Ensuite, déclarez ce jeton au Datalab :

- [ ] Connectez-vous au [Datalab](https://datalab.sspcloud.fr/)
- [ ] Allez dans *Mon Compte*, puis *Services externes*
- [ ] Collez le token dans *Jeton d'accès personnel GitHub*

### Lancer les services

Pour commencer, vous avez besoin d'une base de données PostgreSQL. Sur la Datalab

- [ ] Allez dans *Catalogue de services* > *Database* > `PostgreSQL`
- [ ] Lancez le service
- [ ] Une fois le service lancé, copiez les infos suivantes
  ```
  Hostname : ?
  Port : 5432
  Database : ?
  Username : ?
  Password : ?
  ```
Nous allons ensuite lancer un service VSCode avec Python :

- [ ] Dans le catalogue des services, allez sur *Vscode-python*
- [ ] Cliquez sur *Configuration Vscode-python*
- [ ] Allez dans l'onglet Git
  - Repository : `https://github.com/ludo2ne/ENSAI-2A-projet-info-template.git`
- [ ] Lancez le service

Un nouvel onglet s'ouvre avec VSCode et le dépôt qui a été cloné.

Positionnez-vous dans le bon dossier :

- [ ] File > Open Folder > `/home/onyxia/work/ENSAI-2A-projet-info-template/`


### Connectez votre application et votre base de données

Vous avez lancé 2 services, maintenant il va falloir les relier.

Vous allez utiliser pour cela un fichier `.env` comme décrit dans la section [Variables d'environnement](##:arrow_forward:-Variables-d'environnement) plus haut. Dans votre VScode :

- [ ] Créez à la racine de `ENSAI-2A-projet-info-template` un fichier `.env`
- [ ] Collez le modèle (voir section *Variables d'environnement*)
- [ ] Renseignez les champs `HOSTNAME`, `DATABASE`, `USERNAME` et `PASSWORD` avec ceux de votre service *PostgreSQL*
- [ ] Enregistrez ce fichier

### Installez les packages

- [ ] Ouvrez un terminal (CTRL + ù)
- [ ] Positionnez-vous dans le dépôt : `cd $ROOT_PROJECT_DIRECTORY/ENSAI-2A-projet-info-template`
- [ ] `pip install -r requirements.txt`


### Lancez l'application

Vous pouvez maintenant lancer l'application, le webservice ou les tests unitaires

- `python src/__main__.py` (puis commencez par ré-initialiser la bdd)
- `python src/app.py` (à tester)
- `pytest -v`
