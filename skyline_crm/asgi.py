"""ASGI config for Skyline CRM."""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "skyline_crm.settings")

application = get_asgi_application()
