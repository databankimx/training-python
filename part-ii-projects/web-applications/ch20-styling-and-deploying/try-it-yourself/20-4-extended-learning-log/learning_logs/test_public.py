"""Tests for public topics, for exercise 20-4."""

from django.contrib.auth.models import User
from django.test import TestCase

from .models import Topic


def make_user(username: str) -> User:
    """A user who can own topics."""
    return User.objects.create_user(username, f"{username}@example.com", "a-long-test-password-1")


class PublicTopicTests(TestCase):
    """Check that public topics are visible to everyone, and private ones are not."""

    def setUp(self) -> None:
        """Make two users: Sam owns a public topic and a private one."""
        self.sam = make_user("sam")
        self.alex = make_user("alex")
        self.public_topic = Topic.objects.create(text="Chess", owner=self.sam, public=True)
        self.private_topic = Topic.objects.create(text="Gardening", owner=self.sam)

    def test_new_topics_are_private_by_default(self) -> None:
        """A topic should be private unless its owner makes it public."""
        topic = Topic.objects.create(text="Rock Climbing", owner=self.sam)
        self.assertFalse(topic.public)

    def test_visitor_who_is_not_signed_in_can_read_a_public_topic(self) -> None:
        """A public topic should be readable without signing in."""
        response = self.client.get(f"/topics/{self.public_topic.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Chess")

    def test_visitor_who_is_not_signed_in_is_sent_to_log_in_for_a_private_topic(self) -> None:
        """A private topic should send a visitor who isn't signed in to the login page."""
        response = self.client.get(f"/topics/{self.private_topic.id}/")
        self.assertRedirects(response, f"/accounts/login/?next=/topics/{self.private_topic.id}/",
                             fetch_redirect_response=False)

    def test_home_page_lists_public_topics(self) -> None:
        """The home page should list public topics, for everyone to see."""
        response = self.client.get("/")
        self.assertContains(response, "Chess")
        self.assertNotContains(response, "Gardening")

    def test_visitor_who_is_not_the_owner_does_not_see_owner_links(self) -> None:
        """On someone else's public topic, the add, edit and delete links should be hidden."""
        self.client.force_login(self.alex)
        response = self.client.get(f"/topics/{self.public_topic.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Add new entry")
        self.assertNotContains(response, "Edit entry")

    def test_making_a_topic_public_on_the_form_saves_the_setting(self) -> None:
        """Ticking the Public box on the new topic form should save the topic as public."""
        self.client.force_login(self.alex)
        response = self.client.post("/topics/new/", {"text": "Gardening", "public": "on"})
        self.assertRedirects(response, "/topics/")
        self.assertTrue(Topic.objects.get(text="Gardening", owner=self.alex).public)
