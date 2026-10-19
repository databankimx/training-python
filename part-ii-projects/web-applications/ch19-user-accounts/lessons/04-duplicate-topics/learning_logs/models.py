"""The models for the learning_logs app. A model describes the data the app stores."""

from django.contrib.auth.models import User
from django.db import models


class Topic(models.Model):
    """A topic the user is learning about. Each topic belongs to the user who created it."""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        """A user can't have two topics with the same text. The database enforces this as well as the form."""

        constraints = [
            models.UniqueConstraint(fields=["owner", "text"], name="unique_topic_per_owner"),
        ]

    def __str__(self) -> str:
        """Return a string representation of the topic."""
        return self.text


class Entry(models.Model):
    """Something specific the user has learned about a topic."""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Settings for the Entry model."""

        verbose_name_plural = "entries"

    def __str__(self) -> str:
        """Return a short preview of the entry's text."""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        return self.text
