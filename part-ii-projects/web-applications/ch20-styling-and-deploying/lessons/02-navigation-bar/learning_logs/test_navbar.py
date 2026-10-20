"""Tests for the Bootstrap navigation bar, for chapter 20, step 2."""

from django.contrib.auth.models import User
from django.test import TestCase


class NavigationBarTests(TestCase):
    """Check the navigation bar that every page shares."""

    def test_home_page_has_a_navigation_bar(self) -> None:
        """The home page should show the Bootstrap navigation bar, with the Learning Log name."""
        response = self.client.get("/")
        self.assertContains(response, 'class="navbar')
        self.assertContains(response, 'class="navbar-brand"')

    def test_navigation_bar_links_to_topics(self) -> None:
        """Every visitor should see a Topics link in the navigation bar."""
        response = self.client.get("/")
        self.assertContains(response, 'href="/topics/"')

    def test_signed_in_user_sees_a_log_out_button(self) -> None:
        """A signed-in user should see their name and a Log out button in the navigation bar."""
        User.objects.create_user("sam", "sam@example.com", "a-long-test-password-1")
        self.client.login(username="sam", password="a-long-test-password-1")
        response = self.client.get("/")
        self.assertContains(response, "Hello, sam.")
        self.assertContains(response, "btn btn-outline-light")
