"""Forms for the blogs app. A form turns what a visitor types into data the app can save."""

from django import forms

from .models import Blog, BlogPost


class BlogForm(forms.ModelForm):
    """A form for making a new blog."""

    class Meta:
        """Which model the form uses, and which of its fields the form shows."""

        model = Blog
        fields = ["title"]
        labels = {"title": ""}


class BlogPostForm(forms.ModelForm):
    """A form for writing a post, or editing one."""

    class Meta:
        """Which model the form uses, which fields it shows, and how the text box looks."""

        model = BlogPost
        fields = ["title", "text"]
        labels = {"title": "", "text": ""}
        widgets = {"text": forms.Textarea(attrs={"cols": 80})}
