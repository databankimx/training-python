"""
WSGI config for the Learning Log project.

It exposes the WSGI callable as a module-level variable named application. Web servers use it to run the project
when it's deployed.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ll_project.settings")

application = get_wsgi_application()
