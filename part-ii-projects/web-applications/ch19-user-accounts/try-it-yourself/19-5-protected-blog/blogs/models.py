"""The models for the blogs app. A model describes the data the app stores."""

from django.contrib.auth.models import User
from django.db import models


class Blog(models.Model):
    """An overall blog, such as Travel or Recipes. Each blog belongs to the user who made it."""

    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        """Return the blog's title."""
        return self.title


class BlogPost(models.Model):
    """One post in a blog."""

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Show the newest posts first. The id is a tie-breaker for posts saved in the same instant."""

        ordering = ["-date_added", "-id"]

    def __str__(self) -> str:
        """Return the post's title."""
        return self.title
