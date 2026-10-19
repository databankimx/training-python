"""The views for the learning_logs app. A view receives a request and returns a response."""

from django.shortcuts import render

from .models import Topic


def index(request):
    """The home page for Learning Log."""
    return render(request, "learning_logs/index.html")


def topics(request):
    """Show every topic, in the order they were added."""
    topics = Topic.objects.order_by("date_added")
    context = {"topics": topics}
    return render(request, "learning_logs/topics.html", context)
