from __future__ import absolute_import, unicode_literals
import os

from celery import Celery

from .beat_schedule import *


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server_checker.settings')

app = Celery('server_checker')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.update({'beat_schedule': CELERYBEAT_SCHEDULE})

app.autodiscover_tasks()
