"""Tests for the learning_logs app in chapter 18, steps 2 to 6."""

from django.contrib.auth.models import User
from django.test import TestCase

from .models import Entry, Topic


class TopicModelTests(TestCase):
    """Check the Topic model."""

    def test_topic_string_is_its_text(self) -> None:
        """A topic should display as its text."""
        topic = Topic.objects.create(text="Rock Climbing")
        self.assertEqual(str(topic), "Rock Climbing")

    def test_date_added_is_set_automatically(self) -> None:
        """Django should fill in the date the topic was added."""
        topic = Topic.objects.create(text="Chess")
        self.assertIsNotNone(topic.date_added)


class EntryModelTests(TestCase):
    """Check the Entry model."""

    def setUp(self) -> None:
        """Make a topic for the entries to belong to."""
        self.topic = Topic.objects.create(text="Chess")

    def test_long_entry_is_shortened_in_its_string(self) -> None:
        """A long entry should display as its first 50 characters, followed by three dots."""
        entry = Entry.objects.create(topic=self.topic, text="a" * 80)
        self.assertEqual(str(entry), "a" * 50 + "...")

    def test_short_entry_is_shown_in_full(self) -> None:
        """A short entry should display as all of its text."""
        entry = Entry.objects.create(topic=self.topic, text="Knights move in an L shape.")
        self.assertEqual(str(entry), "Knights move in an L shape.")

    def test_deleting_a_topic_deletes_its_entries(self) -> None:
        """Entries belong to a topic, so they're removed along with it."""
        Entry.objects.create(topic=self.topic, text="The first note.")
        self.topic.delete()
        self.assertEqual(Entry.objects.count(), 0)


class AdminTests(TestCase):
    """Check that topics and entries can be seen in the admin site."""

    def setUp(self) -> None:
        """Create a superuser and sign them in."""
        self.user = User.objects.create_superuser("admin", "admin@example.com", "a-test-password")
        self.client.force_login(self.user)

    def test_topic_list_is_in_admin(self) -> None:
        """The admin page for topics should load and show the topics."""
        Topic.objects.create(text="Rock Climbing")
        response = self.client.get("/admin/learning_logs/topic/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Rock Climbing")

    def test_entry_list_is_in_admin(self) -> None:
        """The admin page for entries should load and show the entries."""
        topic = Topic.objects.create(text="Chess")
        Entry.objects.create(topic=topic, text="Knights move in an L shape.")
        response = self.client.get("/admin/learning_logs/entry/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Knights move in an L shape.")


class HomePageTests(TestCase):
    """Check the Learning Log home page."""

    def test_home_page_loads(self) -> None:
        """The home page should load, using its own template."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "learning_logs/index.html")

    def test_home_page_shows_the_title(self) -> None:
        """The home page should show the words Learning Log."""
        response = self.client.get("/")
        self.assertContains(response, "Learning Log")


class TopicsPageTests(TestCase):
    """Check the page that lists the topics."""

    def test_topics_page_loads(self) -> None:
        """The topics page should load, using its own template."""
        response = self.client.get("/topics/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "learning_logs/topics.html")

    def test_topics_page_lists_the_topics(self) -> None:
        """Every topic should appear on the topics page."""
        Topic.objects.create(text="Chess")
        Topic.objects.create(text="Rock Climbing")
        response = self.client.get("/topics/")
        self.assertContains(response, "Chess")
        self.assertContains(response, "Rock Climbing")

    def test_topics_page_links_to_each_topic(self) -> None:
        """Each topic should link to its own page."""
        topic = Topic.objects.create(text="Chess")
        response = self.client.get("/topics/")
        self.assertContains(response, f'href="/topics/{topic.id}/"')


class TopicPageTests(TestCase):
    """Check the page for one topic."""

    def setUp(self) -> None:
        """Make a topic with two entries."""
        self.topic = Topic.objects.create(text="Chess")
        Entry.objects.create(topic=self.topic, text="Knights move in an L shape.")
        Entry.objects.create(topic=self.topic, text="Bishops stay on one color.")

    def test_topic_page_loads(self) -> None:
        """The topic page should load, using its own template."""
        response = self.client.get(f"/topics/{self.topic.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "learning_logs/topic.html")

    def test_topic_page_shows_its_entries(self) -> None:
        """The topic page should show the topic's name and every one of its entries."""
        response = self.client.get(f"/topics/{self.topic.id}/")
        self.assertContains(response, "Chess")
        self.assertContains(response, "Knights move in an L shape.")
        self.assertContains(response, "Bishops stay on one color.")

    def test_missing_topic_returns_not_found(self) -> None:
        """A topic that doesn't exist should give a 404 page, not an error."""
        response = self.client.get("/topics/9999/")
        self.assertEqual(response.status_code, 404)
