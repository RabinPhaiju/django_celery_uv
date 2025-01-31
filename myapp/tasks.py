from celery import shared_task 
from django.contrib.auth import get_user_model
# settings 
from django_uv.settings import LANGUAGE_CODE

User = get_user_model()

@shared_task(queue="short_tasks")
def add(x, y): 
    return x + y


@shared_task(queue="short_tasks")
def hello(name):
    user = User.objects.filter(username=name).first()

    return f"hello world {name}--{user.id}--{LANGUAGE_CODE}"

@shared_task(queue="system_tasks")
def cleanup_temp_files():
    return "Temporary files cleaned up!..."

@shared_task(queue="short_tasks")
def send_email_notification():
    return "Email sent successfully!"

@shared_task(queue="long_tasks")
def process_large_data():
    import time
    time.sleep(10)  # Simulate long task
    print("Long-running task completed!!!")
    return "Long-running task completed!"

@shared_task(queue="short_tasks")
def test_appConfig(name):
    from myapp.models import MyappConfig
    group,create = MyappConfig.objects.get_or_create(name='test')
    group.value = name
    group.save()
    return group.value