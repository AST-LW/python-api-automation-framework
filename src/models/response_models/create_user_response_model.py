from pydantic.dataclasses import dataclass
from src.models.utils_models.response_model import ResponseModel


@dataclass
class _CreateUserBodyModel:
    user_id: str
    access_token: str


@dataclass
class CreateUserResponseModel(ResponseModel):
    data: _CreateUserBodyModel
