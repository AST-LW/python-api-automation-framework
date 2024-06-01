#!/bin/bash

pytest . --alluredir=allure-results -m ${SUITE} -n ${INSTANCES}

