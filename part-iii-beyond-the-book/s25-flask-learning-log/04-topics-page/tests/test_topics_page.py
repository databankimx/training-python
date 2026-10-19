"""Tests for the topics page, for chapter 4 of the Flask Learning Log."""

import os
import unittest

from flask_log import create_app
from flask_log.database import Base

SEED_PATH = os.path.join(os.path.dirname(__file__), "..", "seed.json")


class TopicsPageTests(unittest.TestCase):
    """Check the topics page, using an in-memory database loaded with the seed data."""

    def setUp(self) -> None:
        """Build the app, create its tables, and load the example topics."""
        self.app = create_app({"DATABASE_URL": "sqlite:///:memory:", "TESTING": True})
        Base.metadata.create_all(self.app.extensions["engine"])
        self.app.test_cli_runner().invoke(args=["load-seed", SEED_PATH])
        self.client = self.app.test_client()

    def test_topics_page_loads(self) -> None:
        """The topics page should load, using its own template."""
        response = self.client.get("/topics/")
        self.assertEqual(response.status_code, 200)

    def test_topics_page_lists_every_topic(self) -> None:
        """Both example topics should appear on the page."""
        response = self.client.get("/topics/")
        self.assertIn(b"Chess", response.data)
        self.assertIn(b"Rock Climbing", response.data)

    def test_each_topic_links_to_its_page(self) -> None:
        """Each topic should link to its own page, by its id."""
        response = self.client.get("/topics/")
        self.assertIn(b'href="/topics/1/"', response.data)
        self.assertIn(b'href="/topics/2/"', response.data)

    def test_navigation_bar_links_to_topics(self) -> None:
        """The shared navigation bar should link to the topics page."""
        response = self.client.get("/")
        self.assertIn(b'href="/topics/"', response.data)
