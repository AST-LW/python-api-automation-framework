from pydantic.dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass
class ResponseModel(Generic[T]):
    status: int = 0
    data: T | None = None
    error: T | None = None