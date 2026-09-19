# 🎬 Application de gestion de films

Application web développée en **Python/Flask** dans le cadre d'un TP (BUT3 Informatique — Programmation avancée Python/Flask, IUT de Villetaneuse, USPN).

L'application permet de parcourir un catalogue de plus de 30 000 films, de consulter leurs informations (année, genres, résumé), de rechercher un film sur Google en un clic, et intègre un système d'authentification complet (inscription, connexion, restriction d'accès).

## ✨ Fonctionnalités

- 📽️ **Catalogue de films** : affichage de tous les films, des *n* premiers films, ou filtrage par année
- 🔍 **Recherche rapide** : bouton "Search" redirigeant vers une recherche Google du titre du film
- 🔐 **Authentification** : inscription et connexion sécurisées, mots de passe hachés (jamais stockés en clair)
- 🔒 **Contrôle d'accès** : restriction centralisée via `@before_request` — seules les pages `index`, `infos`, `login` et `signin` sont accessibles sans être connecté
- 👤 **Page d'informations étudiant** : affichage dynamique des informations de l'utilisateur connecté

## 🏗️ Architecture

Le projet suit une architecture en couches inspirée du pattern **MVC**, avec une séparation stricte entre l'accès aux données, la logique métier et les contrôleurs :

```
app/
├── blueprints/          # Contrôleurs (routes Flask), organisés par domaine
│   ├── index/           # Page d'accueil
│   ├── infos/           # Informations de l'étudiant connecté
│   ├── movies/          # Catalogue de films
│   └── users/           # Authentification (login, inscription, déconnexion)
├── models/              # Modèles objets + DAO (Data Access Object)
│   ├── Movie.py
│   ├── MovieDAO.py
│   ├── User.py
│   ├── UserDAO.py
│   └── UserDAOInterface.py
├── services/            # Logique métier, entre les contrôleurs et les DAO
│   ├── MovieServices.py
│   └── UserServices.py
├── static/
│   ├── css/             # Feuilles de style (style.css, movies.css, infos.css)
│   └── data/            # Données sources (JSON + schémas SQL)
├── templates/           # Templates Jinja partagés (layout.html, nav.html)
└── movies.db            # Base de données SQLite
```

Chaque **blueprint** définit ses propres routes et ses propres templates (dans un sous-dossier `templates/` local), et s'appuie sur un **service** pour sa logique métier, qui lui-même délègue l'accès aux données à un **DAO**. Cette séparation permet, par exemple, de faire évoluer la source de données (changer de SGBD) sans toucher aux routes ni à la logique métier.

## 🗃️ Modèle de données

Deux tables SQLite, définies dans `app/static/data/` :

**`movies`** (`schema_movies.sql`)
| Colonne | Type | Description |
|---|---|---|
| id | INTEGER | Identifiant unique |
| title | TEXT | Titre du film |
| year | INTEGER | Année de sortie |
| genres | TEXT | Genres (séparés par des virgules) |
| href | TEXT | Lien vers la fiche source |
| extract | TEXT | Résumé |
| cover | TEXT | URL de l'affiche |

**`users`** (`schema_users.sql`)
| Colonne | Type | Description |
|---|---|---|
| id | INTEGER | Identifiant unique |
| username | TEXT | Nom d'utilisateur (unique) |
| password | TEXT | Mot de passe **haché** (Werkzeug) |
| firstname | TEXT | Prénom |
| lastname | TEXT | Nom |
| student_id | TEXT | Numéro étudiant |

## 🚀 Installation et lancement

### Prérequis
- Python 3.13
- pip

### Mise en place

```bash
# Cloner le dépôt
git clone https://github.com/clem-221/application-gestion-de-films
cd TD01

# Créer et activer un environnement virtuel (si besoin, non obligatoire)
python3 -m venv mon_environnement
source mon_environnement/bin/activate

# Installer les dépendances
pip install flask

# Générer la base de données (films + utilisateurs)
python3 prepa_db.py

# Lancer l'application
python3 main.py
```

L'application est alors accessible sur [http://localhost:8000](http://localhost:8000).

## 🔑 Sécurité

- Les mots de passe sont hachés avec `werkzeug.security.generate_password_hash` avant tout stockage en base — aucun mot de passe n'est jamais conservé en clair.
- L'authentification s'appuie sur les sessions Flask (`session["logged"]`, `session["username"]`, `session["user_id"]`).
- L'accès aux pages est contrôlé de façon centralisée via un hook `@app.before_request`, qui redirige vers la page de connexion toute requête non authentifiée en dehors de la liste blanche (`index`, `infos`, `login`, `signin`, `static`).

## 🛠️ Stack technique

- **Backend** : Python 3, Flask (Blueprints)
- **Base de données** : SQLite3
- **Frontend** : Jinja2, Bootstrap 5.3
- **Sécurité** : Werkzeug (hachage de mots de passe)

## 🎓 Acquis de ce TP

Ce travail pratique a été l'occasion de mettre en œuvre plusieurs notions clés du développement web avec Flask :

- **Architecture en couches (MVC / DAO / Service)** : séparation claire entre l'accès aux données (DAO), la logique métier (Service) et les contrôleurs (blueprints), pour un code plus maintenable et testable — chaque couche ne connaît que celle juste en dessous.
- **Blueprints Flask** : découpage de l'application en modules indépendants (`index`, `infos`, `movies`, `users`), chacun avec ses propres routes et son propre dossier `templates/`, et compréhension du système d'*endpoints* (`blueprint.fonction`) utilisé par `url_for()`.
- **ORM manuel avec SQLite3** : écriture de requêtes SQL paramétrées (protection contre les injections), conversion des résultats bruts (`sqlite3.Row`) en objets métier (`Movie`, `User`) via des méthodes `from_dict()` / `from_tuple()`.
- **Authentification sécurisée** : hachage des mots de passe avec Werkzeug (jamais de mot de passe en clair), gestion de session Flask, et distinction claire entre les responsabilités (le DAO ne hache rien, c'est le rôle du service).
- **Contrôle d'accès centralisé** : mise en place d'une restriction globale via `@app.before_request` plutôt qu'un décorateur répété sur chaque route, avec gestion d'une liste blanche d'endpoints publics (sans oublier `static`, sous peine de casser tous les assets pour un visiteur non connecté).
- **Héritage de templates Jinja2** (`{% extends %}` / `{% block %}`) : éviter la duplication de la structure HTML (`<head>`, navigation) entre les pages, et centraliser le CSS/JS partagé dans un layout commun.
- **Débogage méthodique** : lecture de tracebacks Flask/Jinja2, diagnostic d'erreurs classiques (`TemplateNotFound`, `BuildError`, `ImportError`, imports circulaires) en remontant la pile d'appels plutôt qu'en devinant, et compréhension du cycle requête/réponse HTTP (codes 200, 304, 404).
- **Gestion des chemins relatifs** : compréhension de la résolution des chemins de fichiers selon le répertoire de travail (`cwd`) lors du lancement d'un script Python, source fréquente d'erreurs `FileNotFoundError`.
- **Qualité et fiabilité des données externes** : gestion défensive des données scrapées (URLs d'images cassées ou invalides), avec une solution de repli côté frontend (`onerror` sur les balises `<img>`) plutôt qu'une tentative de correction systématique côté serveur.

## 📌 Auteur

Clément SENE — Étudiant BUT 3 Informatique, IUT de Villetaneuse (Université Sorbonne Paris Nord)

**Cours créé par** : Gaël Guibon - Professeur Programmation Avancée Python
