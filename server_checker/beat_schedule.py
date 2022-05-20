from celery.schedules import crontab


CELERYBEAT_SCHEDULE = {
    'check-servers-connection-every-1-minute': {
        'task': 'servers.tasks.check_connection',
        'schedule': crontab(minute='*/1'),
        'args': None
    }
}
