
from src.utils.random_data_generator import RandomDataGenerator
from src.utils.json_parser import parse_json


class RequestPayloadGenerator:

    @staticmethod
    def create_new_user_payload(exclude=[]):
        username = RandomDataGenerator.generate_random_string()
        email = RandomDataGenerator.generate_random_string() + "@example.com"
        password = parse_json("user_service", "$.create_new_user_password")

        payload = {
            "username": username,
            "email": email,
            "password": password
        }

        for property in exclude:
            del payload[property]

        return payload
