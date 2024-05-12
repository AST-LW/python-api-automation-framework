import pytest

import globals
from src.utils.logger import Logger
from src.utils.logger import LogReporterUtils


@pytest.fixture(scope="class")
def suite_scope():
    globals.LOGGER_REFERENCE = Logger

    yield


@pytest.fixture(scope="function")
def test_scope():
    globals.LOGGER = LogReporterUtils.logger_initialization()

    yield
