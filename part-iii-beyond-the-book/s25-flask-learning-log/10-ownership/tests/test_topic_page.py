"""Tests for the topic page, for chapter 10 of the Flask Learning Log."""

import os
import unittest

from flask_log import create_app
from flask_log.database import Base
from flask_log.models import User

SEED_PATH = os.path.join(os.path.dirname(__file__), "..", "seed.json")


class TopicPageTests(unittest.TestCase):
    """Check the page for one topic, for the user who owns it."""

    def setUp(self) -> None:
        """Build the app, make user 1 (who owns the example topics), sign them in, and load the seed data."""
        self.app = create_app({"DATABASE_URL": "sqlite:///:memory:", "TESTING": True})
        Base.metadata.create_all(self.app.extensions["engine"])
        with self.app.extensions["session_factory"]() as session:
            sam = User(username="sam")
            sam.set_password("a-long-password-1")
            session.add(sam)
            session.commit()
        self.client = self.app.test_client()
        self.client.post("/accounts/login/", data={"username": "sam", "password": "a-long-password-1"})
        self.app.test_cli_runner().invoke(args=["load-seed", SEED_PATH])

    def test_topic_page_loads(self) -> None:
        """Chess's page should load with a 200 response."""
        response = self.client.get("/topics/1/")
        self.assertEqual(response.status_code, 200)

    def test_topic_page_shows_its_entries(self) -> None:
        """The page should show the topic's name and both of its entries."""
        response = self.client.get("/topics/1/")
        self.assertIn(b"Chess", response.data)
        self.assertIn(b"Knights move in an L shape.", response.data)
        self.assertIn(b"Bishops stay on one color.", response.data)

    def test_missing_topic_gives_not_found(self) -> None:
        """A topic id that doesn't exist should give the 404 page."""
        response = self.client.get("/topics/9999/")
        self.assertEqual(response.status_code, 404)

    def test_topics_list_links_to_each_topic_page(self) -> None:
        """The topics list should link to each topic's page, which now exists."""
        response = self.client.get("/topics/")
        self.assertIn(b'href="/topics/1/"', response.data)
        self.assertIn(b'href="/topics/2/"', response.data)
