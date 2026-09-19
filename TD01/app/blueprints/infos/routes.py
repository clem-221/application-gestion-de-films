from flask import Blueprint, render_template, session
from app.models.UserDAO import UserDAO

infos_bp = Blueprint('infos', __name__, template_folder="templates")
user_dao = UserDAO("app/movies.db")

@infos_bp.route('/', methods=['GET'])
def infos():
    metadata = {"title": "Informations étudiant", "pagename": "infos"}

    user_data = None
    if "user_id" in session:
        user_data = user_dao.get_user_by_id(session["user_id"])

    return render_template('infos.html', metadata=metadata, data=user_data)