"""Tests for the Bootstrap styling of the Blog, for exercise 20-2."""

from django.contrib.auth.models import User
from django.test import TestCase

from .models import Blog, BlogPost


class StylishBlogTests(TestCase):
    """Check that the Blog's pages use the Bootstrap styles."""

    def setUp(self) -> None:
        """Make a user with a blog and a post, and sign them in."""
        self.user = User.objects.create_user("sam", "sam@example.com", "a-long-test-password-1")
        self.client.force_login(self.user)
        blog = Blog.objects.create(title="Travel", owner=self.user)
        BlogPost.objects.create(blog=blog, title="Lisbon", text="Trams and pastries.")

    def test_pages_have_a_navigation_bar(self) -> None:
        """Every page should show the Bootstrap navigation bar."""
        response = self.client.get("/")
        self.assertContains(response, 'class="navbar')

    def test_home_page_shows_posts_as_cards(self) -> None:
        """Each post on the home page should be a Bootstrap card."""
        response = self.client.get("/")
        self.assertContains(response, 'class="card mb-3"')

    def test_new_blog_form_uses_bootstrap_button(self) -> None:
        """The new blog form should use Bootstrap's primary button style."""
        response = self.client.get("/blogs/new/")
        self.assertContains(response, "btn btn-primary")
