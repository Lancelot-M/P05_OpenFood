# Projet 5
Programme ayant pour objectif de proposer des aliments de substitution plus sain. Avec une possibilité d'enregistrer les résultats pour une consultation ultérieure.

## 1) Prérequis.
Python3.6, MySQL, git ainsi qu'accéder à un terminal  est nécessaire pour le fonctionnement du programme. De plus, vous aurez besoin d'une base de donnée à allouer. Créez-la avant d'aller plus loin.  

## 2) Installation.
Pour lancer l'application:  
	- Ouvrez un terminal.
	- Créez et activez un environnement virtuel lié à ce projet.
	- Téléchargez le dossier du projet grâce à la commande "git pull https://github.com/Lancelot-M/P05_OpenFood.git".
	- Dans le dossier téléchargé, créez un fichier "config.py" (grâce à un éditeur de texte), contenant le nom de la base de donnée que vous avez créée, son hôte, votre identifiant mysql ainsi que votre mot de passe mysql en suivant le modèle contenu dans le fichier "config_exemple.py".  
	- Lancer le programme en tappant "python3 main.py".    

## 3) Paramétrage.
Dans le fichier "constants.py" ('./System/System/constants.py'), vous avez la possibilité de paramétrer le programme. En jouant sur les différentes catégories de produits ou le nombre de produits de substitution proposé lors du résultat de recherche.  
Pour ajouter, modifier ou supprimer une catégorie, ajoutez, modifiez ou supprimez "le nom de la catégorie".  
exemple : CATEGORIE = ["Cheeses"]  
	  CATEGORIE = ["Chocolates", "Condiments", "Chickens", "Hams", "Bolognese lasagne", "Potatoes", "Energy drinks", "Berries", "Snacks and desserts for babies", "Aromatic herbs", "Cheeses"]  
	  
Pour modifier le nombre de produits de substitution proposés, changer la valeur de MAX_PROD (avec une valeur minimal de 1).
exemple : MAX_PROD = 1  
	  MAX_PROD = 9  

## 4) Contrôles.
Pour naviguer dans le terminal suivez les instructions.
En cas de problème tapez 'ctr + c' pour sortir.

## 5) Annexe.
Quelques liens vers des ressources permettant de guider l'installation.  
Python : https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/230659-decouvrez-python  
MySQL : https://openclassrooms.com/fr/courses/1959476-administrez-vos-bases-de-donnees-avec-mysql/1959969-installez-mysql  
GIT : https://openclassrooms.com/fr/courses/2342361-gerez-votre-code-avec-git-et-github/2433596-installez-git  
Environnement virtuel : https://docs.python.org/fr/3/library/venv.html
