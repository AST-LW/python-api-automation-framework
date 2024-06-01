FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.8.2 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv" \
    ROOT_DIR="/opt/pysetup"

# prepend poetry and venv to path
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

RUN apt-get update && apt-get install --no-install-recommends -y curl build-essential

# install poetry - respects $POETRY_VERSION & $POETRY_HOME
RUN curl -sSL https://install.python-poetry.org | python

# Installing Java and Allure for report generation in the container
RUN apt-get update && \
    apt-get install -y curl tar gzip default-jdk

# Set JAVA_HOME environment variable
ENV JAVA_HOME=/usr/lib/jvm/default-java

# Download and install Allure
ENV ALLURE_VERSION=2.29.0
RUN mkdir -p /opt/allure && \
    curl -sSL https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/${ALLURE_VERSION}/allure-commandline-${ALLURE_VERSION}.tgz | tar -xz -C /opt/allure --strip-components=1

# Add Allure to PATH
ENV PATH="/opt/allure/bin:${JAVA_HOME}/bin:${PATH}"
WORKDIR $PYSETUP_PATH
COPY ./ ./

# Set executable permissions for the script
RUN chmod +x scripts/execution/execute_in_pipeline.sh

# install runtime deps - uses $POETRY_VIRTUALENVS_IN_PROJECT internally
RUN poetry install --no-dev

CMD ["scripts/execution/execute_in_pipeline.sh"]