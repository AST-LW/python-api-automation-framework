from pydantic.dataclasses import dataclass


@dataclass
class CreateUserRequestModel:
    username: str = ""
    email: str = ""
    password: str = ""


@dataclass
class WithoutEmailRequestModel:
    username: str = ""
    password: str = ""
