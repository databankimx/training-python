"""The models for the blogs app. A model describes the data the app stores."""

from django.db import models


class Blog(models.Model):
    """An overall blog, such as Travel or Recipes. Posts are written inside a blog."""

    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

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
        """Show the newest posts first."""

        ordering = ["-date_added", "-id"]

    def __str__(self) -> str:
        """Return the post's title."""
        return self.title
