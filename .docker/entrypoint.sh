#!/bin/ash

python3 manage.py collectstatic --no-input
python3 manage.py migrate --no-input

gunicorn buzzers_n_hoopers.wsgi $@
