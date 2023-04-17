import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Apiary_online.settings')

app = Celery('Apiary_online')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    # Executes every hour at хх:05
    'add-every-hour': {
        'task': 'tasks.get_meteo_api',
        'schedule': crontab(minute=5),
        'args': (16, 16),
    },
}

'''
https://www.kaefik.ru/2021/09/23/python-celery/

tasks.py

from celery.decorators import task
from celery.decorators import periodic_task
from celery.task.schedules import crontab

@periodic_task(run_every=crontab(hour=0, minute=10))
def transactions():
    print "Task is executed every day on 0:10"
'''