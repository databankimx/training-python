"""Tests for the styled pages, for chapter 20, step 3."""

from django.contrib.auth.models import User
from django.test import TestCase

from .models import Entry, Topic


class StyledPageTests(TestCase):
    """Check that the main pages use the Bootstrap styles."""

    def setUp(self) -> None:
        """Make a user with a topic and an entry, and sign them in."""
        self.user = User.objects.create_user("sam", "sam@example.com", "a-long-test-password-1")
        self.client.force_login(self.user)
        self.topic = Topic.objects.create(text="Chess", owner=self.user)
        Entry.objects.create(topic=self.topic, text="Knights move in an L shape.")

    def test_home_page_has_a_banner(self) -> None:
        """The home page should show a large banner, styled by Bootstrap."""
        response = self.client.get("/")
        self.assertContains(response, "p-5 mb-4 bg-light rounded-3")

    def test_topics_page_uses_a_list_group(self) -> None:
        """The topics should be shown as a Bootstrap list group."""
        response = self.client.get("/topics/")
        self.assertContains(response, "list-group")

    def test_topic_page_shows_entries_as_cards(self) -> None:
        """Each entry on the topic page should be a Bootstrap card."""
        response = self.client.get(f"/topics/{self.topic.id}/")
        self.assertContains(response, 'class="card mb-3"')

    def test_login_page_has_a_styled_button(self) -> None:
        """The login page's button should use Bootstrap's primary button style."""
        self.client.logout()
        response = self.client.get("/accounts/login/")
        self.assertContains(response, "btn btn-primary")
