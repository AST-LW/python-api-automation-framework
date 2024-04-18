-   To initialize the python project in the current directory - poetry init
-   To activate the virtual environment - poetry shell
-   To deactivate the virtual environment - exit
-   To get virtual environment info - poetry env info
-   To change the virtual environment to the current project - poetry config virtualenvs.in-project true
-   To install the virtual environment after adding the pyproject.toml file - poetry install

-   To install the poetry dependencies from lock file - poetry install --no-root
-   To install the package - poetry add <package_name>
-   To uninstall the package - poetry remove <package_name>
-   to install the dev dependency we use - poetry add <package_name> --dev

-   To execute the python file - poetry run python <relative_path_python_file>

-   To generate the build - poetry build
-   To publish a package - poetry publish

-   To publish a package to test pypi repository:

    -   Add the test pypi source to pyproject.toml - poetry source add pypi-test https://test.pypi.org/legacy/
    -   Add the pypi token to config - poetry config pypi-token.pypi-test <token>
    -   Publish to test pypi - poetry publish --repository pypi-test
        or poetry publish -r pypi-test

-   To set the token for pypi actual repository - poetry config pypi-token.pypi <token>

-   If poetry install is causing the issue then we can run the following command to resolve poetry lock dependencies to be resolved again - poetry lock --no-update

-   To avoid the **pycache** to be generated = export PYTHONDONTWRITEBYTECODE=1
