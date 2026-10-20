"""
URL configuration for the Blog project, with user accounts added.

Each app's addresses are included here. Sign-in and registration are under accounts/.
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("", include("blogs.urls")),
]
