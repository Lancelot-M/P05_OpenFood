CREATE DATABASE IF NOT EXISTS OpenFoodFact;

USE OpenFoodFact;

CREATE TABLE IF NOT EXISTS Categorie (
	id INT NOT NULL,
	name VARCHAR(40),
	description TEXT,
	PRIMARY KEY (name)
)
ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS Aliments(
	id INT NOT NULL,
	name VARCHAR(40) NOT NULL,
	description TEXT,
	categorie VARCHAR(40) NOT NULL,
	dispenser VARCHAR(40),
	groups VARCHAR(45) NOT NULL,
	score INT NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (categorie) REFERENCES Categorie(name)
)
ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS Dispenser (
	id INT NOT NULL,
	name VARCHAR(40) NOT NULL,
	location VARCHAR(50),
	PRIMARY KEY (id)
)
ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS Save (
	id INT NOT NULL AUTO_INCREMENT,
	original_prod VARCHAR(45) NOT NULL,
	substitution_prod VARCHAR(45) NOT NULL,
	PRIMARY KEY (id)
)
ENGINE=INNODB;

INSERT INTO Categorie (id, name, description)
VALUES (182038, 'cereales', 'produits issus des grosses moissnoneuz'),
	(2943, 'laitages', NULL),
	(9483304, 'plomb', 'peinture indigeste');

