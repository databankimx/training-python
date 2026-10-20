"""
URL configuration for the Pizzeria project.

Each app's URLs are added to this list as the project grows. Exercises 18-6 and 18-8 add the pizza pages.
"""

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]
