from abc import ABC, abstractmethod


class UserDAOInterface(ABC):
    @abstractmethod
    def get_user_by_username(self, username):
        pass

    @abstractmethod
    def get_user_by_id(self, user_id):
        pass

    @abstractmethod
    def create_user(self, username, hashed_password):
        pass