"""URL configuration for the pizzas app. The project's urls.py includes these addresses."""

from django.urls import path

from . import views

app_name = "pizzas"

urlpatterns = [
    # The home page: the empty address.
    path("", views.index, name="index"),
]
