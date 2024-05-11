from pydantic.dataclasses import dataclass


@dataclass
class _UserEndpointsModel:
    create_new_user: str = ""


@dataclass
class EndpointsModel:
    user: _UserEndpointsModel
