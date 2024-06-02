FROM python:3.12-bookworm as setup

ENV POETRY_HOME=/opt/poetry \
    PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH" \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv" \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=true
RUN python3 -m venv $POETRY_HOME
RUN $POETRY_HOME/bin/pip install poetry==1.8.0
RUN $POETRY_HOME/bin/poetry --version


FROM setup as build
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        # deps for installing poetry
        curl \
        # deps for building python deps
        build-essential

COPY --from=build $POETRY_HOME $POETRY_HOME
COPY --from=build $PYSETUP_PATH $PYSETUP_PATH

# copy project requirement files here to ensure they will be cached.
WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./

# install runtime deps - uses $POETRY_VIRTUALENVS_IN_PROJECT internally
RUN poetry install --no-dev


FROM build

COPY ./src /opt/unemployedda_blog

WORKDIR /opt/unemployedda_blog

RUN poetry install

EXPOSE 8001
ENTRYPOINT ["$POETRY_HOME/bin/fastapi", "run", "src/main.py", "--port", "8001"]