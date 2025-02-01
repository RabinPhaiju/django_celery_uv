import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_uv.settings')
django.setup()

from celery.result import AsyncResult
from django_uv.celery import app

# Short Task
from myapp.tasks import hello,add,send_email_notification,test_appConfig,process_large_data,cleanup_temp_files
# hello.delay("rabin")
# add.delay(3,3)
# send_email_notification.delay()

# Long Task
# process_large_data.delay()

# System Task
cleanup_temp_files.delay()


# print('-------',app.conf.result_backend)
# task_id = "86c739a1-78d0-4a90-9241-92446d7cb05a"
# result = AsyncResult(task_id,app=app)
# result = process_large_data.AsyncResult(task_id)
# print(result.status)  # e.g., "SUCCESS", "FAILURE"
# print(result.result,'--info:',result.info)

