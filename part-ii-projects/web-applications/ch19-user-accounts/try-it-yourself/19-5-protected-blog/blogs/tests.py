"""Tests for the blogs app, for exercises 19-1 and 19-5."""

from django.contrib.auth.models import User
from django.test import TestCase

from .models import Blog, BlogPost


def make_user(username: str) -> User:
    """A user who can own blogs."""
    return User.objects.create_user(username, f"{username}@example.com", "a-long-test-password-1")


class BlogModelTests(TestCase):
    """Check the Blog and BlogPost models."""

    def setUp(self) -> None:
        """Make the user who owns the blog."""
        self.owner = make_user("sam")

    def test_blog_string_is_its_title(self) -> None:
        """A blog should display as its title."""
        blog = Blog.objects.create(title="Travel", owner=self.owner)
        self.assertEqual(str(blog), "Travel")

    def test_post_string_is_its_title(self) -> None:
        """A post should display as its title."""
        blog = Blog.objects.create(title="Travel", owner=self.owner)
        post = BlogPost.objects.create(blog=blog, title="Lisbon", text="Trams and custard tarts.")
        self.assertEqual(str(post), "Lisbon")

    def test_posts_are_ordered_newest_first(self) -> None:
        """Posts should come out newest first, without any extra sorting in the view."""
        blog = Blog.objects.create(title="Travel", owner=self.owner)
        BlogPost.objects.create(blog=blog, title="First", text="One.")
        BlogPost.objects.create(blog=blog, title="Second", text="Two.")
        titles = [post.title for post in BlogPost.objects.all()]
        self.assertEqual(titles, ["Second", "First"])


class HomePageTests(TestCase):
    """Check the home page, which anyone can read."""

    def test_home_page_loads_without_signing_in(self) -> None:
        """The home page should load, using its own template, for a visitor who isn't signed in."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blogs/index.html")

    def test_home_page_shows_posts_and_their_blog(self) -> None:
        """Each post should show its title and the blog it belongs to."""
        blog = Blog.objects.create(title="Travel", owner=make_user("sam"))
        BlogPost.objects.create(blog=blog, title="Lisbon", text="Trams and custard tarts.")
        response = self.client.get("/")
        self.assertContains(response, "Lisbon")
        self.assertContains(response, "Travel")


class NewBlogTests(TestCase):
    """Check the page for making a new blog. Only registered users can make one."""

    def setUp(self) -> None:
        """Make a user and sign them in."""
        self.owner = make_user("sam")
        self.client.force_login(self.owner)

    def test_new_blog_page_loads(self) -> None:
        """The new blog page should load, with the form."""
        response = self.client.get("/blogs/new/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blogs/new_blog.html")

    def test_submitting_the_form_saves_the_blog_for_the_user(self) -> None:
        """A valid submission should save the blog under the signed-in user, then go back to the home page."""
        response = self.client.post("/blogs/new/", {"title": "Recipes"})
        self.assertRedirects(response, "/")
        self.assertEqual(Blog.objects.get(title="Recipes").owner, self.owner)

    def test_signed_out_visitor_is_sent_to_log_in(self) -> None:
        """A visitor who isn't signed in should be sent to the login page, and no blog should be saved."""
        self.client.logout()
        response = self.client.post("/blogs/new/", {"title": "Recipes"})
        self.assertRedirects(response, "/accounts/login/?next=/blogs/new/", fetch_redirect_response=False)
        self.assertFalse(Blog.objects.filter(title="Recipes").exists())


class NewPostTests(TestCase):
    """Check the page for writing a new post. Only the blog's owner can add to it."""

    def setUp(self) -> None:
        """Make a blog owned by Sam, and sign Sam in."""
        self.sam = make_user("sam")
        self.client.force_login(self.sam)
        self.blog = Blog.objects.create(title="Travel", owner=self.sam)

    def test_submitting_the_form_saves_the_post_to_the_blog(self) -> None:
        """A valid submission should save the post in its blog, then go back to the home page."""
        response = self.client.post(f"/blogs/{self.blog.id}/new_post/",
                                    {"title": "Lisbon", "text": "Trams and custard tarts."})
        self.assertRedirects(response, "/")
        self.assertEqual(BlogPost.objects.get(title="Lisbon").blog, self.blog)

    def test_another_users_blog_cannot_get_a_new_post(self) -> None:
        """A user who doesn't own the blog should get a 404 page, and no post should be saved."""
        self.client.force_login(make_user("alex"))
        response = self.client.post(f"/blogs/{self.blog.id}/new_post/", {"title": "Sneaky", "text": "Hello."})
        self.assertEqual(response.status_code, 404)
        self.assertFalse(BlogPost.objects.filter(title="Sneaky").exists())

    def test_missing_blog_returns_not_found(self) -> None:
        """A blog that doesn't exist should give a 404 page, not an error."""
        response = self.client.get("/blogs/9999/new_post/")
        self.assertEqual(response.status_code, 404)


class EditPostTests(TestCase):
    """Check the page for editing a post. Only the owner of the post's blog can edit it."""

    def setUp(self) -> None:
        """Make a post in a blog owned by Sam, and sign Sam in."""
        self.sam = make_user("sam")
        self.client.force_login(self.sam)
        self.blog = Blog.objects.create(title="Travel", owner=self.sam)
        self.post = BlogPost.objects.create(blog=self.blog, title="Lisbon", text="Trams.")

    def test_edit_page_loads_with_the_current_title(self) -> None:
        """The edit page should load, with the post's current title in the form."""
        response = self.client.get(f"/posts/{self.post.id}/edit/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blogs/edit_post.html")
        self.assertContains(response, "Lisbon")

    def test_saving_changes_updates_the_post(self) -> None:
        """A valid submission should change the post, then go back to the home page."""
        response = self.client.post(f"/posts/{self.post.id}/edit/",
                                    {"title": "Lisbon in May", "text": "Warmer, and quieter."})
        self.assertRedirects(response, "/")
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, "Lisbon in May")

    def test_another_users_post_cannot_be_edited(self) -> None:
        """A user who doesn't own the post's blog should get a 404 page, and the post should stay the same."""
        self.client.force_login(make_user("alex"))
        response = self.client.post(f"/posts/{self.post.id}/edit/", {"title": "Changed", "text": "Changed."})
        self.assertEqual(response.status_code, 404)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, "Lisbon")

    def test_missing_post_returns_not_found(self) -> None:
        """A post that doesn't exist should give a 404 page, not an error."""
        response = self.client.get("/posts/9999/edit/")
        self.assertEqual(response.status_code, 404)
