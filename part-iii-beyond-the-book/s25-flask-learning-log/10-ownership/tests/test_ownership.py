"""Tests for ownership: each user sees only their own topics, and other people's topics are not found, for chapter 10."""

import os
import unittest

from flask_log import create_app
from flask_log.database import Base
from flask_log.models import Entry, Topic, User

SEED_PATH = os.path.join(os.path.dirname(__file__), "..", "seed.json")


class OwnershipTests(unittest.TestCase):
    """Check who can see and change what. Sam owns the example topics; Alex has a topic of his own."""

    def setUp(self) -> None:
        """Build the app, create Sam (user 1, who owns Chess) and Alex, and load the seed data."""
        self.app = create_app({"DATABASE_URL": "sqlite:///:memory:", "TESTING": True})
        Base.metadata.create_all(self.app.extensions["engine"])
        with self.app.extensions["session_factory"]() as session:
            for username in ("sam", "alex"):
                user = User(username=username)
                user.set_password("a-long-password-1")
                session.add(user)
            session.commit()
        self.app.test_cli_runner().invoke(args=["load-seed", SEED_PATH])
        with self.app.extensions["session_factory"]() as session:
            alex = session.query(User).filter_by(username="alex").one()
            session.add(Topic(text="Gardening", owner_id=alex.id))
            session.commit()
        self.sam_client = self.app.test_client()
        self.sam_client.post("/accounts/login/", data={"username": "sam", "password": "a-long-password-1"})
        self.alex_client = self.app.test_client()
        self.alex_client.post("/accounts/login/", data={"username": "alex", "password": "a-long-password-1"})

    def test_topics_list_needs_sign_in(self) -> None:
        """A visitor who isn't signed in should be sent to the login page, not shown the list."""
        response = self.app.test_client().get("/topics/")
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.headers["Location"].startswith("/accounts/login/"))

    def test_each_user_sees_only_their_own_topics(self) -> None:
        """Sam sees Chess, and Alex sees Gardening, but neither sees the other's topic."""
        sam_page = self.sam_client.get("/topics/").data
        alex_page = self.alex_client.get("/topics/").data
        self.assertIn(b"Chess", sam_page)
        self.assertNotIn(b"Gardening", sam_page)
        self.assertIn(b"Gardening", alex_page)
        self.assertNotIn(b"Chess", alex_page)

    def test_another_users_topic_gives_not_found(self) -> None:
        """Alex opening Sam's topic should get the 404 page, the same as a topic that doesn't exist."""
        response = self.alex_client.get("/topics/1/")
        self.assertEqual(response.status_code, 404)

    def test_another_user_cannot_add_an_entry(self) -> None:
        """Alex can't add an entry to Sam's topic, and nothing is saved."""
        response = self.alex_client.post("/topics/1/new_entry/", data={"text": "Sneaky note."})
        self.assertEqual(response.status_code, 404)
        with self.app.extensions["session_factory"]() as session:
            self.assertEqual(session.query(Entry).filter_by(text="Sneaky note.").count(), 0)

    def test_two_users_can_use_the_same_topic_name(self) -> None:
        """Names only have to be unique for each user, so Alex can have a topic called Chess too."""
        response = self.alex_client.post("/topics/new/", data={"text": "Chess"})
        self.assertEqual(response.status_code, 302)
        with self.app.extensions["session_factory"]() as session:
            self.assertEqual(session.query(Topic).filter_by(text="Chess").count(), 2)
