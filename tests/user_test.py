import pytest
import allure

from src.actions.actions_lookup import Actions
from src.models.request_models.create_user_request_model import *
from fixtures import suite_scope, test_scope
from src.utils.request_payload_generator import RequestPayloadGenerator

import globals


@pytest.mark.usefixtures("suite_scope", "test_scope")
class UserTests:

    @allure.description("This test attempts to create a new user successfully")
    def test_successful_user_creation(self):
        # Arrange
        username, email, password = RequestPayloadGenerator.create_new_user_payload().values()
        user_data = CreateUserRequestModel(
            username=username, email=email, password=password)

        # Act
        response = Actions.user.create_new_user(user_data)

        # Assert
        assert response.status == 201
        assert response.data.access_token != None

    @allure.description("This test verifies that an email field is required for successful user creation")
    def test_missing_email_field_results_in_unsuccessful_user_creation(self):
        # Arrange
        username, password = RequestPayloadGenerator.create_new_user_payload([
                                                                             "email"]).values()
        user_data = WithoutEmailRequestModel(
            username=username, password=password)

        # Act
        response = Actions.user.create_user_without_email(user_data)

        # Assert
        assert response.status == 400
        assert response.error.error == "Username, password, and email are required."
