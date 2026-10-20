"""The views for the learning_logs app. A view receives a request and returns a response."""

from django.shortcuts import get_object_or_404, render

from .models import Topic


def index(request):
    """The home page for Learning Log."""
    return render(request, "learning_logs/index.html")


def topics(request):
    """Show every topic, in the order they were added."""
    topics = Topic.objects.order_by("date_added")
    context = {"topics": topics}
    return render(request, "learning_logs/topics.html", context)


def topic(request, topic_id):
    """Show one topic and all of its entries, newest first."""
    topic = get_object_or_404(Topic, id=topic_id)
    entries = topic.entry_set.order_by("-date_added")
    context = {"topic": topic, "entries": entries}
    return render(request, "learning_logs/topic.html", context)
