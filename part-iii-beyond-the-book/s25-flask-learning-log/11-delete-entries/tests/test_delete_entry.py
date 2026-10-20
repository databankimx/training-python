"""Tests for deleting entries, for chapter 11 of the Flask Learning Log."""

import os
import unittest

from flask_log import create_app
from flask_log.database import Base
from flask_log.models import Entry, User

SEED_PATH = os.path.join(os.path.dirname(__file__), "..", "seed.json")


class DeleteEntryTests(unittest.TestCase):
    """Check deleting an entry. Only the owner of the entry's topic can delete it."""

    def setUp(self) -> None:
        """Build the app, make Sam (user 1, who owns Chess) and Alex, load the seed data, and sign both in."""
        self.app = create_app({"DATABASE_URL": "sqlite:///:memory:", "TESTING": True})
        Base.metadata.create_all(self.app.extensions["engine"])
        with self.app.extensions["session_factory"]() as session:
            for username in ("sam", "alex"):
                user = User(username=username)
                user.set_password("a-long-password-1")
                session.add(user)
            session.commit()
        self.app.test_cli_runner().invoke(args=["load-seed", SEED_PATH])
        self.sam_client = self.app.test_client()
        self.sam_client.post("/accounts/login/", data={"username": "sam", "password": "a-long-password-1"})
        self.alex_client = self.app.test_client()
        self.alex_client.post("/accounts/login/", data={"username": "alex", "password": "a-long-password-1"})

    def entry_exists(self, entry_id: int) -> bool:
        """Whether an entry with this id is still in the database."""
        with self.app.extensions["session_factory"]() as session:
            return session.get(Entry, entry_id) is not None

    def test_confirmation_page_loads_without_deleting(self) -> None:
        """The confirmation page should show the entry and ask first. Nothing is deleted by a GET."""
        response = self.sam_client.get("/entries/1/delete/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Delete this entry?", response.data)
        self.assertTrue(self.entry_exists(1))

    def test_owner_can_delete_the_entry(self) -> None:
        """Confirming the delete should remove the entry, then send the owner back to the topic."""
        response = self.sam_client.post("/entries/1/delete/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers["Location"], "/topics/1/")
        self.assertFalse(self.entry_exists(1))

    def test_another_user_gets_not_found_and_the_entry_stays(self) -> None:
        """Alex can't delete Sam's entry. He gets the 404 page, and the entry is still there."""
        response = self.alex_client.post("/entries/1/delete/")
        self.assertEqual(response.status_code, 404)
        self.assertTrue(self.entry_exists(1))

    def test_topic_page_links_to_the_delete_page(self) -> None:
        """Each entry on the topic page should link to its delete page."""
        response = self.sam_client.get("/topics/1/")
        self.assertIn(b'href="/entries/1/delete/"', response.data)

    def test_signed_out_visitor_is_sent_to_log_in(self) -> None:
        """A visitor who isn't signed in should be sent to the login page, and the entry should stay."""
        response = self.app.test_client().post("/entries/1/delete/")
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.headers["Location"].startswith("/accounts/login/"))
        self.assertTrue(self.entry_exists(1))
