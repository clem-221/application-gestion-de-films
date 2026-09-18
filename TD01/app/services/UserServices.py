from werkzeug.security import generate_password_hash, check_password_hash
from app.models.UserDAO import UserDAO
from app.models.User import User


class UserServices:
    def __init__(self, user_dao: UserDAO):
        self.user_dao = user_dao

    def register(self, username, password):
        if self.user_dao.get_user_by_username(username):
            return False, "Ce nom d'utilisateur est déjà pris."

        hashed = generate_password_hash(password)
        self.user_dao.create_user(username, hashed)
        return True, None

    def authenticate(self, username, password):
        data = self.user_dao.get_user_by_username(username)
        if data is None:
            return None
        if not check_password_hash(data["password"], password):
            return None
        return User.from_dict(data)