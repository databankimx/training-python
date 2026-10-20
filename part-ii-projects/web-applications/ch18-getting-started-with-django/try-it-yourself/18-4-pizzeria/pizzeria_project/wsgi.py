"""
WSGI config for the Pizzeria project.

It exposes the WSGI callable as a module-level variable named application. Web servers use it to run the project
when it's deployed.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizzeria_project.settings")

application = get_wsgi_application()
