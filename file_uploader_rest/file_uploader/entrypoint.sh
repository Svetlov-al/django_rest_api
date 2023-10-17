#!/bin/bash

if [[ "${1}" == "web" ]]; then
    python3 manage.py migrate
    python3 manage.py collectstatic --noinput
    python3 manage.py runserver 0.0.0.0:8000
elif [[ "${1}" == "celery" ]]; then
    celery -A core worker --loglevel=info
fi
