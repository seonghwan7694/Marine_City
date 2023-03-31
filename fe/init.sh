#!/bin/bash

rm -rf app/migrations/*
rm -rf db.sqlite3
rm -rf static/*

touch app/migrations/__init__.py

python manage.py makemigrations
python manage.py migrate

echo yes | python3 manage.py collectstatic
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'qwert1234')" | python manage.py shell
python3 manage.py loaddata fixtures/*.json
python3 manage.py runserver
# uwsgi --http :8000 --module conf.wsgi