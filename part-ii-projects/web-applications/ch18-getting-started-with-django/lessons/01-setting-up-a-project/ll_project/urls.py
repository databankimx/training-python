"""
URL configuration for the Learning Log project.

The urlpatterns list routes URLs to views. Each app's URLs are added here as the project grows.
"""

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]
