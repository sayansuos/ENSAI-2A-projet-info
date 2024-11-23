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
  - `git clone https://github.com/sayansuos/ENSAI-2A-projet-info.git`

---

## :arrow_forward: Open the depository with VSCode

- [ ] Open **Visual Studio Code**
- [ ] File > Open Folder
- [ ] Click once on *code_equipe_10* and click on `Sélectionner un dossier`
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

## :arrow_forward: Launch the programme

- [ ] In Git Bash :
  - `python src/utils/reset_database.py` : Reset the database and execute the script of the folder "data"
  - `python src/__main__.py` : launch the application


---
