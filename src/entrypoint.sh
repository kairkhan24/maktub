#!/bin/bash

export DATABASE_URL="postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}";
echo ${DATABASE_URL}

case "$PROCESS" in
"LINT")
    mypy . && flake8 . && bandit -r . && safety check
    ;;
"DEV_DJANGO")
    wait_for "${POSTGRES_HOST}" "${POSTGRES_PORT}"
    python manage.py collectstatic --noinput &&
    python manage.py migrate  &&
#    python manage.py runserver 0.0.0.0:8000
    uvicorn config.asgi:application --reload-dir apps --debug --host 0.0.0.0 --port 8000 --log-level info --use-colors
    ;;
"DJANGO")
    wait_for "${POSTGRES_HOST}" "${POSTGRES_PORT}"
    python manage.py collectstatic --noinput &&
    python manage.py migrate
    uvicorn config.asgi:application --reload-dir apps --debug --host 0.0.0.0 --port 8000 --log-level info --use-colors
    ;;
esac
