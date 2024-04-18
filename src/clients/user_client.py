from pydantic import BaseModel

from src.utils.base_client import RequestDirectory


class UserClient:

    @staticmethod
    def create_user(data):
        response = RequestDirectory.create_post_request().with_endpoint(
            "todos/user/create").with_data(data).send()

        return response
