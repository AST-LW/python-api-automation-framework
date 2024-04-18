from dataclasses import dataclass


@dataclass
class RequestModel:
    name: str
    message: str


print(RequestModel(*{"name": "", "message":"Hi"}).__dict__)
