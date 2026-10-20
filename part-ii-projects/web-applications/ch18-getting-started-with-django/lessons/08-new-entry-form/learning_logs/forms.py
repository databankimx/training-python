"""Forms for the learning_logs app. A form turns what a visitor types into data the app can save."""

from django import forms

from .models import Entry, Topic


class TopicForm(forms.ModelForm):
    """A form for adding a new topic. It uses the Topic model."""

    class Meta:
        """Which model the form uses, and which of its fields the form shows."""

        model = Topic
        fields = ["text"]
        # Leave the label blank, so the box is labelled by the sentence above it.
        labels = {"text": ""}


class EntryForm(forms.ModelForm):
    """A form for adding a new entry to a topic. It uses the Entry model."""

    class Meta:
        """Which model the form uses, which of its fields the form shows, and how the box looks."""

        model = Entry
        fields = ["text"]
        labels = {"text": ""}
        # A wider box, with room for several lines of text.
        widgets = {"text": forms.Textarea(attrs={"cols": 80})}
