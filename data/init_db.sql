-----------------------------------------------------
-- Utilisateur
-----------------------------------------------------
DROP TABLE IF EXISTS projet.utilisateur CASCADE ;
CREATE TABLE projet.utilisateur(
    id_utilisateur    SERIAL PRIMARY KEY,
    mdp               VARCHAR(256),
    est_admin         BOOLEAN
);

-----------------------------------------------------
-- Ingrédient
-----------------------------------------------------
DROP TABLE IF EXISTS projet.ingredient CASCADE ;
CREATE TABLE projet.ingredient(
    id_ingredient    SERIAL PRIMARY KEY,
    nom_ingredient   VARCHAR(30) UNIQUE
);

-----------------------------------------------------
-- Recette
-----------------------------------------------------
DROP TABLE IF EXISTS projet.recette CASCADE;
CREATE TABLE projet.recette(
    id_recette               SERIAL PRIMARY KEY,
    nom_recette              VARCHAR(30) UNIQUE,
    description_recette      VARCHAR(250) UNIQUE,
    avis                     VARCHAR(250) UNIQUE,
    note                     FLOAT
);

-----------------------------------------------------
-- RecetteIngredient
-----------------------------------------------------
DROP TABLE IF EXISTS projet.recette_ingredient CASCADE;
CREATE TABLE projet.recette_ingredient(
    id_ingredient INTEGER,
    id_recette INTEGER,
    quantite VARCHAR(30),
    PRIMARY KEY (id_ingredient, id_recette),
    FOREIGN KEY (id_ingredient) REFERENCES projet.ingredient(id_ingredient),
    FOREIGN KEY (id_recette) REFERENCES projet.recette(id_recette)
);

-----------------------------------------------------
-- RecetteFavorite
-----------------------------------------------------
DROP TABLE IF EXISTS recette_favorite CASCADE ;
CREATE TABLE recette_favorite(
    id_utilisateur    INTEGER,
    id_recette       INTEGER,
    PRIMARY KEY (id_utilisateur, id_recette),
    FOREIGN KEY (id_utilisateur) REFERENCES utilisateur(id_utilisateur),
    FOREIGN KEY (id_recette) REFERENCES recette(id_recette)
);

-----------------------------------------------------
-- PréférenceIngrédient
-----------------------------------------------------
DROP TABLE IF EXISTS preference_ingredient CASCADE ;
CREATE TABLE preference_ingredient(
    id_utilisateur    INTEGER,
    id_ingredient     INTEGER,
    PRIMARY KEY (id_utilisateur, id_ingredient),
    FOREIGN KEY (id_utilisateur) REFERENCES utilisateur(id_utilisateur),
    FOREIGN KEY (id_ingredient) REFERENCES ingredient(id_ingredient),
    non_desire  BOOLEAN,
    favori      BOOLEAN
);

-----------------------------------------------------
-- ListeCourse
-----------------------------------------------------
DROP TABLE IF EXISTS liste_course CASCADE ;
CREATE TABLE liste_course(
    id_utilisateur    INTEGER,
    id_ingredient     INTEGER,
    id_recette        INTEGER,
    PRIMARY KEY (id_utilisateur, id_ingredient, id_recette),
    FOREIGN KEY (id_utilisateur) REFERENCES utilisateur(id_utilisateur),
    FOREIGN KEY (id_ingredient, id_recette) REFERENCES recette_ingredient(id_ingredient, id_recette)
);
