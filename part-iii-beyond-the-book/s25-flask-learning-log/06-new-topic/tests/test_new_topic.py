"""Tests for the new topic form, for chapter 6 of the Flask Learning Log."""

import os
import unittest

from flask_log import create_app
from flask_log.database import Base
from flask_log.models import Topic

SEED_PATH = os.path.join(os.path.dirname(__file__), "..", "seed.json")


class NewTopicTests(unittest.TestCase):
    """Check the new topic form and the checks on the name."""

    def setUp(self) -> None:
        """Build the app with the example topics loaded, so there's an existing name to clash with."""
        self.app = create_app({"DATABASE_URL": "sqlite:///:memory:", "TESTING": True})
        Base.metadata.create_all(self.app.extensions["engine"])
        self.app.test_cli_runner().invoke(args=["load-seed", SEED_PATH])
        self.client = self.app.test_client()

    def count_topics_named(self, text: str) -> int:
        """How many topics have exactly this text, read from the database."""
        with self.app.extensions["session_factory"]() as session:
            return session.query(Topic).filter_by(text=text).count()

    def test_new_topic_form_loads(self) -> None:
        """The form page should load, with a form in it."""
        response = self.client.get("/topics/new/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<form", response.data)

    def test_valid_name_is_saved_and_redirects_to_topics(self) -> None:
        """A new name should be saved, and the browser sent back to the topics list."""
        response = self.client.post("/topics/new/", data={"text": "Gardening"})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers["Location"], "/topics/")
        self.assertEqual(self.count_topics_named("Gardening"), 1)

    def test_empty_name_is_rejected(self) -> None:
        """An empty name should not be saved, and the form should explain why."""
        response = self.client.post("/topics/new/", data={"text": "   "})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Please enter a topic name.", response.data)

    def test_duplicate_name_is_rejected_ignoring_capitals(self) -> None:
        """chess should clash with Chess, so it's refused and nothing new is saved."""
        response = self.client.post("/topics/new/", data={"text": "chess"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"A topic with this name already exists.", response.data)
        self.assertEqual(self.count_topics_named("chess"), 0)
