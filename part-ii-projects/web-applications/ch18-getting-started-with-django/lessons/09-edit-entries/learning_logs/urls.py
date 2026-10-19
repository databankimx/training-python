"""URL configuration for the learning_logs app. These URLs are added to the project's list in ll_project/urls.py."""

from django.urls import path

from . import views

app_name = "learning_logs"

urlpatterns = [
    # The home page: the empty path, which is the address with nothing after the port.
    path("", views.index, name="index"),
    # The page that lists every topic.
    path("topics/", views.topics, name="topics"),
    # The page for one topic. The number in the address is the topic's id.
    path("topics/<int:topic_id>/", views.topic, name="topic"),
    # The page for adding a new topic.
    path("topics/new/", views.new_topic, name="new_topic"),
    # The page for adding a new entry to one topic.
    path("topics/<int:topic_id>/new_entry/", views.new_entry, name="new_entry"),
    # The page for editing one entry. The number in the address is the entry's id.
    path("entries/<int:entry_id>/edit/", views.edit_entry, name="edit_entry"),
]
