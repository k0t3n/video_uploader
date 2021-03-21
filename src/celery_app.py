"""
Disclaimer: DO NOT rename this file to celery.py, it will cause import collision
"""

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')

app = Celery('celery-app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_scheduler = 'django_celery_beat.schedulers:DatabaseScheduler'
