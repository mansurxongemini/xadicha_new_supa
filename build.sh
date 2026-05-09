#!/usr/bin/env bash
# Xatolik bo'lsa to'xtash, lekin biz ba'zi buyruqlarni xavfsiz qilamiz
set -o errexit

pip install -r requirements.txt

# Statik fayllarni yig'ish (agar xato bo'lsa ham skript to'xtamaydi)
python manage.py collectstatic --no-input || true

# Bazani migratsiya qilish (BU ENG MUHIMI, u endi albatta ishlaydi)
python manage.py migrate

# Admin yaratish
python manage.py createsuperuser --noinput || true