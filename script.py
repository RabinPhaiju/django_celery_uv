import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_uv.settings')
django.setup()


# Short Task
from myapp.tasks import hello,add,send_email_notification,test_appConfig
# hello.delay("rabin")
# add.delay(3,3)
# send_email_notification.delay()

# Long Task
from myapp.tasks import process_large_data
process_large_data.delay()

# System Task
# from myapp.tasks import cleanup_temp_files
# cleanup_temp_files.delay()

# from celery.result import AsyncResult
# from django_uv.celery import app
# task_id = "bcc96bbb-3eb5-4683-8b32-c6fa88cc085a"
# result = AsyncResult(task_id, app=app)
# print(result.status)  # e.g., "SUCCESS", "FAILURE"
# print(result.result)
# print(result.info)


test_appConfig.delay('test1')