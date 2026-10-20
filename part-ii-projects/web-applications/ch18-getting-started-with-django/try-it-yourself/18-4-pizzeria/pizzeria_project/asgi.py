"""
ASGI config for the Pizzeria project.

It exposes the ASGI callable as a module-level variable named application. The project uses WSGI, so this file is
here for completeness.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizzeria_project.settings")

application = get_asgi_application()
