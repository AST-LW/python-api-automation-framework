import allure
from functools import wraps
from pydantic.dataclasses import dataclass
from dataclasses import asdict
from src.utils.config_parser import CONFIG


@dataclass
class MetaData:
    tags: list[str]
    description: str
    author: str
    test_case_id: str
    severity: str


def meta_data(data: MetaData = None):
    def decorator(function_reference):
        @wraps(function_reference)
        def wrapper(*args, **kwargs):
            # converting the model to dictionary format
            _data = asdict(data)
            if data:
                if 'tags' in _data:
                    for tag in _data["tags"]:
                        allure.dynamic.tag(tag)
                if 'description' in _data:
                    allure.dynamic.description(_data["description"])
                if 'author' in _data:
                    allure.dynamic.tag(
                        "test-case-author-" + _data["author"])
                if 'test_case_id' in _data:
                    allure.dynamic.testcase(
                        CONFIG.TEST_CASE_LINK + _data["test_case_id"])
                if 'severity' in _data:
                    allure.dynamic.severity(_data["severity"])

                # Add other metadata handlers here as needed
            return function_reference(*args, **kwargs)
        return wrapper
    return decorator
