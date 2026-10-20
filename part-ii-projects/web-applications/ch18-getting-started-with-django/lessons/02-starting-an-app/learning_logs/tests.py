"""Tests for the learning_logs app in chapter 18, step 2."""

from django.contrib.auth.models import User
from django.test import TestCase

from .models import Topic


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


class TopicAdminTests(TestCase):
    """Check that topics can be seen in the admin site."""

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
