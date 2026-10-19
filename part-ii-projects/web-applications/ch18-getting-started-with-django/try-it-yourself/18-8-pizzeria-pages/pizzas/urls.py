"""URL configuration for the pizzas app. The project's urls.py includes these addresses."""

from django.urls import path

from . import views

app_name = "pizzas"

urlpatterns = [
    # The home page: the empty address.
    path("", views.index, name="index"),
    # The list of every pizza.
    path("pizzas/", views.pizzas, name="pizzas"),
    # One pizza and its toppings. The number in the address is the pizza's id.
    path("pizzas/<int:pizza_id>/", views.pizza, name="pizza"),
]
