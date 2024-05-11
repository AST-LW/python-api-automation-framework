from typing import TypeVar
from src.utils.config_parser import ENDPOINTS
from src.utils.base_client import RequestDirectory
from src.models.response_models.create_user_response_model import *

T = TypeVar("T")


class UserClient:

    @staticmethod
    def create_user(data: T) -> CreateUserResponseModel:
        response = RequestDirectory.post.with_endpoint(
            ENDPOINTS.user.create_new_user).with_data(data).send()
        return CreateUserResponseModel(**response)
