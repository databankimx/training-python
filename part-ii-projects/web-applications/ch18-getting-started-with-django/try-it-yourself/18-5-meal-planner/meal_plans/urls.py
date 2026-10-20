"""URL configuration for the meal_plans app. The project's urls.py includes these addresses."""

from django.urls import path

from . import views

app_name = "meal_plans"

urlpatterns = [
    # The home page: the empty address.
    path("", views.index, name="index"),
]
