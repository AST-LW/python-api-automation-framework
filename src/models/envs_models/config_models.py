from pydantic.dataclasses import dataclass


@dataclass
class ManifestModel:
    BASE_URL: str = ""


@dataclass
class BaseConfigModel:
    manifest_file_path: str = ""
    endpoints_path: str = ""
