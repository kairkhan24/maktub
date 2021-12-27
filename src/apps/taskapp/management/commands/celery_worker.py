import sys
import shlex
import subprocess

from django.utils import autoreload
from django.core.management.base import (
    BaseCommand,
)


def restart_celery():
    cmd = 'pkill -f "celery worker"'
    if sys.platform == 'win32':
        cmd = 'taskkill /f /t /im celery.exe'

    subprocess.call(shlex.split(cmd))
    subprocess.call(shlex.split(
        'celery -A apps.taskapp worker --loglevel=INFO --concurrency=1'
    ))


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Starting celery worker with autoreload...')
        autoreload.run_with_reloader(restart_celery)
