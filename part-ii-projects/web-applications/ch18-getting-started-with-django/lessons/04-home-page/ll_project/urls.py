"""
URL configuration for the Learning Log project.

The urlpatterns list routes URLs to views. Each app's URLs are added here as the project grows.
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # Everything the learning_logs app handles, such as the home page.
    path("", include("learning_logs.urls")),
]
