"""Tests for the blogs app, for exercise 19-1."""

from django.test import TestCase

from .models import Blog, BlogPost


class BlogModelTests(TestCase):
    """Check the Blog and BlogPost models."""

    def test_blog_string_is_its_title(self) -> None:
        """A blog should display as its title."""
        blog = Blog.objects.create(title="Travel")
        self.assertEqual(str(blog), "Travel")

    def test_post_string_is_its_title(self) -> None:
        """A post should display as its title."""
        blog = Blog.objects.create(title="Travel")
        post = BlogPost.objects.create(blog=blog, title="Lisbon", text="Trams and custard tarts.")
        self.assertEqual(str(post), "Lisbon")

    def test_posts_are_ordered_newest_first(self) -> None:
        """Posts should come out newest first, without any extra sorting in the view."""
        blog = Blog.objects.create(title="Travel")
        BlogPost.objects.create(blog=blog, title="First", text="One.")
        BlogPost.objects.create(blog=blog, title="Second", text="Two.")
        titles = [post.title for post in BlogPost.objects.all()]
        self.assertEqual(titles, ["Second", "First"])


class HomePageTests(TestCase):
    """Check the home page, which shows every post."""

    def test_home_page_loads(self) -> None:
        """The home page should load, using its own template."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blogs/index.html")

    def test_home_page_shows_posts_and_their_blog(self) -> None:
        """Each post should show its title and the blog it belongs to."""
        blog = Blog.objects.create(title="Travel")
        BlogPost.objects.create(blog=blog, title="Lisbon", text="Trams and custard tarts.")
        response = self.client.get("/")
        self.assertContains(response, "Lisbon")
        self.assertContains(response, "Travel")


class NewBlogTests(TestCase):
    """Check the page for making a new blog."""

    def test_new_blog_page_loads(self) -> None:
        """The new blog page should load, with the form."""
        response = self.client.get("/blogs/new/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blogs/new_blog.html")

    def test_submitting_the_form_saves_the_blog(self) -> None:
        """A valid submission should save the blog, then go back to the home page."""
        response = self.client.post("/blogs/new/", {"title": "Recipes"})
        self.assertRedirects(response, "/")
        self.assertTrue(Blog.objects.filter(title="Recipes").exists())


class NewPostTests(TestCase):
    """Check the page for writing a new post."""

    def setUp(self) -> None:
        """Make a blog for the posts to belong to."""
        self.blog = Blog.objects.create(title="Travel")

    def test_submitting_the_form_saves_the_post_to_the_blog(self) -> None:
        """A valid submission should save the post in its blog, then go back to the home page."""
        response = self.client.post(f"/blogs/{self.blog.id}/new_post/",
                                    {"title": "Lisbon", "text": "Trams and custard tarts."})
        self.assertRedirects(response, "/")
        post = BlogPost.objects.get(title="Lisbon")
        self.assertEqual(post.blog, self.blog)

    def test_missing_blog_returns_not_found(self) -> None:
        """A blog that doesn't exist should give a 404 page, not an error."""
        response = self.client.get("/blogs/9999/new_post/")
        self.assertEqual(response.status_code, 404)


class EditPostTests(TestCase):
    """Check the page for editing a post."""

    def setUp(self) -> None:
        """Make a post to edit."""
        self.blog = Blog.objects.create(title="Travel")
        self.post = BlogPost.objects.create(blog=self.blog, title="Lisbon", text="Trams.")

    def test_edit_page_loads_with_the_current_text(self) -> None:
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

    def test_missing_post_returns_not_found(self) -> None:
        """A post that doesn't exist should give a 404 page, not an error."""
        response = self.client.get("/posts/9999/edit/")
        self.assertEqual(response.status_code, 404)
