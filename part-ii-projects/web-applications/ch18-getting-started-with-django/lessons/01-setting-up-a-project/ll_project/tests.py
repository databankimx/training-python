"""Tests for the project setup in chapter 18, step 1."""

from django.conf import settings
from django.test import SimpleTestCase


class ProjectSetupTests(SimpleTestCase):
    """Check that the project is set up the way the chapter describes."""

    def test_admin_site_is_routed(self) -> None:
        """The admin login page should load, which proves the URL configuration is working."""
        response = self.client.get("/admin/login/")
        self.assertEqual(response.status_code, 200)

    def test_database_is_sqlite(self) -> None:
        """The project uses a single SQLite file for its database."""
        self.assertEqual(settings.DATABASES["default"]["ENGINE"], "django.db.backends.sqlite3")
