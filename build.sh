#!/usr/bin/env bash
set -o errexit

python manage.py migrate --noinput
python manage.py collectstatic --noinput
python manage.py createsuperuser --noinput || true
