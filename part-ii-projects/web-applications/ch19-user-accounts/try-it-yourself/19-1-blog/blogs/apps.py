"""Configuration for the blogs app."""

from django.apps import AppConfig


class BlogsConfig(AppConfig):
    """The settings Django uses for the blogs app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "blogs"
