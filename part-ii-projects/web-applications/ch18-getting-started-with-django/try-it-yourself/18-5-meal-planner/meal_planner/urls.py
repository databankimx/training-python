"""
URL configuration for the Meal Planner project.

The app's addresses are included here, so the home page is at the empty address.
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("meal_plans.urls")),
]
