"""
URL configuration for the Pizzeria project.

Each app's URLs are added to this list as the project grows.
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # Everything the pizzas app handles, such as the home page.
    path("", include("pizzas.urls")),
]
