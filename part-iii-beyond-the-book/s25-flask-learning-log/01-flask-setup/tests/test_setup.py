"""Tests for the Flask setup, for chapter 1 of the Flask Learning Log."""

import unittest

from flask_log import create_app


class SetupTests(unittest.TestCase):
    """Check that the app starts, serves its home page, and has a working database connection."""

    def setUp(self) -> None:
        """Build the app with its own in-memory database, so tests never touch the learner's file."""
        self.app = create_app({"DATABASE_URL": "sqlite:///:memory:", "TESTING": True})
        self.client = self.app.test_client()

    def test_home_page_loads(self) -> None:
        """The home page should answer with 200 OK."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_says_learning_log(self) -> None:
        """The home page should show the app's name."""
        response = self.client.get("/")
        self.assertIn(b"Learning Log", response.data)

    def test_database_connection_is_made(self) -> None:
        """The app should keep an engine, so later steps can open sessions."""
        self.assertIsNotNone(self.app.extensions["engine"])
        self.assertIsNotNone(self.app.extensions["session_factory"])
