FROM python:3.9.6-buster as production

WORKDIR /app

RUN apt-get -y update && \
    apt-get -y upgrade

RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add && \
    echo "deb http://apt.postgresql.org/pub/repos/apt/ bionic-pgdg main" | tee /etc/apt/sources.list.d/pgdg.list && \
    apt-get update && apt-get -y install postgresql-client-12

COPY pyproject.toml poetry.lock ./
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

RUN poetry install --no-root --no-dev
EXPOSE 80
COPY . .
ENV LOG_LEVEL info
ENV PYTHONPATH=.
CMD ["python", "-m","uvicorn","app.main:app","--host","0.0.0.0","--port","80"]
