#!/bin/bash
set -e
echo "🗃️ Применение миграций..."
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser_if_none_exist
echo "Запуск Django-сервера..."
python manage.py runserver 0.0.0.0:8011