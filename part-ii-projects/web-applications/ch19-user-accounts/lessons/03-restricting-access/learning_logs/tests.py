"""Tests for the learning_logs app in chapter 19, steps 1 to 3 (and the chapter 18 steps before them)."""

from django.contrib.auth.models import User
from django.test import TestCase

from .models import Entry, Topic


def make_user(username: str = "sam") -> User:
    """A user who can own topics."""
    return User.objects.create_user(username, f"{username}@example.com", "a-long-test-password-1")


class TopicModelTests(TestCase):
    """Check the Topic model."""

    def setUp(self) -> None:
        """Make the user who owns the topics."""
        self.owner = make_user()

    def test_topic_string_is_its_text(self) -> None:
        """A topic should display as its text."""
        topic = Topic.objects.create(text="Rock Climbing", owner=self.owner)
        self.assertEqual(str(topic), "Rock Climbing")

    def test_date_added_is_set_automatically(self) -> None:
        """Django should fill in the date the topic was added."""
        topic = Topic.objects.create(text="Chess", owner=self.owner)
        self.assertIsNotNone(topic.date_added)

    def test_topic_belongs_to_its_owner(self) -> None:
        """A topic should record the user who created it."""
        topic = Topic.objects.create(text="Chess", owner=self.owner)
        self.assertEqual(topic.owner, self.owner)


class EntryModelTests(TestCase):
    """Check the Entry model."""

    def setUp(self) -> None:
        """Make a topic for the entries to belong to."""
        self.topic = Topic.objects.create(text="Chess", owner=make_user())

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
        Topic.objects.create(text="Rock Climbing", owner=self.user)
        response = self.client.get("/admin/learning_logs/topic/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Rock Climbing")

    def test_entry_list_is_in_admin(self) -> None:
        """The admin page for entries should load and show the entries."""
        topic = Topic.objects.create(text="Chess", owner=self.user)
        Entry.objects.create(topic=topic, text="Knights move in an L shape.")
        response = self.client.get("/admin/learning_logs/entry/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Knights move in an L shape.")


