from typing import TypeVar, Callable
from src.utils.config_parser import ENDPOINTS
from src.utils.base_client import RequestDirectory
from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)

class UserClient:
    @staticmethod
    def create_user(data: BaseModel, response_model: Callable[..., T]) -> T:
        response = RequestDirectory.post.with_endpoint(
            ENDPOINTS.user.create_new_user).with_data(data).send()
        return response_model(**response)