#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# Admin yaratish (Render Environment bo'limida DJANGO_SUPERUSER_... o'zgaruvchilari bo'lishi kerak)
python manage.py createsuperuser --noinput || true