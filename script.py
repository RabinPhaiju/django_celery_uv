# ruff: noqa: E402
import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_uv.settings')
django.setup()

# from django.contrib.auth import get_user_model

# User = get_user_model()

from myapp.tasks import hello,add

hello.delay("rabin")
add.delay(2,3)