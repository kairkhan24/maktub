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
"DEV_CELERY_WORKER")
    wait_for "${BROKER_HOST}" "${BROKER_PORT}"
    python manage.py celery_worker
    ;;
"DEV_CELERY_BEAT")
    wait_for "${BROKER_HOST}" "${BROKER_PORT}"
    celery -A apps.taskapp beat -l info
    ;;
"DEV_CELERY_BEAT")
    wait_for "${BROKER_HOST}" "${BROKER_PORT}"
    celery -A apps.taskapp beat -l info
    ;;
"DJANGO")
    wait_for "${POSTGRES_HOST}" "${POSTGRES_PORT}"
    python manage.py collectstatic --noinput &&
    python manage.py migrate
    uvicorn config.asgi:application --reload-dir apps --debug --host 0.0.0.0 --port 8000 --log-level info --use-colors
    ;;
"CELERY_WORKER")
    wait_for "${BROKER_HOST}" "${BROKER_PORT}"
    echo 'vm.overcommit_memory = 1' >> /etc/sysctl.conf
    case "$NODE" in
    "SCHEDULER")
        celery -A apps.taskapp beat --loglevel=INFO
        ;;
    "CONSUMER")
        celery -A apps.taskapp worker --loglevel=INFO \
        --concurrency=3 --max-tasks-per-child=2048
        ;;
    *)
        echo "NO NODE SPECIFIED!"
        exit 1
        ;;
    esac
    ;;
"FLOWER")
    wait_for "${BROKER_HOST}" "${BROKER_PORT}"
    celery flower \
    --app=apps.taskapp \
    --broker="${CELERY_BROKER_URL}" \
    --basic_auth="${FLOWER_USER}:${FLOWER_PASSWORD}"
    ;;
*)
    echo "NO PROCESS SPECIFIED!"
    exit 1
    ;;
esac
