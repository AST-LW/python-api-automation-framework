import string
import random


class RandomDataGenerator:

    @staticmethod
    def generate_random_string(length: int = 8) -> str:
        characters = string.ascii_letters + string.digits
        return "".join(random.choice(characters) for _ in range(length))
