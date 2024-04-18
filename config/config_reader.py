import os

from src.utils.toml_operations import load_toml_config

QA_CONFIG = os.getcwd() + "/config/qa.toml"


def fetch_config():
    env = os.getenv("ENV")
    if env == "qa":
        return load_toml_config(QA_CONFIG)


CONFIG = fetch_config()
