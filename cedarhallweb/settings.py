import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
DEBUG = os.environ.get("DEBUG") == "1"
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "localhost").split(",")
INSTALLED_APPS = ["django.contrib.contenttypes", "rest_framework", "orders"]
DATABASES = {"default": {"ENGINE": "django.db.backends.postgresql", "NAME": os.environ.get("DB_NAME", "app"), "USER": os.environ.get("DB_USER", "app"), "PASSWORD": os.environ.get("DB_PASSWORD", ""), "HOST": os.environ.get("DB_HOST", "localhost")}}
ROOT_URLCONF = "cedarhallweb.urls"
