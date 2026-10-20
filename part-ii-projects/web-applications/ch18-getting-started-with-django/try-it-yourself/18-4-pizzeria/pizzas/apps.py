"""Configuration for the pizzas app."""

from django.apps import AppConfig


class PizzasConfig(AppConfig):
    """The settings Django uses for the pizzas app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "pizzas"
