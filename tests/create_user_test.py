import pytest

from src.actions.actions_lookup import Actions
from src.utils.random_data_generator import RandomDataGenerator
from src.models.request_models.create_user_request_model import *


@pytest.mark.usefixtures("suite_scope", "test_scope")
class CreateUserTests:
    def test_successful_user_creation(self):
        # Arrange
        username = RandomDataGenerator.generate_random_string()
        email = RandomDataGenerator.generate_random_string() + "@example.com"

        user_data = CreateUserRequestModel(
            username=username, email=email, password="1234567890")

        # Act
        response = Actions.user.create_new_user(user_data)

        # Assert
        assert response.data.access_token != None
