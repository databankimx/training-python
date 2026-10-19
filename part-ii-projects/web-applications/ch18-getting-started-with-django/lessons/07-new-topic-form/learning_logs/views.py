"""The views for the learning_logs app. A view receives a request and returns a response."""

from django.shortcuts import get_object_or_404, redirect, render

from .forms import TopicForm
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


def new_topic(request):
    """Add a new topic. On a GET request, show an empty form. On a POST, save the form if it's valid."""
    if request.method != "POST":
        # No data was submitted, so show a blank form.
        form = TopicForm()
    else:
        # The visitor submitted the form, so check the data and save it.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("learning_logs:topics")

    context = {"form": form}
    return render(request, "learning_logs/new_topic.html", context)
