"""Tests for the shared layout and the home page, for chapter 2 of the Flask Learning Log."""

import unittest

from flask_log import create_app
from flask_log.database import Base


class LayoutTests(unittest.TestCase):
    """Check that the home page is built from the shared layout, with Bootstrap styling."""

    def setUp(self) -> None:
        """Build the app with its own in-memory database, and create its tables."""
        self.app = create_app({"DATABASE_URL": "sqlite:///:memory:", "TESTING": True})
        Base.metadata.create_all(self.app.extensions["engine"])
        self.client = self.app.test_client()

    def test_home_page_has_the_navigation_bar(self) -> None:
        """The shared layout should give every page a Bootstrap navigation bar."""
        response = self.client.get("/")
        self.assertIn(b'class="navbar', response.data)

    def test_home_page_has_the_banner(self) -> None:
        """The home page should show its banner, which comes from index.html."""
        response = self.client.get("/")
        self.assertIn(b"Track your learning", response.data)