class HomePageTests(TestCase):
    """Check the Learning Log home page. The home page is open to everyone."""

    def test_home_page_loads(self) -> None:
        """The home page should load, using its own template, without signing in."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "learning_logs/index.html")

    def test_home_page_shows_the_title(self) -> None:
        """The home page should show the words Learning Log."""
        response = self.client.get("/")
        self.assertContains(response, "Learning Log")


class TopicsPageTests(TestCase):
    """Check the page that lists the signed-in user's topics."""

    def setUp(self) -> None:
        """Make the user who owns the topics, and sign them in."""
        self.owner = make_user()
        self.client.force_login(self.owner)

    def test_topics_page_loads(self) -> None:
        """The topics page should load, using its own template."""
        response = self.client.get("/topics/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "learning_logs/topics.html")

    def test_topics_page_lists_the_topics(self) -> None:
        """Every topic belonging to the user should appear on the topics page."""
        Topic.objects.create(text="Chess", owner=self.owner)
        Topic.objects.create(text="Rock Climbing", owner=self.owner)
        response = self.client.get("/topics/")
        self.assertContains(response, "Chess")
        self.assertContains(response, "Rock Climbing")

    def test_topics_page_links_to_each_topic(self) -> None:
        """Each topic should link to its own page."""
        topic = Topic.objects.create(text="Chess", owner=self.owner)
        response = self.client.get("/topics/")
        self.assertContains(response, f'href="/topics/{topic.id}/"')


class TopicPageTests(TestCase):
    """Check the page for one topic."""

    def setUp(self) -> None:
        """Make a topic with two entries, and sign in the user who owns it."""
        self.owner = make_user()
        self.client.force_login(self.owner)
        self.topic = Topic.objects.create(text="Chess", owner=self.owner)
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

    def test_topic_page_links_to_the_new_entry_form(self) -> None:
        """The topic page should link to the form for adding an entry to this topic."""
        response = self.client.get(f"/topics/{self.topic.id}/")
        self.assertContains(response, f'href="/topics/{self.topic.id}/new_entry/"')


class NewTopicTests(TestCase):
    """Check the form for adding a new topic. Only signed-in users can add topics."""

    def setUp(self) -> None:
        """Make a user and sign them in."""
        self.owner = make_user()
        self.client.force_login(self.owner)

    def test_new_topic_page_loads(self) -> None:
        """The new topic page should load, with the form."""
        response = self.client.get("/topics/new/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "learning_logs/new_topic.html")

    def test_submitting_the_form_saves_the_topic_for_the_user(self) -> None:
        """A valid submission should save the topic under the signed-in user, then go back to the topics page."""
        response = self.client.post("/topics/new/", {"text": "Gardening"})
        self.assertRedirects(response, "/topics/")
        topic = Topic.objects.get(text="Gardening")
        self.assertEqual(topic.owner, self.owner)

    def test_empty_submission_is_rejected(self) -> None:
        """An empty submission shouldn't save anything, and the form should show again."""
        response = self.client.post("/topics/new/", {"text": ""})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Topic.objects.count(), 0)

    def test_signed_out_visitor_is_sent_to_log_in(self) -> None:
        """A visitor who isn't signed in should be sent to the login page, and no topic should be saved."""
        self.client.logout()
        response = self.client.post("/topics/new/", {"text": "Gardening"})
        self.assertRedirects(response, "/accounts/login/?next=/topics/new/", fetch_redirect_response=False)
        self.assertEqual(Topic.objects.count(), 0)


class NewEntryTests(TestCase):
    """Check the form for adding a new entry to a topic."""

    def setUp(self) -> None:
        """Make a topic for the entries to belong to, and sign in its owner."""
        self.owner = make_user()
        self.client.force_login(self.owner)
        self.topic = Topic.objects.create(text="Chess", owner=self.owner)

    def test_new_entry_page_loads(self) -> None:
        """The new entry page should load, with the form."""
        response = self.client.get(f"/topics/{self.topic.id}/new_entry/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "learning_logs/new_entry.html")

    def test_submitting_the_form_saves_the_entry_to_the_topic(self) -> None:
        """A valid submission should save the entry under its topic, then go back to the topic page."""
        response = self.client.post(f"/topics/{self.topic.id}/new_entry/", {"text": "Pawns move forward."})
        self.assertRedirects(response, f"/topics/{self.topic.id}/")
        entry = Entry.objects.get(text="Pawns move forward.")
        self.assertEqual(entry.topic, self.topic)

    def test_empty_entry_is_rejected(self) -> None:
        """An empty submission shouldn't save an entry, and the form should show again."""
        response = self.client.post(f"/topics/{self.topic.id}/new_entry/", {"text": ""})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Entry.objects.count(), 0)


class EditEntryTests(TestCase):
    """Check the form for editing an existing entry."""

    def setUp(self) -> None:
        """Make a topic with one entry to edit, and sign in its owner."""
        self.owner = make_user()
        self.client.force_login(self.owner)
        self.topic = Topic.objects.create(text="Chess", owner=self.owner)
        self.entry = Entry.objects.create(topic=self.topic, text="Knights move in an L shape.")

    def test_edit_page_loads_with_the_current_text(self) -> None:
        """The edit page should load, with the entry's current text in the form."""
        response = self.client.get(f"/entries/{self.entry.id}/edit/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "learning_logs/edit_entry.html")
        self.assertContains(response, "Knights move in an L shape.")

    def test_saving_changes_updates_the_entry(self) -> None:
        """A valid submission should change the entry, then go back to its topic page."""
        response = self.client.post(f"/entries/{self.entry.id}/edit/", {"text": "Knights move in an L."})
        self.assertRedirects(response, f"/topics/{self.topic.id}/")
        self.entry.refresh_from_db()
        self.assertEqual(self.entry.text, "Knights move in an L.")

    def test_missing_entry_returns_not_found(self) -> None:
        """An entry that doesn't exist should give a 404 page, not an error."""
        response = self.client.get("/entries/9999/edit/")
        self.assertEqual(response.status_code, 404)

    def test_topic_page_links_to_the_edit_page(self) -> None:
        """Each entry on the topic page should link to its edit page."""
        response = self.client.get(f"/topics/{self.topic.id}/")
        self.assertContains(response, f'href="/entries/{self.entry.id}/edit/"')


class AccessTests(TestCase):
    """Check that each user sees only their own topics and entries."""

    def setUp(self) -> None:
        """Make two users, each with a topic and an entry."""
        self.sam = make_user("sam")
        self.alex = make_user("alex")
        self.sams_topic = Topic.objects.create(text="Chess", owner=self.sam)
        self.sams_entry = Entry.objects.create(topic=self.sams_topic, text="Knights move in an L shape.")
        self.alexs_topic = Topic.objects.create(text="Gardening", owner=self.alex)

    def test_topics_page_redirects_a_visitor_who_is_not_signed_in(self) -> None:
        """The topics page should send a visitor who isn't signed in to the login page."""
        response = self.client.get("/topics/")
        self.assertRedirects(response, "/accounts/login/?next=/topics/", fetch_redirect_response=False)

    def test_topic_page_redirects_a_visitor_who_is_not_signed_in(self) -> None:
        """A topic page should send a visitor who isn't signed in to the login page."""
        response = self.client.get(f"/topics/{self.sams_topic.id}/")
        self.assertRedirects(response, f"/accounts/login/?next=/topics/{self.sams_topic.id}/",
                             fetch_redirect_response=False)

    def test_topics_page_lists_only_the_users_own_topics(self) -> None:
        """Sam should see Sam's topic, and not Alex's."""
        self.client.force_login(self.sam)
        response = self.client.get("/topics/")
        self.assertContains(response, "Chess")
        self.assertNotContains(response, "Gardening")

    def test_another_users_topic_is_not_found(self) -> None:
        """A user who opens someone else's topic should get a 404 page."""
        self.client.force_login(self.alex)
        response = self.client.get(f"/topics/{self.sams_topic.id}/")
        self.assertEqual(response.status_code, 404)

    def test_another_users_topic_cannot_get_a_new_entry(self) -> None:
        """A user can't add an entry to someone else's topic."""
        self.client.force_login(self.alex)
        response = self.client.post(f"/topics/{self.sams_topic.id}/new_entry/", {"text": "Sneaky note."})
        self.assertEqual(response.status_code, 404)
        self.assertFalse(Entry.objects.filter(text="Sneaky note.").exists())

    def test_another_users_entry_cannot_be_edited(self) -> None:
        """A user can't edit an entry on someone else's topic."""
        self.client.force_login(self.alex)
        response = self.client.post(f"/entries/{self.sams_entry.id}/edit/", {"text": "Changed by Alex."})
        self.assertEqual(response.status_code, 404)
        self.sams_entry.refresh_from_db()
        self.assertEqual(self.sams_entry.text, "Knights move in an L shape.")
