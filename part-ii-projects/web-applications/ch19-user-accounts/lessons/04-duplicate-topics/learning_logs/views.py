"""The views for the learning_logs app. A view receives a request and returns a response."""

from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EntryForm, TopicForm
from .models import Entry, Topic


def index(request):
    """The home page for Learning Log."""
    return render(request, "learning_logs/index.html")


@login_required
def topics(request):
    """Show the signed-in user's topics, in the order they were added."""
    topics = Topic.objects.filter(owner=request.user).order_by("date_added")
    context = {"topics": topics}
    return render(request, "learning_logs/topics.html", context)


@login_required
def topic(request, topic_id):
    """Show one of the signed-in user's topics and all of its entries, newest first."""
    topic = get_object_or_404(Topic, id=topic_id)
    # A topic that belongs to someone else is treated as not found, so their topics stay private.
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by("-date_added")
    context = {"topic": topic, "entries": entries}
    return render(request, "learning_logs/topic.html", context)


@login_required
def new_topic(request):
    """Add a new topic for the signed-in user. On a GET request, show an empty form."""
    if request.method != "POST":
        form = TopicForm()
    else:
        # The form needs the user, so it can check the name against their own topics.
        form = TopicForm(data=request.POST, owner=request.user)
        if form.is_valid():
            # Build the topic, then record who owns it, before saving it.
            topic_record = form.save(commit=False)
            topic_record.owner = request.user
            topic_record.save()
            return redirect("learning_logs:topics")

    context = {"form": form}
    return render(request, "learning_logs/new_topic.html", context)


@login_required
def new_entry(request, topic_id):
    """Add a new entry to one of the signed-in user's topics."""
    topic = get_object_or_404(Topic, id=topic_id)
    if topic.owner != request.user:
        raise Http404

    if request.method != "POST":
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            # Build the entry, but don't save it yet, so the topic can be added first.
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect("learning_logs:topic", topic_id=topic.id)

    context = {"topic": topic, "form": form}
    return render(request, "learning_logs/new_entry.html", context)


@login_required
def edit_entry(request, entry_id):
    """Edit an entry on one of the signed-in user's topics."""
    entry = get_object_or_404(Entry, id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != "POST":
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("learning_logs:topic", topic_id=topic.id)

    context = {"entry": entry, "topic": topic, "form": form}
    return render(request, "learning_logs/edit_entry.html", context)
