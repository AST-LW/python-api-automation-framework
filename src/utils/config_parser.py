import os

from src.models.envs_models.config_models import *
from src.models.envs_models.endpoints_models import EndpointsModel
from src.utils.toml_operations import load_toml_config

SUPPORTED_ENVS = ["qa"]


@dataclass
class QaConfig(BaseConfigModel):
    manifest_file_path: str = os.path.join(
        os.getcwd(), "envs", "qa", "manifest.toml")
    endpoints_path: str = os.path.join(
        os.getcwd(), "envs", "qa", "endpoints.toml")

# other environments


def _select_environment_paths() -> BaseConfigModel:
    env = os.getenv("ENV")
    if env.lower() not in SUPPORTED_ENVS:
        raise Exception(f"{env} is not supported environment")

    if env == "qa":
        return QaConfig()


def fetch_config() -> ManifestModel:
    manifest_file = _select_environment_paths()
    manifest_data = load_toml_config(manifest_file.manifest_file_path)
    return ManifestModel(**manifest_data)


def fetch_endpoints():
    endpoints_file = _select_environment_paths()
    endpoints_data = load_toml_config(endpoints_file.endpoints_path)
    return EndpointsModel(**endpoints_data)


CONFIG = fetch_config()
ENDPOINTS = fetch_endpoints()
