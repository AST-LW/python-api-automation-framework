import os

from src.models.envs_models.config_models import *
from src.models.envs_models.endpoints_models import EndpointsModel
from src.utils.toml_operations import load_toml_config

SUPPORTED_ENVS = ["qa"]


@dataclass
class QaConfigModel(BaseConfigModel):
    manifest_file_path: str = os.path.join(
        os.getcwd(), "envs", "qa", "manifest.toml")
    endpoints_path: str = os.path.join(
        os.getcwd(), "envs", "qa", "endpoints.toml")

# other environments


def _select_environment_paths() -> BaseConfigModel:
    # Select the environment given in the main manifest file
    main_manifest_file = BaseConfigModel().main_manifest_file_path
    main_manifest_data = load_toml_config(main_manifest_file)

    # ENV from CLI is prioritized over main manifest file
    env = os.getenv("ENV") or ManifestModel(**main_manifest_data).ENV

    # Raise the exception if the environment is not specified
    if env == "" or None:
        raise Exception(
            "The environment on which test suite execution is missing, specify in either CLI as environment variables or provide in main manifest file")

    # Raise the exception if the environment is not supported environments
    if env.lower() not in SUPPORTED_ENVS:
        raise Exception(f"{env} is not supported environment")

    # Choose the environment data model
    if env == "qa":
        return QaConfigModel()
    else:
        raise Exception(
            f"The specified environment - {env}, is not configured")


def fetch_config() -> ManifestModel:
    # config priority -> Main manifest file < Environment specific manifest file < CLI property passing as environment variables of the system / command line arguments
    selected_environment = _select_environment_paths()

    main_manifest_data = load_toml_config(
        selected_environment.main_manifest_file_path)
    environment_manifest_data = load_toml_config(
        selected_environment.manifest_file_path)

    # The order is important as the later having the same property will override the earlier one
    # As the environment level manifest file has more priority compared to main manifest file present at root level
    merged_manifest_data = {**main_manifest_data, **environment_manifest_data}

    # After merging the environment data, we can check if any environment variable is passed via CLI, then we need to replace with CLI one
    for key, value in merged_manifest_data.items():
        if os.getenv(key) is not None:
            merged_manifest_data[key] = os.getenv(key)

    return ManifestModel(**merged_manifest_data)


def fetch_endpoints():
    selected_environment = _select_environment_paths()
    endpoints_data = load_toml_config(selected_environment.endpoints_path)
    return EndpointsModel(**endpoints_data)


CONFIG = fetch_config()
ENDPOINTS = fetch_endpoints()
