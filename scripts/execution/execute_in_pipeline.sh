#!/bin/bash

pytest . --alluredir=allure-results -m ${SUITE} -n ${INSTANCES}

# allure report generation from within the container
chmod +x scripts/util-scripts/generate-allure-report.sh
scripts/util-scripts/generate-allure-report.sh

# extract the test execution summary
ls -a
python3 src/utils/test_summary_extractor.py