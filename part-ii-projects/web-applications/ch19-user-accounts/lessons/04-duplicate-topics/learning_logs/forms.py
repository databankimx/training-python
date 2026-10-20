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

    def __init__(self, *args, owner=None, **kwargs) -> None:
        """Remember the user who is adding the topic, so the name can be checked against their topics."""
        super().__init__(*args, **kwargs)
        self.owner = owner

    def clean_text(self) -> str:
        """Reject a name the user already has. Capital letters don't count, so chess and Chess are the same."""
        text = self.cleaned_data["text"].strip()
        if self.owner is not None and Topic.objects.filter(owner=self.owner, text__iexact=text).exists():
            raise forms.ValidationError("You already have a topic with this name.")
        return text


class EntryForm(forms.ModelForm):
    """A form for adding a new entry to a topic. It uses the Entry model."""

    class Meta:
        """Which model the form uses, which of its fields the form shows, and how the box looks."""

        model = Entry
        fields = ["text"]
        labels = {"text": ""}
        # A wider box, with room for several lines of text.
        widgets = {"text": forms.Textarea(attrs={"cols": 80})}
