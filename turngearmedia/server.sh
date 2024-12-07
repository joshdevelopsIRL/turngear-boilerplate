#!/bin/ash

if [ ! -f .dockersetup ]; then
  python manage.py makemigrations
  python manage.py migrate
  touch .dockersetup
fi

python manage.py runserver "0.0.0.0:8000"
