#!/bin/bash

ROOT_DIR="$(git rev-parse --show-toplevel)"

ALLURE_RESULTS_DIR="$ROOT_DIR/allure-results"
ALLURE_REPORT_DIR="$ROOT_DIR/allure-report"

# Check if the allure report directory exists
if [ -d "$ALLURE_REPORT_DIR" ]; then
  echo "Deleting existing allure report directory."
  rm -rf "$ALLURE_REPORT_DIR"
fi

# Check if allure results directory exists
if [ ! -d "$ALLURE_RESULTS_DIR" ]; then
  echo "Error: allure results directory '$ALLURE_RESULTS_DIR' not found."
  exit 1
fi

# Create the directory to store allure reports
mkdir -p "$ALLURE_REPORT_DIR"

# Generate allure report from allure results
allure generate "$ALLURE_RESULTS_DIR" --clean -o "$ALLURE_REPORT_DIR"