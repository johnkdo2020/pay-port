# `python-base` sets up all our shared environment variables
FROM python:3.7-slim as python-base

RUN         apt -y update && apt -y dist-upgrade && apt -y autoremove
RUN         apt -y install nginx


            # python
ENV         PYTHONUNBUFFERED=1 \
            # prevents python creating .pyc files
            PYTHONDONTWRITEBYTECODE=1 \
            \
            # pip
            PIP_NO_CACHE_DIR=off \
            PIP_DISABLE_PIP_VERSION_CHECK=on \
            PIP_DEFAULT_TIMEOUT=100 \
            \
            # poetry
            # https://python-poetry.org/docs/configuration/#using-environment-variables
            POETRY_VERSION=1.0.3 \
            # make poetry install to this location
            POETRY_HOME="/opt/poetry" \
            # make poetry create the virtual environment in the project's root
            # it gets named `.venv`
            POETRY_VIRTUALENVS_IN_PROJECT=true \
            # do not ask any interactive question
            POETRY_NO_INTERACTION=1 \
            \
             # paths
                                     # this is where our requirements + virtual environment will live
            PYSETUP_PATH="/opt/pysetup" \
            VENV_PATH="/opt/pysetup/.venv"

ENV         PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

            # `builder-base` stage is used to build deps + create our virtual environment


FROM        python-base as builder-base

RUN         apt-get update \
            && apt-get install --no-install-recommends -y \
            # deps for installing poetry
            curl \
            # deps for building python deps
            build-essential



# install poetry - respects $POETRY_VERSION & $POETRY_HOME
RUN         curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

# copy project requirement files here to ensure they will be cached.
WORKDIR     $PYSETUP_PATH
COPY        poetry.lock pyproject.toml ./

# install runtime deps - uses $POETRY_VIRTUALENVS_IN_PROJECT internally
RUN         poetry install --no-dev
# `development` image is used during development / testing
FROM        python-base as development
ENV         FASTAPI_ENV=development
WORKDIR     $PYSETUP_PATH

# copy in our built poetry + venv
COPY        --from=builder-base $POETRY_HOME $POETRY_HOME
COPY        --from=builder-base $PYSETUP_PATH $PYSETUP_PATH

# quicker install as runtime deps are already installed
RUN         poetry install

# 소스코드 복사
COPY        . /srv/iamport
WORKDIR     /srv/iamport/app

RUN         rm /etc/nginx/sites-enabled/default
RUN         cp /srv/iamport/.config/local_dev/iamport.nginx /etc/nginx/sites-enabled/

RUN         mkdir /var/log/gunicorn

CMD         /bin/bash
