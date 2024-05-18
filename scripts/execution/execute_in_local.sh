#!/bin/bash


# Clean all the reports and logs before test execution
chmod +x scripts/util-scripts/clear-reports.sh
scripts/util-scripts/clear-reports.sh

pytest . --alluredir=allure-results -m local

# Remove the pycache files from the code-base once the execution is done
python src/utils/remove_python_cache_files.py

# Execute generate-allure-report.sh script
chmod +x scripts/util-scripts/generate-allure-report.sh
scripts/util-scripts/generate-allure-report.sh