#!/bin/bash

# Set the path to the log folder
LOG_FOLDER="./logs"

# Set the path to the allure results & reports folder
ALLURE_RESULTS_FOLDER="./allure-results"
ALLURE_REPORT_FOLDER="./allure-report"
TEST_SUMMARY_FILE="./test-summary.json"

# Function to remove a folder if it exists
remove_folder() {
    local folder_path="$1"
    local folder_name="$2"

    if [ -d "$folder_path" ]; then
        rm -rf "$folder_path"
        echo "$folder_name folder removed successfully."
    else
        echo "The $folder_name folder does not exist."
    fi
}

# Remove the logs folder if it exists
remove_folder "$LOG_FOLDER" "logs"

# Remove the allure-results folder if it exists
remove_folder "$ALLURE_RESULTS_FOLDER" "allure-results"

# Remove the allure-report folder if it exists
remove_folder "$ALLURE_REPORT_FOLDER" "allure-report"

# Remove the test summary json file
echo "test-summary file removed successfully."
rm -rf "$TEST_SUMMARY_FILE"