import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ded.settings')
app = Celery('ded')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Периодическая таска, запускается каждый день в 6 утра
app.conf.beat_schedule = {
    'send_email_user_reminder_every_year': {
        'task': 'about_present.tasks.send_periodic_email_every_year',
        'schedule': crontab(minute=0, hour=6, ),
    },
}
