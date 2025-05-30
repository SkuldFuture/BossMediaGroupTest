FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/BossMediaGroupTest

RUN apt-get update && apt-get install -y libpq-dev gcc

WORKDIR /BossMediaGroupTest

COPY pyproject.toml .
COPY poetry.lock .
COPY .env .

RUN python -m pip install --upgrade pip \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

COPY . .
RUN chmod +x run.sh
CMD /BossMediaGroupTest/run.sh