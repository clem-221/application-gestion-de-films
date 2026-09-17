import json, os
from flask import Blueprint, render_template, current_app

infos_bp = Blueprint('infos', __name__, template_folder="templates")

@infos_bp.route('/', methods=['GET'])
def infos():
    # 1. Données de l'étudiant attendues par infos.html
    student_data = {
        "firstname": "Alex",
        "lastname": "Dupont",
        "studentId": "12011001"
    }

    # 2. Métadonnées attendues par layout.html
    metadata = {
        "title": "Informations étudiant"
    }

    return render_template('infos.html', data=student_data, metadata=metadata)