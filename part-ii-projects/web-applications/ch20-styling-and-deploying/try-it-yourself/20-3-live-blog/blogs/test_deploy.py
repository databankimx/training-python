"""Tests for the live-ready Blog, for exercise 20-3."""

from django.conf import settings
from django.test import TestCase


class LiveBlogTests(TestCase):
    """Check the friendly error page, and the settings a live site needs."""

    def test_unknown_address_uses_the_blog_404_page(self) -> None:
        """An address that doesn't exist should show the Blog's 404 page, not Django's default."""
        response = self.client.get("/no-such-page/")
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "404.html")

    def test_404_page_has_a_friendly_message(self) -> None:
        """The 404 page should explain what happened, and offer a way back to the home page."""
        response = self.client.get("/no-such-page/")
        self.assertContains(response, "Page not found", status_code=404)
        self.assertContains(response, "Go to the home page", status_code=404)

    def test_static_files_are_collected_into_a_static_root(self) -> None:
        """A live site needs a folder for collected static files, so collectstatic has somewhere to put them."""
        self.assertIsNotNone(settings.STATIC_ROOT)
