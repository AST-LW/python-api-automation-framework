import pytest
from http import HTTPStatus

from src.actions.actions_lookup import Actions
from src.models.request_models.create_user_request_model import *
from fixtures import suite_scope, test_scope
from src.utils.request_payload_generator import RequestPayloadGenerator
from tests.data.assert_messages import user_service

from src.utils.decorators.meta_data_decorator import meta_data, MetaData


@pytest.mark.usefixtures("suite_scope", "test_scope")
class UserServiceTests:

    @pytest.mark.local  # To execute in local we use the "local marker"
    @pytest.mark.regression
    @meta_data(data=MetaData(tags=["positive-tc", "smoke"],
                             description="This test attempts to create a new user successfully",
                             author="Jane",
                             test_case_id="TC001", severity="critical"))
    def test_successful_user_creation(self):
        # Arrange
        username, email, password = RequestPayloadGenerator.create_new_user_payload().values()
        user_data = CreateUserRequestModel(
            username=username, email=email, password=password)

        # Act
        response = Actions.user.create_new_user(user_data)

        # Assert
        assert response.status == HTTPStatus.CREATED
        assert response.data.access_token != None

    @pytest.mark.regression
    @meta_data(data=MetaData(tags=["negative-tc", "smoke", "regression"],
                             description="This test verifies that an email field is required for successful user creation",
                             author="Jimmy",
                             test_case_id="TC002",  severity="normal"))
    def test_missing_email_field_results_in_unsuccessful_user_creation(self):
        # Arrange
        username, password = RequestPayloadGenerator.create_new_user_payload([
                                                                             "email"]).values()
        user_data = WithoutEmailRequestModel(
            username=username, password=password)

        # Act
        response = Actions.user.create_user_without_email(user_data)

        # Assert
        assert response.status == HTTPStatus.BAD_REQUEST
        assert response.error.error == user_service.MISSING_EMAIL_ASSERT_MESSAGE
