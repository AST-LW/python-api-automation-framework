# Poetry Cheatsheet

## Project Setup

-   Initialize a new Python project: `poetry init`
-   Change the virtual environment creation to the current project: `poetry config virtualenvs.in-project true`

## Virtual Environment Management

-   Activate the virtual environment: `poetry shell`
-   Deactivate the virtual environment: `exit`
-   Get virtual environment information: `poetry env info`

## Installing Dependencies

-   Install dependencies from `pyproject.toml`: `poetry install`
-   Install dependencies from `poetry.lock` without installing the current package: `poetry install --no-root`
-   Install a new package: `poetry add <package_name>`
-   Install a new development dependency: `poetry add <package_name> --dev`
-   Uninstall a package: `poetry remove <package_name>`

## Running Scripts

-   Execute a Python file: `poetry run python <relative_path_python_file>`

## Building and Publishing

-   Generate a build: `poetry build`
-   Publish to PyPI: `poetry publish`

## Publishing to Test PyPI

1. Add the Test PyPI source to `pyproject.toml`:
    ```
    poetry source add pypi-test https://test.pypi.org/legacy/
    ```
2. Add the Test PyPI token to the config:
    ```
    poetry config pypi-token.pypi-test <token>
    ```
3. Publish to Test PyPI:
    ```
    poetry publish --repository pypi-test
    ```
    or
    ```
    poetry publish -r pypi-test
    ```

## Building and Publishing to PyPI

-   Generate a build: `poetry build`
-   Publish to PyPI:
    1. Set the token for the actual PyPI repository:
        ```
        poetry config pypi-token.pypi <token>
        ```
    2. Publish to PyPI:
        ```
        poetry publish
        ```

## Troubleshooting

-   Resolve `poetry.lock` dependencies: `poetry lock --no-update`
-   Avoid generating `__pycache__`: `export PYTHONDONTWRITEBYTECODE=1`

## Setting the PyPI Token

-   Set the token for the actual PyPI repository: `poetry config pypi-token.pypi <token>`
