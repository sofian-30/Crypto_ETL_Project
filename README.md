# ETL Project

Ce projet implémente un pipeline ETL (Extraction, Transformation, Loading) qui permet d'extraire des données d'une source via un API, de les transformer, puis de les charger dans une base de données pour analyse. Ce projet dispose aussi d'une partie Devops en plus de la data ingénierie, à savoir l'utilisation de conteneur Docker et des tests unitaires github Action CI/CD.

## Prérequis

Avant de commencer, vous devez avoir installé les éléments suivants :

- **Python 3.8+**
- **PostgreSQL** (ou une autre base de données compatible)
- **Docker** et **Docker Compose** (si vous souhaitez utiliser des conteneurs pour exécuter le projet)

## Installation

### 1. Cloner le Repository

Clonez le repository sur votre machine locale en utilisant la commande suivante :

```bash
git clone https://github.com/sofian-30/ETL_Project.git
cd ETL_Project
```

### 2.Créer un Environnement Virtuel
Créez un environnement virtuel pour isoler les dépendances Python :

```bash
python -m venv venv
source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`
```
### 3. Installer les Dépendances
Installez les dépendances nécessaires listées dans le fichier requirements.txt :

```bash

pip install -r requirements.txt
```
### 4. Démarrer les Services Docker (Optionnel)
Si vous utilisez Docker pour la base de données ou d'autres services, vous pouvez démarrer les conteneurs avec Docker Compose :

```bash

docker-compose up
```
Cela démarrera les services comme définis dans le fichier docker-compose.yml, y compris la base de données et toute autre dépendance nécessaire.

Structure du Projet
Voici un aperçu de la structure du projet :

extract.py : Code pour extraire les données de la source (par exemple, fichiers CSV, API).
transform.py : Code pour transformer les données (nettoyage, ajout de nouvelles colonnes, etc.).
load.py : Code pour charger les données dans la base de données (PostgreSQL ou autre).
docker-compose.yml : Fichier pour configurer et démarrer les services Docker nécessaires.
requirements.txt : Liste des dépendances Python pour le projet.
README.md : Documentation du projet.
Utilisation
Exécution du pipeline ETL : Le pipeline ETL peut être exécuté directement depuis le terminal en appelant les scripts Python correspondants. Par exemple :

```bash

python extract.py
python transform.py
python load.py
```
Automatiser le pipeline : Vous pouvez automatiser l'exécution du pipeline à intervalles réguliers en utilisant un planificateur de tâches (par exemple, cron sous Linux ou Airflow).

Dépendances
Voici les principales bibliothèques Python utilisées dans ce projet :

pandas : Pour la manipulation et l'analyse des données.
SQLAlchemy : ORM pour interagir avec la base de données.
psycopg2 : Connecteur PostgreSQL pour Python.
requests : Pour effectuer des requêtes HTTP (si l'extraction des données provient d'une API).
docker-compose : Pour la gestion des conteneurs Docker (optionnel).
pytest : Pour les tests unitaires.
Contribution
Les contributions sont les bienvenues ! Si vous souhaitez améliorer ce projet, suivez ces étapes :

Forkez ce repository.
Créez une nouvelle branche (git checkout -b feature/nouvelle-feature).
Faites vos modifications et commitez-les (git commit -am 'Ajout de nouvelle-feature').
Poussez votre branche (git push origin feature/nouvelle-feature).
Ouvrez une pull request pour que vos modifications soient examinées.


Auteurs
Sofian Ouass - Data Ingénieur/Devops et mainteneur principal.

Licence
Ce projet est sous licence MIT - voir le fichier LICENSE pour plus de détails.







