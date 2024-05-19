import os
from pydantic.dataclasses import dataclass


@dataclass
class ManifestModel:
    BASE_URL: str = ""
    CAPTURE_LOGS: bool = False
    ENV: str = ""
    TEST_CASE_LINK: str = ""


@dataclass
class BaseConfigModel:
    main_manifest_file_path: str = os.path.join(os.getcwd(), "manifest.toml")
    manifest_file_path: str = ""
    endpoints_path: str = ""
