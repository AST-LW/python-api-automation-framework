import toml


def load_toml_config(file_path: str):
    config = toml.load(file_path)
    return config
