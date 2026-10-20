"""URL configuration for the learning_logs app. These URLs are added to the project's list in ll_project/urls.py."""

from django.urls import path

from . import views

app_name = "learning_logs"

urlpatterns = [
    # The home page: the empty path, which is the address with nothing after the port.
    path("", views.index, name="index"),
    # The page that lists every topic.
    path("topics/", views.topics, name="topics"),
]
