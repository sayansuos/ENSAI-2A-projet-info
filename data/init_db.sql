-----------------------------------------------------
-- Utilisateur
-----------------------------------------------------
DROP TABLE IF EXISTS utilisateur CASCADE ;
CREATE TABLE utilisateur(
    id_utilisateur    SERIAL PRIMARY KEY,
    mdp               VARCHAR(256),
    est_admin         BOOLEAN
);

-----------------------------------------------------
-- Ingrédient
-----------------------------------------------------
DROP TABLE IF EXISTS ingredient CASCADE ;
CREATE TABLE ingredient(
    id_ingredient    SERIAL PRIMARY KEY,
    nom_ingredient   VARCHAR(30) UNIQUE
);

-----------------------------------------------------
-- Recette
-----------------------------------------------------
DROP TABLE IF EXISTS recette CASCADE ;
CREATE TABLE recette(
    id_recette    SERIAL PRIMARY KEY,
    nom_recette   VARCHAR(30) UNIQUE,
);

-----------------------------------------------------
-- RecetteIngredient
-----------------------------------------------------
DROP TABLE IF EXISTS recetteingredient CASCADE ;
CREATE TABLE recetteingredient(
    id_recette       SERIAL PRIMARY KEY,
    id_ingredient    SERIAL PRIMARY KEY,
    FOREIGN KEY (id_recette) REFERENCES recette(id_recette),
    FOREIGN KEY (id_ingredient) REFERENCES ingredient(id_ingredient),
    quantite VARCHAR(30),
);

-----------------------------------------------------
-- RecetteFavorite
-----------------------------------------------------
DROP TABLE IF EXISTS recettefavorite CASCADE ;
CREATE TABLE recettefavorite(
    id_utilisateur    SERIAL PRIMARY KEY,
    id_recette        SERIAL PRIMARY KEY,
    FOREIGN KEY (id_utilisateur) REFERENCES utilisateur(id_utilisateur),
    FOREIGN KEY (id_recette) REFERENCES recette(id_recette),
);

-----------------------------------------------------
-- PréférenceIngrédient
-----------------------------------------------------
DROP TABLE IF EXISTS preferenceingredient CASCADE ;
CREATE TABLE preferenceingredient(
    id_utilisateur    SERIAL PRIMARY KEY,
    id_ingredient     SERIAL PRIMARY KEY,
    FOREIGN KEY (id_utilisateur) REFERENCES utilisateur(id_utilisateur),
    FOREIGN KEY (id_ingredient) REFERENCES ingredient(id_ingredient),
    non_desire  BOOLEAN,
    favori      BOOLEAN
);

-----------------------------------------------------
-- ListeCourse
-----------------------------------------------------
DROP TABLE IF EXISTS listecourse CASCADE ;
CREATE TABLE listecourse(
    id_utilisateur    SERIAL PRIMARY KEY,
    id_ingredient     SERIAL PRIMARY KEY,
    FOREIGN KEY (id_utilisateur) REFERENCES utilisateur(id_utilisateur),
    FOREIGN KEY (id_ingredient) REFERENCES recetteingredient(id_ingredient),
);
