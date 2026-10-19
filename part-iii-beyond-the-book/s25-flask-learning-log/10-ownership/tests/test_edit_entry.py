"""Tests for the edit entry form, for chapter 10 of the Flask Learning Log."""

import os
import unittest

from flask_log import create_app
from flask_log.database import Base
from flask_log.models import Entry, User

SEED_PATH = os.path.join(os.path.dirname(__file__), "..", "seed.json")


class EditEntryTests(unittest.TestCase):
    """Check the form for changing an existing entry, for the user who owns its topic."""

    def setUp(self) -> None:
        """Build the app with the example data loaded, and sign in user 1. Entry 1 is the Knights entry under Chess."""
        self.app = create_app({"DATABASE_URL": "sqlite:///:memory:", "TESTING": True})
        Base.metadata.create_all(self.app.extensions["engine"])
        with self.app.extensions["session_factory"]() as session:
            sam = User(username="sam")
            sam.set_password("a-long-password-1")
            session.add(sam)
            session.commit()
        self.app.test_cli_runner().invoke(args=["load-seed", SEED_PATH])
        self.client = self.app.test_client()
        self.client.post("/accounts/login/", data={"username": "sam", "password": "a-long-password-1"})

    def entry_text(self, entry_id: int) -> str:
        """The current text of an entry, read from the database."""
        with self.app.extensions["session_factory"]() as session:
            return session.get(Entry, entry_id).text

    def test_edit_form_shows_the_current_text(self) -> None:
        """The form should load with the entry's current text already in the box."""
        response = self.client.get("/entries/1/edit/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Knights move in an L shape.", response.data)

    def test_valid_edit_is_saved_and_redirects_to_the_topic(self) -> None:
        """A changed entry should be saved, and the browser sent back to its topic."""
        response = self.client.post("/entries/1/edit/", data={"text": "Knights move in an L."})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers["Location"], "/topics/1/")
        self.assertEqual(self.entry_text(1), "Knights move in an L.")

    def test_blank_edit_is_rejected(self) -> None:
        """A blank entry should not replace the old text, and the form should explain why."""
        response = self.client.post("/entries/1/edit/", data={"text": "  "})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Please write something for this entry.", response.data)
        self.assertEqual(self.entry_text(1), "Knights move in an L shape.")

    def test_missing_entry_gives_not_found(self) -> None:
        """An entry id that doesn't exist should give the 404 page."""
        response = self.client.get("/entries/9999/edit/")
        self.assertEqual(response.status_code, 404)

    def test_topic_page_links_to_the_edit_form(self) -> None:
        """Each entry on the topic page should link to its edit form."""
        response = self.client.get("/topics/1/")
        self.assertIn(b'href="/entries/1/edit/"', response.data)
