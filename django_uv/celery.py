from celery import Celery 
import os  
# Set the default Django settings module for the 'celery' program. 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_uv.settings')  
# Create a new Celery 
app = Celery('django_uv')  
# Configure Celery to use Django's settings 
app.config_from_object('django.conf:settings', namespace='CELERY')  
# Auto-discover tasks from all installed apps 
app.autodiscover_tasks()