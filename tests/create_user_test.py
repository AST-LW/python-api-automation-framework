import pytest

import random
import string

from src.actions.actions import Actions


def generate_random_string(length):
    # Includes uppercase letters, lowercase letters, and digits
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def test_successful_user_creation():
    username = generate_random_string(3)
    email = generate_random_string(3) + "@example.com"

    user_data = {
        "username": username,
        "email": email,
        "password": "1234567890"
    }

    # Act
    response = Actions.user.create_new_user(user_data)

    # Assert
    assert response["data"]["access_token"] != None
