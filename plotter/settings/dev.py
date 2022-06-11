from .base import *

DEBUG = True
SECRET_KEY = "something"
ALLOWED_HOSTS = ["*"]
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

INSTALLED_APPS.append("django_extensions")

try:
    from .local import *
except ImportError:
    pass
