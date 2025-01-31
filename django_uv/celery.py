from celery import Celery 
import os

from django_uv.settings import CELERY_BROKER_URL,CELERY_RESULT_BACKEND
# Set the default Django settings module for the 'celery' program. 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_uv.settings')  
# Create a new Celery 
app = Celery('django_uv')
# Configure Celery to use Django's settings 
app.config_from_object('django.conf:settings', namespace='CELERY')  

# Update or customize further configurations if needed
# app.conf.broker_url = CELERY_BROKER_URL
# app.conf.result_backend = CELERY_RESULT_BACKEND

# Define queues for task types
app.conf.task_queues = {
    "long_tasks": {"exchange": "long", "routing_key": "long"},
    "short_tasks": {"exchange": "short", "routing_key": "short"},
    "system_tasks": {"exchange": "system", "routing_key": "system"},
}

app.conf.task_default_queue = "long_tasks"

app.conf.beat_schedule = {
    
}

# Auto-discover tasks from all installed apps 
app.autodiscover_tasks()

