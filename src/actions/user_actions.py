from src.clients.user_client import UserClient


class UserActions:

    @staticmethod
    def create_new_user(data):
        return UserClient.create_user(data)
