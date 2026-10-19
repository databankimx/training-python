"""Tests for the topics and entries models and the load-seed command, for chapter 10 of the Flask Learning Log."""

import os
import unittest

from flask_log import create_app
from flask_log.database import Base
from flask_log.models import Entry, Topic, User

SEED_PATH = os.path.join(os.path.dirname(__file__), "..", "seed.json")


class TopicModelTests(unittest.TestCase):
    """Check the Topic and Entry tables, using an in-memory database."""

    def setUp(self) -> None:
        """Build the app, create its tables, and make the user who owns the example topics (user 1)."""
        self.app = create_app({"DATABASE_URL": "sqlite:///:memory:", "TESTING": True})
        self.engine = self.app.extensions["engine"]
        Base.metadata.create_all(self.engine)
        self.session = self.app.extensions["session_factory"]()
        owner = User(username="sam")
        owner.set_password("a-long-password-1")
        self.session.add(owner)
        self.session.commit()
        self.owner_id = owner.id

    def tearDown(self) -> None:
        """Close the session."""
        self.session.close()

    def test_topic_is_saved_and_read_back(self) -> None:
        """A topic added to the session should be found again with its text."""
        self.session.add(Topic(text="Gardening", owner_id=self.owner_id))
        self.session.commit()
        topic = self.session.query(Topic).filter_by(text="Gardening").one()
        self.assertEqual(topic.text, "Gardening")

    def test_entry_belongs_to_its_topic(self) -> None:
        """An entry should be linked to its topic, and the topic should list it."""
        topic = Topic(text="Chess", owner_id=self.owner_id)
        topic.entries.append(Entry(text="Knights move in an L shape."))
        self.session.add(topic)
        self.session.commit()
        self.assertEqual(self.session.query(Entry).one().topic.text, "Chess")
        self.assertEqual(len(topic.entries), 1)

    def test_load_seed_adds_topics_and_entries(self) -> None:
        """The load-seed command should add the example topics and their entries."""
        result = self.app.test_cli_runner().invoke(args=["load-seed", SEED_PATH])
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(self.session.query(Topic).count(), 2)
        self.assertEqual(self.session.query(Entry).count(), 2)

    def test_load_seed_twice_adds_nothing_new(self) -> None:
        """Running load-seed again should skip rows that are already there."""
        runner = self.app.test_cli_runner()
        runner.invoke(args=["load-seed", SEED_PATH])
        runner.invoke(args=["load-seed", SEED_PATH])
        self.assertEqual(self.session.query(Topic).count(), 2)
        self.assertEqual(self.session.query(Entry).count(), 2)
