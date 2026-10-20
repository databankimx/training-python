"""Configuration for the meal_plans app."""

from django.apps import AppConfig


class MealPlansConfig(AppConfig):
    """The settings Django uses for the meal_plans app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "meal_plans"
