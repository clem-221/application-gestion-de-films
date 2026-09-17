from flask import Blueprint, render_template, jsonify

index_bp = Blueprint('index', __name__)

@index_bp.route('/', methods=['GET'])
def index():
    return "Bonjour, bienvenue sur l'API de gestion des films ! (par blueprint)"