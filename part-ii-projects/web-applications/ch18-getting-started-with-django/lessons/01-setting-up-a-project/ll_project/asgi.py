"""
ASGI config for the Learning Log project.

It exposes the ASGI callable as a module-level variable named application. ASGI servers can use it to run the
project. Learning Log uses WSGI, so this file is here for completeness.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ll_project.settings")

application = get_asgi_application()
