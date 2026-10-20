"""Tests for the new entry form, for chapter 7 of the Flask Learning Log."""

import os
import unittest

from flask_log import create_app
from flask_log.database import Base
from flask_log.models import Entry

SEED_PATH = os.path.join(os.path.dirname(__file__), "..", "seed.json")


class NewEntryTests(unittest.TestCase):
    """Check the form for adding an entry under a topic."""

    def setUp(self) -> None:
        """Build the app with the example topics loaded, so Chess has two entries to start with."""
        self.app = create_app({"DATABASE_URL": "sqlite:///:memory:", "TESTING": True})
        Base.metadata.create_all(self.app.extensions["engine"])
        self.app.test_cli_runner().invoke(args=["load-seed", SEED_PATH])
        self.client = self.app.test_client()

    def count_entries_for(self, topic_id: int) -> int:
        """How many entries belong to this topic, read from the database."""
        with self.app.extensions["session_factory"]() as session:
            return session.query(Entry).filter_by(topic_id=topic_id).count()

    def test_new_entry_form_loads(self) -> None:
        """The form for Chess should load, with a text box in it."""
        response = self.client.get("/topics/1/new_entry/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<textarea", response.data)

    def test_valid_entry_is_saved_under_its_topic(self) -> None:
        """A new entry should be saved under Chess, and the browser sent back to the topic page."""
        response = self.client.post("/topics/1/new_entry/", data={"text": "Pawns move forward."})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers["Location"], "/topics/1/")
        self.assertEqual(self.count_entries_for(1), 3)

    def test_blank_entry_is_rejected(self) -> None:
        """A blank entry should not be saved, and the form should explain why."""
        response = self.client.post("/topics/1/new_entry/", data={"text": "   "})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Please write something for this entry.", response.data)
        self.assertEqual(self.count_entries_for(1), 2)

    def test_missing_topic_gives_not_found(self) -> None:
        """An entry form for a topic that doesn't exist should give the 404 page."""
        response = self.client.get("/topics/9999/new_entry/")
        self.assertEqual(response.status_code, 404)

    def test_topic_page_links_to_the_new_entry_form(self) -> None:
        """Chess's page should link to the form for adding an entry."""
        response = self.client.get("/topics/1/")
        self.assertIn(b'href="/topics/1/new_entry/"', response.data)
