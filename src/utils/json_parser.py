import os
import json
from jsonpath_ng import parse
from .file_dir_operations import search_file_path


def parse_json(filename: str, pattern: str):
    scope_to_search: list[str] = ["tests/data"]

    results = []
    file_path: str | None = None

    # Search the json file within the scope given at top
    for scope in scope_to_search:
        file_path = search_file_path(os.path.join(
            os.getcwd(), scope), filename + ".json")
        if file_path is not None:
            break

    if file_path is None:
        return None

    with open(file_path) as json_file:
        json_data = json.load(json_file)
        parsed_values = parse(pattern).find(json_data)
        results.extend([i.value for i in parsed_values])

    if len(results) == 0:
        return "KEY_NOT_FOUND"

    if len(results) == 1:
        return results[0]

    return results
