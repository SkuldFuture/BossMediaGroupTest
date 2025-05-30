#!/bin/bash
set -e

ENV_FILE=".env"

if [ -f "$ENV_FILE" ]; then
  export BACKEND_PORT=$(grep -E '^BACKEND_PORT=' "$ENV_FILE" | cut -d '=' -f2 | tr -d '[:space:]')
  echo "BACKEND_PORT = $BACKEND_PORT"
fi

if [ -z "$BACKEND_PORT" ]; then
  echo "BACKEND_PORT не задан"
  exit 1
fi

echo "Применение миграций..."
python manage.py migrate

echo "Сбор статиков..."
python manage.py collectstatic --noinput

echo "Создание суперпользователя..."
python manage.py createsuperuser_if_none_exist

echo "Запуск Django-сервера..."
python manage.py runserver 0.0.0.0:$BACKEND_PORT
