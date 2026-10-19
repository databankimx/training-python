"""Tests for public topics, for chapter 12 of the Flask Learning Log."""

import os
import unittest

from flask_log import create_app
from flask_log.database import Base
from flask_log.models import Topic, User

SEED_PATH = os.path.join(os.path.dirname(__file__), "..", "seed.json")


class PublicTopicTests(unittest.TestCase):
    """Check who can read a topic. Chess is private, and Rock Climbing is public. Both belong to Sam."""

    def setUp(self) -> None:
        """Build the app, make Sam (user 1) and Alex, load the seed data, and sign both in."""
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

    def test_new_topic_is_private_unless_the_box_is_ticked(self) -> None:
        """A topic created without the Public box ticked should stay private."""
        self.sam_client.post("/topics/new/", data={"text": "Gardening"})
        with self.app.extensions["session_factory"]() as session:
            self.assertFalse(session.query(Topic).filter_by(text="Gardening").one().public)

    def test_ticking_the_box_makes_the_topic_public(self) -> None:
        """A topic created with the Public box ticked should be saved as public."""
        self.sam_client.post("/topics/new/", data={"text": "Gardening", "public": "on"})
        with self.app.extensions["session_factory"]() as session:
            self.assertTrue(session.query(Topic).filter_by(text="Gardening").one().public)

    def test_visitor_who_is_not_signed_in_can_read_a_public_topic(self) -> None:
        """Rock Climbing is public, so a visitor who isn't signed in can read it."""
        response = self.app.test_client().get("/topics/2/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Rock Climbing", response.data)

    def test_visitor_who_is_not_signed_in_is_sent_to_log_in_for_a_private_topic(self) -> None:
        """Chess is private, so a visitor who isn't signed in is sent to the login page."""
        response = self.app.test_client().get("/topics/1/")
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.headers["Location"].startswith("/accounts/login/"))

    def test_home_page_lists_the_public_topics(self) -> None:
        """The home page shows Rock Climbing, which is public, but not Chess, which is private."""
        response = self.app.test_client().get("/")
        self.assertIn(b"Rock Climbing", response.data)
        self.assertNotIn(b"Chess", response.data)

    def test_other_users_see_a_public_topic_without_the_owner_controls(self) -> None:
        """Alex can read Sam's public topic, but he doesn't see the add, edit or delete links."""
        response = self.alex_client.get("/topics/2/")
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b"Add new entry", response.data)
        self.assertNotIn(b"Delete entry", response.data)
