"""
URL configuration for the Blog project.

Each app's addresses are included here. The blog pages are at the top of the site.
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blogs.urls")),
]
