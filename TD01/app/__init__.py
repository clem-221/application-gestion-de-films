import os
from flask import Flask

def create_app():
    # Création de l'instance de l'application Flask
    app = Flask(__name__, static_url_path='/static') # on indique où se trouvent les fichiers statiques

    # On personnalise la configuration de l'application avec la base de données
    app.config['DATABASE_PATH'] = os.path.join(app.root_path, 'movies.db') # on indique où se trouve la base de données
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + app.config['DATABASE_PATH'] # on indique l'URI de la base de données

    # Et on indique qu'on veut des cookies sécurisées pour la session
    app.config['SESSION_COOKIE_SECURE'] = True

    # La configuration de la clé secrète pour la session est obligatoire pour Flask, on la définit ici
    app.config['SECRET_KEY'] = 'ma cle secrete unique'  # Remplacez par une clé secrète aléatoire et sécurisée

    from app.blueprints import index_bp, infos_bp, movies_bp, users_bp
    
    app.register_blueprint(users_bp)
    app.register_blueprint(index_bp)
    app.register_blueprint(infos_bp, url_prefix="/infos")
    app.register_blueprint(movies_bp)

    @app.before_request
    def require_login():
        from flask import request, session, redirect, url_for

        allowed_endpoints = {
            "index.index",
            "infos.infos",
            "users.login",
            "users.signin",
            "static",
        }

        if request.endpoint not in allowed_endpoints and "logged" not in session:
            return redirect(url_for("users.login"))

    return app