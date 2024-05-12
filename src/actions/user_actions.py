from src.clients.user_client import UserClient
from src.models.response_models.create_user_response_model import *
from src.models.request_models.create_user_request_model import *

class UserActions:
    @staticmethod
    def create_new_user(data: CreateUserRequestModel) -> CreateUserResponseModel:
        return UserClient.create_user(data, CreateUserResponseModel)

    @staticmethod
    def create_user_without_email(data: WithoutEmailRequestModel) -> WithoutEmailResponseModel:
        return UserClient.create_user(data, WithoutEmailResponseModel)